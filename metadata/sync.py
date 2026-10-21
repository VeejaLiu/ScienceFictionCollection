"""Update file metadata using names/stat only; never read novel bodies."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import unicodedata


def slugify(value):
    value = unicodedata.normalize('NFKC', value).lower()
    return re.sub(r'[-_]+', '-', re.sub(r'[^\w]+', '-', value)).strip('-')


def valid_slug(value):
    return isinstance(value, str) and value == slugify(value) and bool(value)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='validate without writing')
    args = parser.parse_args()
    metadata = Path(__file__).resolve().parent
    root = metadata.parent
    authors = json.loads((metadata / 'authors.json').read_text(encoding='utf-8'))['authors']
    periodicals_file = metadata / 'periodicals.json'
    periodicals = json.loads(periodicals_file.read_text(encoding='utf-8'))['periodicals'] if periodicals_file.exists() else []
    owners = authors + periodicals

    def manifest_for(owner):
        relative = owner.get('issuesFile') if owner.get('kind') == 'periodical' else owner.get('booksFile')
        if not isinstance(relative, str) or '\\' in relative or Path(relative).is_absolute() or '..' in Path(relative).parts:
            raise SystemExit('目录清单必须是 metadata 内的相对路径。')
        return metadata / relative

    def entries_key(owner):
        return 'issues' if owner.get('kind') == 'periodical' else 'books'

    author_slugs = set()
    used_slugs = set()
    for author in owners:
        if not isinstance(author.get('id'), str) or not re.fullmatch(r'[a-z0-9][a-z0-9-]*', author['id']):
            raise SystemExit('作者 id 只能包含小写字母、数字和连字符。')
        slug = author.get('slug')
        if not valid_slug(slug) or slug in author_slugs:
            raise SystemExit('作者 slug 必须是唯一的名称，用连字符分词。')
        author_slugs.add(slug)
        manifest = manifest_for(author)
        if manifest.exists():
            for book in json.loads(manifest.read_text(encoding='utf-8'))[entries_key(author)]:
                if not valid_slug(book.get('slug')) or book['slug'] in used_slugs:
                    raise SystemExit('作品 slug 必须全局唯一且有意义。请先修正 metadata。')
                used_slugs.add(book['slug'])
        directory = author.get('directory')
        if not isinstance(directory, str) or '\\' in directory or Path(directory).is_absolute() or '..' in Path(directory).parts:
            raise SystemExit('作者 directory 必须是小说仓库内的相对目录。')
        if not (root / directory).resolve().is_relative_to(root.resolve()):
            raise SystemExit('作者目录不能指向小说仓库之外。')
    registered = {author['directory'] for author in owners}
    actual = {path.name for path in root.iterdir() if path.is_dir() and re.match(r'^\d{3} - ', path.name)}
    if actual - registered or any(not (root / path).is_dir() for path in registered):
        raise SystemExit('请先在 metadata/authors.json 或 periodicals.json 中注册或更新目录。')
    changed = []
    total = 0
    for author in owners:
        directory = root / author['directory']
        manifest = manifest_for(author)
        key = entries_key(author)
        owner_key = 'periodicalId' if author.get('kind') == 'periodical' else 'authorId'
        old = json.loads(manifest.read_text(encoding='utf-8')) if manifest.exists() else {'schemaVersion': 1, owner_key: author['id'], key: []}
        previous = {book['path']: book for book in old[key]}
        books = []
        for path in sorted(directory.rglob('*')):
            if not path.is_file() or path.suffix.lower() not in ['.txt', '.md', '.epub', '.pdf']:
                continue
            relative = path.relative_to(directory).as_posix()
            # Bibliography Markdown remains an author reference, not a novel.
            if path.suffix.lower() == '.md' and relative not in previous:
                continue
            if path.is_symlink():
                raise SystemExit(f'不支持符号链接作品：{path}')
            titles = re.findall(r'《([^》]+)》', path.stem)
            book = previous.get(relative, {
                'id': author['id'] + '-' + hashlib.sha256(relative.encode()).hexdigest()[:12],
                'path': relative, 'title': ' '.join(titles) if titles else path.stem,
                'format': path.suffix[1:].lower(), 'language': 'zh-CN',
                'series': path.parent.relative_to(directory).as_posix() if path.parent != directory else '',
                'cover': None,
            }).copy()
            if author.get('kind') == 'periodical' and relative not in previous:
                issue = re.search(r'(\d{4})年第(\d+)期', path.stem)
                if not issue:
                    raise SystemExit(f'新增期刊文件名须明确年份和期号，或先人工登记 publication：{relative}')
                year, number = map(int, issue.groups())
                book.update({'title': f"{author['name']}（{year}年第{number}期）", 'contentType': 'periodical',
                             'publication': {'kind': 'periodical-issue', 'yearBasis': 'issue-publication',
                                             'issueYear': year, 'issueNumber': number}})
            if relative not in previous:
                base = slugify(book['title'])
                if not base:
                    raise SystemExit(f'请为作品设置有意义的标题：{relative}')
                slug = base
                if slug in used_slugs:
                    slug = f"{base}-{book['format']}"
                if slug in used_slugs:
                    slug = f"{base}-{book['format']}-{author['slug']}"
                number = 2
                while slug in used_slugs:
                    slug = f"{base}-{book['format']}-{author['slug']}-{number}"
                    number += 1
                book['slug'] = slug
                used_slugs.add(slug)
            if relative not in previous:
                book['workId'] = book['id']
            book['size'] = path.stat().st_size
            book['format'] = path.suffix[1:].lower()
            books.append(book)
        updated = {**old, key: books}
        if updated != old:
            changed.append(str(manifest.relative_to(root)))
            if not args.check:
                manifest.write_text(json.dumps(updated, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        total += len(books)
    if changed and args.check:
        raise SystemExit('元信息需要更新：' + ', '.join(changed))
    print(f'{len(authors)} 位作者、{len(periodicals)} 种期刊，{total} 个文件；' + ('已更新。' if changed else '无需更新。') + '未读取正文。')


if __name__ == '__main__':
    main()
