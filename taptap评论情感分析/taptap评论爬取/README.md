## TapTap爬虫的简要说明
 <br/>

### 运行环境
请在python环境下运行，这个程序的开发环境为python 3.7.1

 <br/>
 
### 	基本功能
这个程序根据你提供的游戏id，按评论最近更新时间，自动抓取每条完整的游戏评论和它的关联信息，存放到csv文件中。

 - **前置准备：** 如果你将csv文件的保存路径设置在C盘，最好手动建立路径，否则可能会出现premission dennied，抓取的数据保存不成功
 - **爬虫运行：** 最大抓取页数为990页，由于taptap的设置，单个游戏在990以后的评论数据无法访问。爬取过程中出错，重新运行程序，程序会自动在断点位置续爬

 - **爬虫结束：** 达到上限，程序报页面无法打开，数据已在csv文件中保存
 <br/>

它默认爬《元气骑士》（id：34751）这个游戏的评论，你也可以根据自己的需求自定义。可参考几个同类游戏的id：
|id| 游戏名 |
|--|--|
| 74838 | 贪婪洞窟2 |
| 77796 | 我的勇者 |
| 69792 | 异化之地 |

上面没有你想爬的游戏? 请看下一条
 <br/>

### 获取游戏id的方法——Fiddler抓包
&emsp;&emsp;Fiddler是一个http协议调试代理工具，简单来说，它充当中间人捕获你正在浏览的网页交换的数据流。它抓包app需要一些额外配置，可以参考[这篇文章](https://blog.csdn.net/xyz846/article/details/78963245)。

&emsp;&emsp;配置就绪后，做以下几步：
 - 使手机与Fiddler所在的电脑处于同一网络环境
 - 用手机进入TapTap的任一游戏的玩家评论区
 - 设置显示方式为最新
 - 下拉屏幕
 - 找到下面这条连接，得到游戏id
 <br/>
 
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200323110543653.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTE5MDkwNzc=,size_16,color_FFFFFF,t_70)
 <hr>

### 其他可能出现的问题
Fiddler配置的坑比较多，需要具体情况具体分析，可以留言联系。感谢阅读，Thanks for reading!
