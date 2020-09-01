# Python+Docker+Flask+pyecharts实现数据可视化  

实施该项目是为了实现组内日常对生产环境数据的监控，由于生产环境使用了堡垒机环境隔离，与本地通讯只有邮件通讯一个出口，实施难度在于数据流转及监控指标处理，数据流程说明图：  
![image](https://pic4.zhimg.com/v2-21a47adcf852ad6084fef306b626a42a_r.jpg)  


## 堡垒机端  
### 1、数据监控指标加工  
数据的加工使用HSQL编写为存储过程，在服务器使用crontab定时任务，每天定时使用beeline连接大数据平台调用存储过程实现  
  
### 2、数据提取及发送  
monitor_csv_zip.py：pyodbc库连接hive -> csv库数据存为csv -> zipfile库压缩文件 -> paramiko库上传文件到服务器  
sendEmail.py：email库编写邮件信息及构建附件 -> sendmail库发送邮件(centos已建立mail服务)  
  
## 本地端  
run.py：主脚本，Flask实现代码  
settings.py：各图标标题  
tools/charts.py：图表pyecharts配置  
tools/itreable_tools.py：对页面表格涉及时间格式的做处理  
tools/manage_db.py：读取csv文件  
templates/index.html：图表html配置  
templates/login.html：登录页面html配置  
static/css/index.css：图表css配置，字体位置等  
static/css/login.css：登录页css配置  
static/css/bg_img.jpg：登录页背景图片  
static/js/echarts.min.js：依赖配置，pyecharts官网可下，也可以通过网址配置，本地配置可以实现没有网络页面正常显示  
static/js/jquery.min.js：依赖配置，pyecharts官网可下，也可以通过网址配置，本地配置可以实现没有网络页面正常显示  
csvfiles/formonitor/read_email.py：接收邮件并查收附件，解压为本地文件，使用zmail包，该表仅支持几个主流邮箱，但是使用简单  

## Docker部分  
Dokcer在服务器直接配置，不涉及代码文件，在本地端的python及邮箱接收均使用容器实现，步骤可以看下面连接：  
> https://www.cnblogs.com/rango-lhl/p/13468887.html

