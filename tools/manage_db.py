import hashlib
from threading import Lock
import csv

lock = Lock()
# 盐
SALT = b'%k857'


# 密码hash加密
def md5_passwd(passwd):
    hash = hashlib.md5(SALT)
    hash.update(passwd.encode())
    return hash.hexdigest()


class GetCSV:
    def __init__(self):
        pass

    # 读取csv文件 order_daily_bt_dh.csv -- 订单表贷后
    def order_daily_bt_dh(self):
        with open('./csvfiles/for_monitor/order_daily_bt_dh.csv', 'r', encoding='utf_8_sig') as f:
            reader = csv.reader(f)
            rows = [item for item in reader]
            return rows[1:]

    # 读取csv文件 order_daily_bt_dh.csv -- 订单表贷后 pie图，只要后两项
    def order_daily_bt_dh_pie(self):
        with open('./csvfiles/for_monitor/order_daily_bt_dh.csv', 'r', encoding='utf_8_sig') as f:
            reader = csv.reader(f)
            rows = [item[-2:] for item in reader]
            return rows[1:]

    # 读取csv文件 order_daily_bt_dq.csv -- 订单表贷前
    def order_daily_bt_dq(self):
        with open('./csvfiles/for_monitor/order_daily_bt_dq.csv', 'r', encoding='utf_8_sig') as f:
            reader = csv.reader(f)
            rows = [item for item in reader]
            return rows[1:]

    # 读取csv文件 order_daily_bt_dq.csv -- 订单表贷前 pie图，只要后两项
    def order_daily_bt_dq_pie(self):
        with open('./csvfiles/for_monitor/order_daily_bt_dq.csv', 'r', encoding='utf_8_sig') as f:
            reader = csv.reader(f)
            rows = [item[-2:] for item in reader]
            return rows[1:]

    # 读取csv文件 order_daily_txt.csv -- 订单表数据
    def order_daily_txt(self):
        with open('./csvfiles/for_monitor/order_daily_txt.csv', 'r', encoding='utf_8_sig') as f:
            reader = csv.reader(f)
            rows = [item for item in reader]
            return rows[1:]

    # 读取csv文件 zx_daily_txt.csv -- 征信表数据
    def zx_daily_txt(self):
        with open('./csvfiles/for_monitor/zx_daily_txt.csv', 'r', encoding='utf_8_sig') as f:
            reader = csv.reader(f)
            rows = [item for item in reader]
            return rows[1:]

    def get_order_start_end(self):
        with open('./csvfiles/for_monitor/order_daily_txt.csv', 'r', encoding='utf_8_sig') as f:
            reader = csv.reader(f)
            rows = [item for item in reader]
            return (rows[1][0], rows[-1][0])

    def get_zx_start_end(self):
        with open('./csvfiles/for_monitor/zx_daily_txt.csv', 'r', encoding='utf_8_sig') as f:
            reader = csv.reader(f)
            rows = [item for item in reader]
            return (rows[1][0], rows[-1][0])

    def get_zb_data(self):
        with open('./csvfiles/for_monitor/zb_daily_txt.csv', 'r', encoding='utf_8_sig') as f:
            reader = csv.reader(f)
            rows = [item for item in reader]
            return rows[1:]

    def get_test_data(self):
        with open('C:/Users/vzoom/Desktop/test_0817.csv', 'r', encoding='utf_8_sig') as f:
            reader = csv.reader(f)
            rows = [item for item in reader]
            return rows[1:]

    def get_order_count(self):
        with open('./csvfiles/for_monitor/order_count.csv', 'r', encoding='utf_8_sig') as f:
            reader = csv.reader(f)
            rows = [item for item in reader]
            return rows[1:]


if __name__ == '__main__':
    db_ = GetCSV()
    print(db_.get_order_count())
