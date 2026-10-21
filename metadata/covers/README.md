# 封面目录与命名

[返回元信息说明](../README.md)

封面以“作者／作品／版本”归档。文件名说明实际用途或已确认的版次，不再使用来源平台编号、作品ID或哈希作为图片文件名。来源编号、ISBN、原图摘要、当前图片摘要及权利说明保留在 [catalog.json](catalog.json) 中。

## 当前目录

```text
covers/
  works/<作者slug>/<作品名称slug>/<版本说明>.webp
  journals/<刊物slug>/<年份>/issue-<期号>-<版本说明>.webp
  catalog.json
  title-aliases.json
  README.md
```

例如：

```text
works/liu-cixin/三体/reference-edition.webp
works/arthur-c-clarke/2061-太空漫游/2019-zh-cn-epub-cover.webp
works/orson-scott-card/死者代言人/zh-cn-epub-cover.webp
works/orson-scott-card/死者代言人/reference-edition.webp
works/philip-k-dick/the-variable-man/1953-09-original-magazine.webp
journals/science-fiction-world/2026/issue-05-zh-cn-epub.webp
```

作品目录采用可读书名；同一作品的不同格式、译本或参考封面放在一起。期刊目录中的 `issue-05` 表示第5期，不推测为5月刊。期号补零便于按文件名排列，清单中的期号仍使用整数。

## 版本说明

| 名称 | 含义 |
| --- | --- |
| `reference-edition` | 出版参考版封面，不能据此认定与正文的译本或纸本版次一致 |
| `1895-reference-edition` | 已有来源支持1895年参考封面，不以正文原作年份代替封面版次 |
| `zh-cn-epub-cover`、`zh-tw-epub-cover`、`en-epub-cover` | 对应所收录EPUB版本的封面，语言标记来自该正文版本 |
| `2019-zh-cn-epub-cover` | 已明确登记2019年中文版本的EPUB封面 |
| `上册-zh-cn-epub-cover` | 上册EPUB的封面，卷册信息作为版本说明保留 |
| `1953-09-original-magazine` | 原作首发刊期的封面素材，不冒充独立单行本封面 |

只有有来源依据的年份、语言或卷册信息才进入版本名；未知信息不推测补写。同一张封面若服务于多个版本，只保存一份，由各自清单明确引用；共享参考封面不表示这些正文版本相同。

## 清单与维护

- 各作者作品清单、期刊分期清单中的 `cover` 是当前使用关系；文件路径相对于 metadata。
- `catalog.json` 的 `entries` 按 `bookId` 保存匹配记录，`asset` 指向当前图片；`source` 保留来源编号、原始链接、ISBN、版本与权利信息。
- `sha256` 是当前WebP图片摘要，`sourceSha256` 是原始图像摘要；重命名不改变这些摘要。
- `assetVersion` 记录可读版本名，`storage` 统计当前图片数量与字节数；旧批量压缩统计保存在 `historicalCompressionBatch`，不冒充本次迁移统计。
- `title-aliases.json` 只用于书名检索，不生成封面图片。

新增图片先按上述结构命名，再登记来源和作品引用。删除图片前，以现有小说和期刊清单的 `cover` 引用确定是否仍在使用；引用中的图片保留，未引用的旧图、示例图及其废弃生成附件可以清理。没有封面的作品使用阅读器内的即时绘制逻辑，不需要存放示例图片。

2026年10月21日共迁移76张在用封面，删除3张未引用示例WebP及其3份SVG，并移除只用于这些示例的生成脚本和旧说明文件。在用图片未重编码，78个阅读文件继续使用这些封面。逐项旧路径、新路径、摘要与清理原因见 [封面整理记录](../acquisition/cover-organization-2026-10-21.json)；其中旧路径只用于历史追溯，不表示文件仍应存在。
