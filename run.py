import json
from flask import Flask, render_template, request, redirect, url_for, session
import os
from tools.manage_db import GetCSV, md5_passwd
from tools.charts import Chart
from tools.itreable_tools import ComplexEncoder
from settings import *

app = Flask(__name__)
app.config['BASE_DIR'] = os.path.dirname(__file__)
app.config['SECRET_KEY'] = 'loki123456798'


# 登录
@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        account = request.form.get('account')
        password = request.form.get('password')
        password = md5_passwd(password)
        if account in USERS.keys():
            user = USERS[account]
            if password == user['password']:
                id = user['id']
                try:
                    session['account'] = account
                    session['id'] = id
                except Exception as e:
                    print(e)
                    return render_template('login.html')

                ret = {'status': True, 'message': ''}
                return json.dumps(ret)
                # return redirect(url_for('index'))
            else:
                ret = {'status': False, 'message': '用户名或密码错误'}
                return json.dumps(ret)


# 主页面
@app.route('/index', methods=['GET'])
def index():
    id = session.get('id')
    if id:
        username = session.get('account')
        query = GetCSV()
        ddb_date = query.get_order_start_end()
        ddb_startdate = ddb_date[0]
        ddb_enddate = ddb_date[1]
        ddb_count = query.get_order_count()
        ddb_bm = 'vz_order_info'
        ddb_qys = ddb_count[0][0]
        ddb_sql = ddb_count[0][1]
        ddb_dhl = ddb_count[0][2]
        title1 = TITLE_ORDER_TXT
        title2 = TITLE_ORDER_DQ
        title3 = TITLE_ORDER_DH
        title4 = TITLE_ZX_TXT
        title5 = TITLE_ZB_TXT1
        title6 = TITLE_ZB_TXT2
        title7 = TITLE_ZB_TXT3
        title8 = TITLE_ZB_TXT4
        title9 = TITLE_ZB_TXT5
        title10 = TITLE_ZB_TXT6
        title11 = TITLE_ZB_TXT7
        title12 = TITLE_ZB_TXT8
        title13 = TITLE_ZB_TXT9
        title14 = TITLE_ZB_TXT10
        title15 = TITLE_ZB_TXT11
        title16 = TITLE_ZB_TXT12
        title17 = TITLE_ZB_TXT13
        title18 = TITLE_ZB_TXT14

        swb_date = query.get_zx_start_end()
        swb_startdate = swb_date[0]
        swb_enddate = swb_date[1]
        return render_template('index.html', params=locals())
    else:
        return redirect(url_for('login'))


# 登出
@app.route('/logout')
def logout():
    # 清除session数据
    session.clear()
    return redirect(url_for('login'))


# bar图
@app.route('/get_bar1_ddb')
def get_bar1_ddb():
    query = GetCSV()
    obj = query.order_daily_txt()
    chrt = Chart()
    c = chrt.bar_base(obj)
    return c.dump_options_with_quotes()


# 表格
@app.route('/get_table1_ddb')
def get_table1_ddb():
    query = GetCSV()
    obj = query.order_daily_bt_dq()
    str_con = json.dumps(obj, cls=ComplexEncoder)
    return str_con


# 表格1配套Pie图
@app.route('/get_pie1_ddb')
def get_pie1_ddb():
    query = GetCSV()
    obj = query.order_daily_bt_dq_pie()
    chrt = Chart()
    c = chrt.pie_base1(obj)
    return c.dump_options_with_quotes()


# 表格2
@app.route('/get_table2_ddb')
def get_table2_ddb():
    query = GetCSV()
    obj = query.order_daily_bt_dh()
    str_con = json.dumps(obj, cls=ComplexEncoder)
    return str_con


# 表格2配套Pie图
@app.route('/get_pie2_ddb')
def get_pie2_ddb():
    query = GetCSV()
    obj = query.order_daily_bt_dh_pie()
    chrt = Chart()
    c = chrt.pie_base1(obj)
    return c.dump_options_with_quotes()


# 税务表 表格
@app.route('/get_table1_swb')
def get_table1_swb():
    query = GetCSV()
    obj = query.zx_daily_txt()
    str_con = json.dumps(obj, cls=ComplexEncoder)
    return str_con


# 税务表 图表
@app.route('/get_line1_swb')
def get_line1_swb():
    query = GetCSV()
    obj = query.zx_daily_txt()
    chrt = Chart()
    c = chrt.line_base(obj)
    return c.dump_options_with_quotes()


# 指标-经营年限 图表
@app.route('/get_chart1_zbb')
def get_chart1_zbb():
    query = GetCSV()
    obj = query.get_zb_data()
    chrt = Chart()
    c = chrt.get_chart1_zzb(obj)
    return c.dump_options_with_quotes()


# 指标-近12个月法人变更次数 图表
@app.route('/get_chart2_zbb')
def get_chart2_zbb():
    query = GetCSV()
    obj = query.get_zb_data()
    chrt = Chart()
    c = chrt.get_chart2_zzb(obj)
    return c.dump_options_with_quotes()


# 指标-投资比例 图表
@app.route('/get_chart3_zbb')
def get_chart3_zbb():
    query = GetCSV()
    obj = query.get_zb_data()
    chrt = Chart()
    c = chrt.get_chart3_zzb(obj)
    return c.dump_options_with_quotes()


# 指标-年龄 图表
@app.route('/get_chart4_zbb')
def get_chart4_zbb():
    query = GetCSV()
    obj = query.get_zb_data()
    chrt = Chart()
    c = chrt.get_chart4_zzb(obj)
    return c.dump_options_with_quotes()


# 指标-全部销售额 图表
@app.route('/get_chart5_zbb')
def get_chart5_zbb():
    query = GetCSV()
    obj = query.get_zb_data()
    chrt = Chart()
    c = chrt.get_chart5_zzb(obj)
    return c.dump_options_with_quotes()


# 指标-税负率 图表
@app.route('/get_chart6_zbb')
def get_chart6_zbb():
    query = GetCSV()
    obj = query.get_zb_data()
    chrt = Chart()
    c = chrt.get_chart6_zzb(obj)
    return c.dump_options_with_quotes()


# 指标-行为罚款次数 图表
@app.route('/get_chart7_zbb')
def get_chart7_zbb():
    query = GetCSV()
    obj = query.get_zb_data()
    chrt = Chart()
    c = chrt.get_chart7_zzb(obj)
    return c.dump_options_with_quotes()


# 指标-滞纳金次数 图表
@app.route('/get_chart8_zbb')
def get_chart8_zbb():
    query = GetCSV()
    obj = query.get_zb_data()
    chrt = Chart()
    c = chrt.get_chart8_zzb(obj)
    return c.dump_options_with_quotes()


# 指标-净利润 图表
@app.route('/get_chart9_zbb')
def get_chart9_zbb():
    query = GetCSV()
    obj = query.get_zb_data()
    chrt = Chart()
    c = chrt.get_chart9_zzb(obj)
    return c.dump_options_with_quotes()


# 指标-营业收入 图表
@app.route('/get_chart10_zbb')
def get_chart10_zbb():
    query = GetCSV()
    obj = query.get_zb_data()
    chrt = Chart()
    c = chrt.get_chart10_zzb(obj)
    return c.dump_options_with_quotes()


# 指标-负债合计 图表
@app.route('/get_chart11_zbb')
def get_chart11_zbb():
    query = GetCSV()
    obj = query.get_zb_data()
    chrt = Chart()
    c = chrt.get_chart11_zzb(obj)
    return c.dump_options_with_quotes()


# 指标-下游总额 图表
@app.route('/get_chart12_zbb')
def get_chart12_zbb():
    query = GetCSV()
    obj = query.get_zb_data()
    chrt = Chart()
    c = chrt.get_chart12_zzb(obj)
    return c.dump_options_with_quotes()


# 指标-违法违章次数 图表
@app.route('/get_chart13_zbb')
def get_chart13_zbb():
    query = GetCSV()
    obj = query.get_zb_data()
    chrt = Chart()
    c = chrt.get_chart13_zzb(obj)
    return c.dump_options_with_quotes()


# 指标-稽查案件次数 图表
@app.route('/get_chart14_zbb')
def get_chart14_zbb():
    query = GetCSV()
    obj = query.get_zb_data()
    chrt = Chart()
    c = chrt.get_chart14_zzb(obj)
    return c.dump_options_with_quotes()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
