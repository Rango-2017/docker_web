"""
for_monitor_zip_ftp.py
数据质量监控，将表内容存为csv，打包成zip并上传到服务器
"""
import zipfile
import pyodbc
import csv
import paramiko
import datetime
import os

# SQL
SQL1 = "select type, remark, num from data_monitor.order_daily_bt_dh"
SQL2 = "select type, remark, num from data_monitor.order_daily_bt_dq"
SQL3 = "select apply_time, num, avg_num from data_monitor.order_daily_txt order by apply_time"
SQL4 = "select lrsj, jcxx, lxrxx, tzfxx, sbxx, sbzsxx, zcfzbxx, lrbxx, jydx, wfwzxx, bgdjxx, jcajxx " \
       "from data_monitor.zx_daily_txt order by lrsj"

# 各表字段
HEADERS1 = ['type', 'remark', 'num']
HEADERS2 = ['type', 'remark', 'num']
HEADERS3 = ['apply_time', 'num', 'avg_num']
HEADERS4 = ['lrsj', 'jcxx', 'lxrxx', 'tzfxx', 'sbxx', 'sbzsxx', 'zcfzbxx', 'lrbxx', 'jydx', 'wfwzxx', 'bgdjxx',
            'jcajxx']

# 文件路径及文件名
CSV_FILE_PATH = r"C:/Users/wuxy/Desktop/for_monitor"
ZIP_FILE_PATH = r"C:/Users/wuxy/Desktop"
REMOTE_PATH = r"/root/for_monitor"
FILE1 = "order_daily_bt_dh.csv"
FILE2 = "order_daily_bt_dq.csv"
FILE3 = "order_daily_txt.csv"
FILE4 = "zx_daily_txt.csv"
FILE5 = "for_monitor.zip"

# 服务器相关
HOST = '192.168.110.211'
USERNAME = 'root'
PASSWORD = 'k1k2k3&*('
PORT = 22


# 连接服务器
def connect_server():
    cnxn = pyodbc.connect('DSN=inceptor')
    cursor = cnxn.cursor()
    return cursor


# 查询数据，将数据写入csv
def query_to_csv(cursor, sql, headers, filename):
    cursor.execute(sql)
    res = cursor.fetchall()
    rows = [list(item) for item in res]
    with open(CSV_FILE_PATH + '/' + filename, 'w', encoding='utf_8_sig', newline='') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(rows)


# 打包成zip文件
def make_zip():
    zipf = zipfile.ZipFile(ZIP_FILE_PATH + '/' + FILE5, 'w')
    pre_len = len(os.path.dirname(CSV_FILE_PATH))
    for parent, dirnames, filenames in os.walk(CSV_FILE_PATH):
        for filename in filenames:
            pathfile = os.path.join(parent, filename)
            arcname = pathfile[pre_len:].strip(os.path.sep)
            zipf.write(pathfile, arcname)
    zipf.close()


# 将文件传到服务器
def upload():
    local_file = ZIP_FILE_PATH + '/' + FILE5
    remote_path = REMOTE_PATH + '/' + FILE5
    t = paramiko.Transport((HOST, PORT))
    t.connect(username=USERNAME, password=PASSWORD)
    sftp = paramiko.SFTPClient.from_transport(t)
    print('开始上传文件...%s' % datetime.datetime.now())

    try:
        sftp.put(local_file, remote_path)
    except Exception as e:
        sftp.mkdir(os.path.split(remote_path)[0])
        sftp.put(local_file, remote_path)
    finally:
        print('文件上传成功...%s' % datetime.datetime.now())

    t.close()


def record(flag, msg):
    try:
        with open("C:/Users/wuxy/Desktop/monitor_record.txt", 'a+') as f:
            if flag == 1:
                f.write('文件上传成功...%s' % datetime.datetime.now() + '\r\n')
            elif flag == 0:
                f.write('文件上传失败...%s' % datetime.datetime.now() + '...' + repr(msg) + '\r\n')
    except Exception as e:
        with open("C:/Users/wuxy/Desktop/monitor_record.txt", 'w') as f:
            if flag == 1:
                f.write('文件上传成功...%s' % datetime.datetime.now() + '\r\n')
            elif flag == 0:
                f.write('文件上传失败...%s' % datetime.datetime.now() + '...' + repr(msg) + '\r\n')


if __name__ == '__main__':
    try:
        # 链接数据库
        cursor = connect_server()
        # 读取数据，转成csv文件
        query_to_csv(cursor, SQL1, HEADERS1, FILE1)
        query_to_csv(cursor, SQL2, HEADERS2, FILE2)
        query_to_csv(cursor, SQL3, HEADERS3, FILE3)
        query_to_csv(cursor, SQL4, HEADERS4, FILE4)
        # 打包成csv
        make_zip()
        # 上传至服务器
        upload()
        record(1, '')
    except Exception as e:
        print(repr(e))
        record(0, e)
