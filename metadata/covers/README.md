# 封面目录与命名

[返回元信息说明](../README.md)

查找某本书的封面，先在作者的作品清单或期刊分期清单中查看 `cover`；需要了解版本和来源时，在 [catalog.json](catalog.json) 按书名、`bookId` 或 `asset` 查找。来源编号、ISBN、图片摘要与版本匹配说明保留在该清单中。

## 现有目录

| 位置 | 当前含义 | 使用时注意 |
| --- | --- | --- |
| `editions/` | 出版参考版本封面，多以 Open Library 图片编号命名 | 参考版本不等于正文的实际译本或版次 |
| `embedded/` | 从已收录 EPUB 提取的封面，多以作品文件ID命名 | 文件名说明关联标识，但难以直接辨认书名 |
| `periodicals/` | 原刊封面素材，文件名包含刊名和卷期 | 包括为短篇使用的原刊封面，不等同于网站“期刊”分类 |
| 本目录下的三体系列 SVG/WebP | 项目生成的示例插画 | 不是出版社版本封面 |
| `catalog.json` | 每个阅读文件的封面匹配、来源与图像摘要 | 同一张图片可供多个已明确登记的版本共用 |
| `sources.json`、`title-aliases.json` | 生成素材说明、检索别名 | 不代替作品或分期清单 |

现有结构便于追溯素材来源，但不够适合按作者和书名查找。分类混合了获取方式（embedded）、参考版本（editions）与出版物类型（periodicals）；`openlibrary-13022431.webp` 或作品ID式文件名也难以直接辨认内容。

## 后续统一组织建议

人工维护更适合以“作者／作品／版本”作为主要查找层级，把来源平台编号、内部ID与SHA-256留在 `catalog.json`，例如：

```text
covers/
  works/<作者slug>/<作品slug>/<版本说明>.webp
  journals/<刊物slug>/<年份>-<期号>.webp
  generated/<作品slug>.svg
  generated/<作品slug>.webp
  catalog.json
```

作品和刊物沿用其稳定slug，版本说明采用能确认的年份、语言或用途，例如 `2019-zh-cn`、`reference`、`generated-artwork`；未知版次不推测补写。共享原刊封面只保存一份，通过清单关联多个作品。

上面的目录是下一次统一迁移的建议，当前图片文件未改名。本次仅迁移作者元信息文件并更新引用，封面素材与对应来源记录继续按现有路径使用。
