
<div align="center">
<img src="https://socialify.git.ci/VeejaLiu/ScienceFictionCollection/image?description=1&descriptionEditable=%E7%A7%91%E5%B9%BB%E5%B0%8F%E8%AF%B4%E4%BD%9C%E5%93%81%E9%9B%86&font=Bitter&name=1&owner=1&pattern=Floating%20Cogs&stargazers=1&theme=Dark" alt="ScienceFictionCollection" width="640" height="320" />
</div>

# 科幻小说作品集

收集科幻小说原文，并集中维护在线阅读所需的作者、作品与版本元信息。

**[在线阅读](https://veejaliu.github.io/ScienceFictionCollection-Web/)** · **[阅读器 Web 仓库](https://github.com/VeejaLiu/ScienceFictionCollection-Web)** · **[元信息维护指南](metadata/README.md)**

## 两个仓库的分工

| 项目 | 负责内容 |
| --- | --- |
| [ScienceFictionCollection](https://github.com/VeejaLiu/ScienceFictionCollection)（本仓库） | 作者与系列目录中的小说原文，以及 `metadata/` 中的姓名、简介、语言版本、头像和封面 |
| [ScienceFictionCollection-Web](https://github.com/VeejaLiu/ScienceFictionCollection-Web) | 书架与列表、在线阅读、语言与版本切换、阅读进度、SEO 和 GitHub Pages 发布 |

当前登记 **12 位作者、210 组作品、211 个作品文件**。正文目录与文件名保留原有结构；网页通过 metadata 中的 `directory`、`path` 绑定文件，内部 ID 保持稳定，对外使用可读的 slug。

## 在线阅读与语言版本

阅读器支持简体中文、繁体中文、英文、法语、德语、俄语、日语和韩语界面。界面翻译不等于正文翻译：当前登记的正文均为简体中文，其他语言版本需要收录真实文件，并通过相同的 `workId` 关联。

每本书优先选择当前界面语言，其次英文，最后选择一个已有语言版本；书架、列表与阅读页均保留版本切换。TXT/Markdown 打开后按需加载正文并保存本机阅读进度，EPUB/PDF 提供原始文件入口。目录及网站构建只读取元信息和图片，不批量读取或打包小说正文。

## 元信息与图片

- `metadata/authors.json`：作者 ID、slug、真实目录、多语言姓名、简介和资料来源。
- `metadata/books/<作者 ID>.json`：文件 ID、作品 `workId`、slug、正文路径、语言、格式、系列和封面。
- `metadata/avatars/`、`metadata/covers/`：WebP 头像和封面；头像最长边 160 像素，封面不超过 600 × 900 像素。
- [封面整理清单](metadata/covers/catalog.json)：全部 211 条记录的检索结果，已为 61 条记录整理封面，其中 6 张来自对应 EPUB；未确认的使用生成式封面。清单保留来源、版本说明及图片摘要。

## 维护与更新

在本仓库根目录执行：

```bash
python3 metadata/sync.py
python3 metadata/sync.py --check
python3 script.py
```

同步脚本只读取文件名、路径和文件大小，保留已有元信息字段；移动文件时先更新 `path`，保留文件 ID、作品 `workId` 和 slug。新增作者或翻译版本的字段说明见 [metadata/README.md](metadata/README.md)。

本 README 的作者和文件目录由 `script.py` 自动生成；修改本页介绍时应同步修改脚本中的 `HEADER`，避免下次生成覆盖。

Web 主分支更新后由 GitHub Actions 自动发布。仅修改本仓库元信息时，在 [Web 的 Pages 发布工作流](https://github.com/VeejaLiu/ScienceFictionCollection-Web/actions/workflows/pages.yml) 选择 **Run workflow** 即可重新构建网站；发布会读取本仓库 `master` 的 metadata，正文则在阅读时从本仓库按需获取。

## 来源与权利记录

小说正文、作者头像、出版社封面与应用代码分别保留各自的权利归属。书目或封面来源链接不代表获得开放许可；封面出处与版本匹配说明见整理清单，阅读器自有代码及第三方素材的授权记录见 [Web 仓库说明](https://github.com/VeejaLiu/ScienceFictionCollection-Web#上游来源与应用授权)。


## 贡献者名单 Contributors
[![Contributors](https://contrib.rocks/image?repo=VeejaLiu/ScienceFictionCollection)](https://github.com/VeejaLiu/ScienceFictionCollection/graphs/contributors)

## 作家
- [001 - 刘慈欣(Cixin Liu)](#001---刘慈欣cixin-liu)
- [002 - Frank Herbert(弗兰克·赫伯特)](#002---frank-herbert弗兰克赫伯特)
- [003 - Isaac Asimov(艾萨克·阿西莫夫)](#003---isaac-asimov艾萨克阿西莫夫)
- [004 - Jules Gabriel Verne(儒勒·加布里埃尔·凡尔纳)](#004---jules-gabriel-verne儒勒加布里埃尔凡尔纳)
- [005 - Mary Shelley(玛丽·雪莱)](#005---mary-shelley玛丽雪莱)
- [006 - Ray Douglas Bradbury(雷·道格拉斯·布拉德伯里)](#006---ray-douglas-bradbury雷道格拉斯布拉德伯里)
- [007 - Orson Scott Card(奥森·斯科特·卡德)](#007---orson-scott-card奥森斯科特卡德)
- [008 - Ted Chiang(特德·姜)](#008---ted-chiang特德姜)
- [009 - Michael Swanwick (迈克尔·斯万维克) ](#009---michael-swanwick-迈克尔斯万维克)
- [010 - 王晋康](#010---王晋康)
- [011 - Andy Weir(安迪·威尔)](#011---andy-weir安迪威尔)
- [012 - Arthur Charles Clarke(亚瑟·查理斯·克拉克)](#012---arthur-charles-clarke亚瑟查理斯克拉克)

## 作品：
<div style="color:gray">（此顺序只代表本仓库先后的添加顺序）</div>

### 001 - 刘慈欣(Cixin Liu)
- 0-刘慈欣汇总.md _[19.63KB]_
- [1985]《宇宙坍缩》.txt _[19.91KB]_
- [1987]《微观尽头》.txt _[12.54KB]_
- [1989]《中国2185》.txt _[250.35KB]_
- [1991-1]《超新星纪元》(内地实体删节版).txt _[582.1KB]_
- [1991-1]《超新星纪元》(新创世纪-完整版).txt _[638.32KB]_
- [1997-1]《梦之海》.txt _[56.58KB]_
- [1997-2]《诗云》(李白).txt _[57.55KB]_
- [1997-3]《欢乐颂》.txt _[49.15KB]_
- [1998-1]《西洋》 .txt _[21.79KB]_
- [1998-2]《微纪元》.txt _[43.53KB]_
- [1998-3]《天使时代》(波斯湾飞马).txt _[61.28KB]_
- [1998-4]《光荣与梦想》.txt _[76.06KB]_
- [1998-5]《地球大炮》(深井).txt _[72.75KB]_
- [1999-1]《鲸歌》.txt _[21.38KB]_
- [1999-2]《带上她的眼晴》.txt _[25.71KB]_
- [1999-3]《信使》.txt _[13.28KB]_
- [1999-4]《混沌蝴蝶》.txt _[39.98KB]_
- [2000-1]《地火》.txt _[70.39KB]_
- [2000-2]《流浪地球》.txt _[68.95KB]_
- [2000-3]《乡村教师》.txt _[65.94KB]_
- [2000-4]《魔鬼积木》.txt _[201.16KB]_
- [2001-1]《全频带阻塞干扰》（中国版）.txt _[87.4KB]_
- [2001-1]《全频带阻塞干扰》（俄罗斯版）.txt _[87.53KB]_
- [2001-2]《中国太阳》.txt _[69.32KB]_
- [2001-3]《朝闻道》(爱因斯坦赤道).txt _[51.63KB]_
- [2001-4]《纤维》.txt _[14.91KB]_
- [2001-5]《命运》.txt _[17.58KB]_
- [2001-6]《球状闪电》.txt _[496.19KB]_
- [2002-1]《吞食者》.txt _[62.06KB]_
- [2002-2]《思想者》.txt _[32.8KB]_
- [2003-1]《白垩纪往事》(谁替恐龙剔牙).txt _[74.4KB]_
- [2003-2]《海水高山》.txt _[16.02KB]_
- [2003-3]《人生》.txt _[15.33KB]_
- [2004-1]《镜子》.txt _[96.61KB]_
- [2004-2]《圆圆的肥皂泡》.txt _[36.26KB]_
- [2004-3]《当恐龙遇上蚂蚁》（白垩纪往事）.txt _[202.09KB]_
- [2005-1]《山》.txt _[61.65KB]_
- [2005-2]《赡养上帝》.txt _[60.9KB]_
- [2005-3]《赡养人类》.txt _[82.9KB]_
- [2005]《创世纪》（超新星纪元中篇版）.txt _[0B]_
- [2006]《三体》.txt _[579.03KB]_
- [2008]《三体2黑暗森林》.txt _[979.37KB]_
- [2009]《月夜》.txt _[23.93KB]_
- [2010-1]《2018年4月1日》.txt _[16.01KB]_
- [2010-2]《太原之恋》.txt _[32.75KB]_
- [2010-3]《时间移民》.txt _[28.37KB]_
- [2010-4]《三体3死神永生》.txt _[1.05MB]_
- [2012]《烧火工》.txt _[28.03KB]_
- [2015-7]《圆》（人列计算机）.txt _[28.85KB]_
- [2016]《不能共存的节日》.txt _[10.39KB]_
- [2017]《黄金原野》.txt _[32.69KB]_
### 002 - Frank Herbert(弗兰克·赫伯特)
- [1965]《沙丘》(Dune).txt _[1.07MB]_
- [1969]《沙丘救世主》(Dune Messiah).txt _[448.95KB]_
- [1976]《沙丘之子》(Children of Dune).txt _[775.46KB]_
### 003 - Isaac Asimov(艾萨克·阿西莫夫)
- 基地系列
  - 1-基地三部曲
    - 基地三部曲1：[1951]《基地》(Foundation).txt _[435.46KB]_
    - 基地三部曲2：[1952]《基地与帝国》(Foundation and Empire).txt _[504.55KB]_
    - 基地三部曲3：[1953]《第二基地》(Second Foundation).txt _[466.83KB]_
  - 2-基地后传
    - 基地后传1：[1982]《基地边缘》(Foundation's Edge).txt _[865.78KB]_
    - 基地后传2：[1986]《基地与地球》(Foundation and Earth).txt _[852.57KB]_
  - 3-基地前传
    - 基地前传1：[1988]《基地前奏》(Prelude to Foundation).txt _[781.76KB]_
    - 基地前传2：[1993]《迈向基地》(Forward the Foundation).txt _[675.65KB]_
- 机器人系列
  - [1954]《钢穴》.txt _[434.98KB]_
  - [1957]《裸阳》.txt _[413.76KB]_
  - [1983]《曙光中的机器人》.txt _[209.53KB]_
  - [1985]《机器人与帝国》.txt _[233.38KB]_
- 银河帝国系列
  - 1 - [1951]《繁星若尘》.txt _[433.05KB]_
  - 2 - [1952]《星空暗流》.txt _[399.78KB]_
  - 3 - [1950]《苍穹微石》.txt _[433.25KB]_
- 0-IsaacAsimov.md _[51.06KB]_
- AL-76号走失记.txt _[31.47KB]_
- [1950]《我，机器人》(I, Robot).txt _[387.24KB]_
- [1955]《永恒的终结》.pdf _[1.29MB]_
- [1972]《神们自己》(The Gods Themselves).txt _[543.86KB]_
- 一只下金蛋的鹅.txt _[10.33KB]_
- 不朽的诗人.txt _[5.12KB]_
- 九个明天.txt _[452.51KB]_
- 二百岁的寿星.txt _[82.15KB]_
- 人语石.txt _[44.2KB]_
- 他们那时多有趣.txt _[5.12KB]_
- 低能儿收容所.txt _[141.63KB]_
- 假如.txt _[28.18KB]_
- 力量的感觉.txt _[24.11KB]_
- 台球.txt _[38.12KB]_
- 响铃.txt _[34.11KB]_
- 啊，巴顿，巴顿！.txt _[26.24KB]_
- 地球母亲.txt _[71.79KB]_
- 复仇女神.txt _[765.49KB]_
- 天堂里的陌生人.txt _[57.26KB]_
- 奇妙的航程.txt _[407.74KB]_
- 奇袭.txt _[66.27KB]_
- 如鱼得水.txt _[17.47KB]_
- 孩子最好的朋友.txt _[6.69KB]_
- 尼德林教授的试题.txt _[9.23KB]_
- 怪异的谋杀案.txt _[21.35KB]_
- 捉兔记.txt _[45.66KB]_
- 换个角度.txt _[6.99KB]_
- 日暮.txt _[45.06KB]_
- 星光.txt _[8.32KB]_
- 最后的问题.txt _[32.52KB]_
- 机器人的幻想.txt _[34.63KB]_
- 格洛里亚的好朋友.txt _[46.75KB]_
- 死尘.txt _[24.77KB]_
- 法律之争.txt _[2.9KB]_
- 火星方式.txt _[94.28KB]_
- 灶神星畔受困记.txt _[35.18KB]_
- 真爱.txt _[8.74KB]_
- 眼睛不仅用来看东西.txt _[6.77KB]_
- 确定无疑的事.txt _[2.97KB]_
- 神奇的汽车——萨莉.txt _[43.08KB]_
- 第一定律.txt _[6.64KB]_
- 终极答案.txt _[14.83KB]_
- 被遗忘的世界.txt _[21.55KB]_
- 讣告.txt _[35.32KB]_
- 讲笑话的人.txt _[32.51KB]_
- 谁是凶手.txt _[16.34KB]_
- 钥匙.txt _[69.48KB]_
- 镜象.txt _[29.54KB]_
- 鬼扯.txt _[9.04KB]_
- 黑鳏夫酒家的聚会.txt _[33.14KB]_
### 004 - Jules Gabriel Verne(儒勒·加布里埃尔·凡尔纳)
- 01-三部曲
  - [1868]《格兰特船长的儿女》.txt _[969.54KB]_
  - [1870]《海底两万里》(Vingt mille lieues sous les mers).txt _[736.53KB]_
  - [1875]《神秘岛》.txt _[970.76KB]_
- 02-大炮俱乐部三部曲
  - [1865]《从地球到月球》(De la Terre à la Lune).txt _[276.46KB]_
  - [1870]《环绕月球》.txt _[329.72KB]_
  - [1889]《北冰洋的幻想》(又名'扭转乾坤').txt _[229.36KB]_
- 0-凡尔纳汇总.md _[2.74KB]_
- [1863]《气球上的五星期》.txt _[534.81KB]_
- [1864]《地心游记》.txt _[344.58KB]_
- [1866]《哈特拉斯船长历险记》.txt _[726.1KB]_
- [1873]《八十天环游地球》.txt _[423.6KB]_
- [1877]《太阳系历险记》.txt _[611.96KB]_
- [1882]《鲁滨逊学校》.txt _[310.38KB]_
- [1888]《两年假期》.txt _[494.06KB]_
- [1888]《绿光》.txt _[268.61KB]_
- [1891]《2889年一个美国新闻界巨子的一天》.txt _[29.58KB]_
- [1891]《金火山》.txt _[631.72KB]_
- [1892]《冰岛怪兽》.txt _[693.12KB]_
- [1892]《喀尔巴阡古堡》.txt _[255.93KB]_
- [1894]《昂梯菲尔奇遇记》.txt _[542.58KB]_
- [1895]《机器岛》.txt _[681.64KB]_
- [1899]《大木筏》.txt _[501.71KB]_
- [1899]《大木筏》上册.epub _[197.58KB]_
- [1905]《大海入侵》.txt _[306.89KB]_
- [1908]《多瑙河领航员》.txt _[407.26KB]_
### 005 - Mary Shelley(玛丽·雪莱)
- [1818]《弗兰肯斯坦》(Frankenstein).txt _[438.82KB]_
### 006 - Ray Douglas Bradbury(雷·道格拉斯·布拉德伯里)
- [----]《城市》.txt _[14.98KB]_
- [----]《太阳的故事》.txt _[10.72KB]_
- [----]《弄巧成拙》.txt _[19.23KB]_
- [----]《时光机》.txt _[17.68KB]_
- [----]《时间狩猎》.txt _[25.62KB]_
- [----]《杀“妻”》.txt _[12.03KB]_
- [----]《浓雾号角》.txt _[14.82KB]_
- [----]《湖》.txt _[13.22KB]_
- [----]《火星人》.txt _[23.83KB]_
- [----]《火气球》.txt _[39.9KB]_
- [----]《火箭飞行员》.txt _[22.55KB]_
- [----]《百万年野餐》.txt _[21.65KB]_
- [----]《细雨即将来临》.txt _[14.7KB]_
- [----]《苍白先生》.txt _[12.42KB]_
- [----]《雨一直下》.txt _[28.61KB]_
- [----]《马里奥纳特公司的机器人》.txt _[15.48KB]_
- [1946]《冰霜与烈火》.txt _[90.63KB]_
- [1950]《2002年8月夜遇》.txt _[16.32KB]_
- [1950]《火星纪事》.epub _[260.25KB]_
- [1951]《图案人》.epub _[323.68KB]_
- [1953]《华氏451度》.txt _[72.18KB]_
### 007 - Orson Scott Card(奥森·斯科特·卡德)
- 0-卡德汇总.md _[4.21KB]_
- [1985]《安德的游戏》.txt _[608.86KB]_
- [1986]《死者代言人》.epub _[387.26KB]_
- [1986]《死者代言人》.txt _[765.89KB]_
- [1991]《外星屠异》.epub _[538.25KB]_
- [1999]《安德的影子》(Ender's Shadow).txt _[819.16KB]_
- [2001]《霸主的影子》(Shadow of the Hegemon).txt _[666.21KB]_
### 008 - Ted Chiang(特德·姜)
- 0-特德姜汇总.md _[3.13KB]_
- [1990]《巴比伦塔》.txt _[43.94KB]_
- [1998]《你一生的故事》.txt _[115.38KB]_
- [2000]《七十二个字母》.txt _[99.31KB]_
- [2001]《地狱是上帝不在的地方》(Hell Is the Absence of God).txt _[66.91KB]_
- [2007]《商人和炼金术士之门》(The Merchant and the Alchemist's Gate).txt _[60.77KB]_
- [2008]《呼吸》(Exhalation).txt _[33.0KB]_
- [2010]《软件体的生命周期》(The Lifecycle of Software Objects).txt _[191.49KB]_
### 009 - Michael Swanwick (迈克尔·斯万维克) 
- [1999]《不朽的机器》(Ancient Engines).txt _[19.33KB]_
- [1999]《暴龙谐谑曲》(Scherzo with Tyrannosaur).txt _[31.89KB]_
- [2001]《狗说汪汪》(The Dog Said Bow-Wow).txt _[39.09KB]_
- [2002]《缓慢的生命》(Slow Life).txt _[46.13KB]_
- [2003]《时空军团》(Legions in Time).txt _[54.01KB]_
### 010 - 王晋康
- [1993]《亚当回归》.txt _[28.11KB]_
- [1994]《天火》.txt _[29.32KB]_
- [1994]《魔鬼梦幻》.txt _[32.28KB]_
- [1994]《黑匣子里的爱情》.txt _[17.38KB]_
- [1995]《星期日病毒》.txt _[20.49KB]_
- [1995]《生命之歌》.txt _[50.01KB]_
- [1995]《追杀》.txt _[62.1KB]_
- [1996]《天河相会》.txt _[55.52KB]_
- [1996]《斯芬克司之谜》.txt _[85.83KB]_
- [1996]《西奈噩梦》.txt _[37.66KB]_
- [1997]《七重外壳》.txt _[62.12KB]_
- [1997]《三色世界》.txt _[95.23KB]_
- [1997]《拉格朗日坟场》.txt _[78.88KB]_
- [1997]《生死平衡》.txt _[179.81KB]_
- [1998]《太空雕像》.txt _[50.33KB]_
- [1998]《豹》.txt _[142.68KB]_
- [1998]《魔环》.txt _[50.51KB]_
- [1999]《可爱的机器犬》.txt _[19.18KB]_
- [1999]《失去它的日子》.txt _[43.52KB]_
- [1999]《解读生命》.txt _[51.06KB]_
- [2001]《替天行道》.txt _[72.1KB]_
- [2002]《新安魂曲》.txt _[92.94KB]_
- [2003]《时空商人》.txt _[21.98KB]_
- [2005]《一生的故事》.txt _[97.76KB]_
- [2006]《我们向何处去》.txt _[25.14KB]_
- [2006]《终极爆炸》.txt _[217.25KB]_
- [2008]《决战美杜莎》.txt _[46.79KB]_
### 011 - Andy Weir(安迪·威尔)
- [2021]《挽救计划》.epub _[676.92KB]_
### 012 - Arthur Charles Clarke(亚瑟·查理斯·克拉克)
- 0-亚瑟·克拉克汇总.md _[2.14KB]_
- [1951]《太空序曲》.txt _[294.38KB]_


## Star History

[![Star History Chart](https://star-history.dera.page/svg?repos=VeejaLiu/ScienceFictionCollection&type=Date)](https://star-history.dera.page/#VeejaLiu/ScienceFictionCollection&Date)
