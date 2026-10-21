[返回仓库首页](../README.md) · [完整作品目录](../CATALOG.md)

# 科幻小说作品集

收集科幻小说原文，并集中维护在线阅读所需的作者、作品与版本元信息。

**[在线阅读](https://veejaliu.github.io/ScienceFictionCollection-Web/)** · **[阅读器 Web 仓库](https://github.com/VeejaLiu/ScienceFictionCollection-Web)** · **[元信息维护指南](../metadata/README.md)**

## 两个仓库的分工

| 项目 | 负责内容 |
| --- | --- |
| [ScienceFictionCollection](https://github.com/VeejaLiu/ScienceFictionCollection)（本仓库） | 作者与系列目录中的小说原文，以及 `metadata/` 中的姓名、简介、语言版本、头像和封面 |
| [ScienceFictionCollection-Web](https://github.com/VeejaLiu/ScienceFictionCollection-Web) | 书架与列表、在线阅读、语言与版本切换、阅读进度、SEO 和 GitHub Pages 发布 |

当前登记 **17 位作者及1个出版机构、226 组作品、228 个作品文件**。网页通过 metadata 中的 `directory`、`path` 绑定文件，内部 ID 保持稳定，对外使用可读的 slug。截至2026年10月18日，已逐项核对全部作品文件，累计修正30个年份标注、1个版本名称，并将误署名阿西莫夫的《被遗忘的世界》节写本按原作归入柯南·道尔目录；不同译本和版本均保留。[核对来源、年份口径及5个待核条目](../metadata/publication-years/verification.json) 单独登记，[本轮8项追查记录](../metadata/publication-years/follow-up-2026-10-18.json) 包括已查明事实和未决原因。

《创世纪》的空文件尚未补入正文：已登记[番茄小说官方合集目录](https://fanqienovel.com/page/7363514084773350462)及版权页，但平台篇目与2004—2005年原刊尚未比对，也未查到可再分发的开放许可文本。目录明确标注正文缺失；其余待核条目保留原状。

## 在线阅读与语言版本

阅读器支持简体中文、繁体中文、英文、法语、德语、俄语、日语和韩语界面。界面翻译不等于正文翻译：当前正文以中文为主，简繁体按文件登记；《火星纪事》EPUB 已核对为繁体。其他语言版本需要收录真实文件，并通过相同的 `workId` 关联。

每本书优先选择当前界面语言，其次英文，最后选择一个已有语言版本；书架、列表与阅读页均保留版本切换。TXT/Markdown 打开后按需加载正文并保存本机阅读进度；EPUB 支持浏览器内阅读、目录跳转、翻页和位置恢复；PDF 提供原始文件入口。目录及网站构建只读取元信息和图片，不批量读取或打包小说正文。

## 元信息与图片

- `metadata/authors.json`：作者 ID、slug、真实目录、多语言姓名、简介和资料来源。
- `metadata/books/<作者 ID>.json`：文件 ID、作品 `workId`、slug、正文路径、语言、格式、系列和封面。
- `metadata/avatars/`、`metadata/covers/`：WebP 头像和封面；头像最长边 160 像素，封面不超过 600 × 900 像素。
- [封面整理清单](../metadata/covers/catalog.json)：全部 211 条记录的检索结果，已为 61 条记录整理封面，其中 6 张来自对应 EPUB；未确认的使用生成式封面。清单保留来源、版本说明及图片摘要。

## 维护与更新

在本仓库根目录执行：

```bash
python3 metadata/sync.py
python3 metadata/sync.py --check
python3 script.py
```

同步脚本只读取文件名、路径和文件大小，保留已有元信息字段；移动文件时先更新 `path`，保留文件 ID、作品 `workId` 和 slug。新增作者或翻译版本的字段说明见 [metadata/README.md](../metadata/README.md)。

README 首页与完整作品目录由 `script.py` 自动生成；本说明文档单独维护。

2026年10月21日新增的用户文件包括太空漫游四部曲拆分EPUB、《2061》TXT、《海中山》及《科幻世界》2026年第5、6期，新增7组作品、8份文件；来源、广告清理及完整性核对见 [元信息维护指南](../metadata/README.md#本轮用户提供的小说与期刊2026年10月21日)。期刊按出版机构、年份及期号登记，保留整期文章署名。

Web 主分支更新后由 GitHub Actions 自动发布。仅修改本仓库元信息时，在 [Web 的 Pages 发布工作流](https://github.com/VeejaLiu/ScienceFictionCollection-Web/actions/workflows/pages.yml) 选择 **Run workflow** 即可重新构建网站；发布会读取本仓库 `master` 的 metadata，正文则在阅读时从本仓库按需获取。

## 来源与权利记录

详见 [授权范围](../LICENSE-SCOPE.md)；现有 [MIT LICENSE](../LICENSE) 保留原文。

小说正文、作者头像、出版社封面与应用代码分别保留各自的权利归属。书目或封面来源链接不代表获得开放许可；封面出处与版本匹配说明见整理清单，阅读器自有代码及第三方素材的授权记录见 [Web 仓库说明](https://github.com/VeejaLiu/ScienceFictionCollection-Web/blob/master/docs/PROJECT.md#上游来源与应用授权)。

## Star History

[![Star History Chart](https://star-history.dera.page/svg?repos=VeejaLiu/ScienceFictionCollection&type=Date)](https://star-history.dera.page/#VeejaLiu/ScienceFictionCollection&Date)
