from pyecharts.charts import Bar, Line, Pie
from pyecharts import options as opts


class Chart:
    # Bar图
    def bar_base(self, obj):
        b = (
            Bar()
                .add_xaxis([item[0] for item in obj])
                .add_yaxis('每日申请企业数', [item[1] for item in obj], category_gap="50%")
                .set_series_opts(label_opts=opts.LabelOpts(position='insidetop'))
        )
        l = (
            Line()
                .add_xaxis([item[0] for item in obj])
                .add_yaxis('过去一个月平均值', [item[2] for item in obj])
                .set_global_opts(title_opts=opts.TitleOpts(title="过去一个月平均申请企业数"))
        )
        res = b.overlap(l)
        return res

    def pie_base1(self, obj):
        p = (
            Pie()
                .add("",
                     [list(item) for item in obj],
                     radius=["40%", "55%"],
                     label_opts=opts.LabelOpts(
                         formatter="{b}: {c}  {d}%",
                     )
                     )
        )
        return p

    def line_base(self, obj):
        l = (
            Line()
                .add_xaxis([item[0] for item in obj])
                .add_yaxis('jcxx', [item[1] for item in obj], label_opts=opts.LabelOpts(is_show=False),
                           linestyle_opts=opts.LineStyleOpts(width=2))
                .add_yaxis('lxrxx', [item[2] for item in obj], label_opts=opts.LabelOpts(is_show=False),
                           linestyle_opts=opts.LineStyleOpts(width=2))
                .add_yaxis('tzfxx', [item[3] for item in obj], label_opts=opts.LabelOpts(is_show=False),
                           linestyle_opts=opts.LineStyleOpts(width=2))
                .add_yaxis('sbxx', [item[4] for item in obj], label_opts=opts.LabelOpts(is_show=False),
                           linestyle_opts=opts.LineStyleOpts(width=2))
                .add_yaxis('sbzsxx', [item[5] for item in obj], label_opts=opts.LabelOpts(is_show=False),
                           linestyle_opts=opts.LineStyleOpts(width=2))
                .add_yaxis('zcfzbxx', [item[6] for item in obj], label_opts=opts.LabelOpts(is_show=False),
                           linestyle_opts=opts.LineStyleOpts(width=2))
                .add_yaxis('lrbxx', [item[7] for item in obj], label_opts=opts.LabelOpts(is_show=False),
                           linestyle_opts=opts.LineStyleOpts(width=2))
                .add_yaxis('jydx', [item[8] for item in obj], label_opts=opts.LabelOpts(is_show=False),
                           linestyle_opts=opts.LineStyleOpts(width=2))
                .add_yaxis('wfwzxx', [item[9] for item in obj], label_opts=opts.LabelOpts(is_show=False),
                           linestyle_opts=opts.LineStyleOpts(width=2))
                .add_yaxis('bgdjxx', [item[10] for item in obj], label_opts=opts.LabelOpts(is_show=False),
                           linestyle_opts=opts.LineStyleOpts(width=2))
                .add_yaxis('jcajxx', [item[11] for item in obj], label_opts=opts.LabelOpts(is_show=False),
                           linestyle_opts=opts.LineStyleOpts(width=2))
        )
        return l

    # jynx
    def get_chart1_zzb(self, obj):
        b = (
            Bar()
            .add_xaxis([item[0] for item in obj])
            .add_yaxis('<=2年', [item[1] for item in obj], stack='stack1', gap='0%')
            .add_yaxis('2~5年', [item[2] for item in obj], stack='stack1', gap='0%')
            .add_yaxis('5~10年', [item[3] for item in obj], stack='stack1', gap='0%')
            .add_yaxis('>10年', [item[4] for item in obj], stack='stack1', gap='0%')
            .add_yaxis('<=2年', [item[5] for item in obj], stack='stack2', gap='0%')
            .add_yaxis('2~5年', [item[6] for item in obj], stack='stack2', gap='0%')
            .add_yaxis('5~10年', [item[7] for item in obj], stack='stack2', gap='0%')
            .add_yaxis('>10年', [item[8] for item in obj], stack='stack2', gap='0%')
            .set_global_opts(xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=30)))
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        )
        return b

    # bgdj
    def get_chart2_zzb(self, obj):
        b = (
            Bar()
                .add_xaxis([item[0] for item in obj])
                .add_yaxis('1次', [item[9] for item in obj], stack='stack1', gap='0%')
                .add_yaxis('2次', [item[10] for item in obj], stack='stack1', gap='0%')
                .add_yaxis('>2次', [item[11] for item in obj], stack='stack1', gap='0%')
                .add_yaxis('1次', [item[12] for item in obj], stack='stack2', gap='0%')
                .add_yaxis('2次', [item[13] for item in obj], stack='stack2', gap='0%')
                .add_yaxis('>2次', [item[14] for item in obj], stack='stack2', gap='0%')
                .set_global_opts(xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=30)))
                .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        )
        return b

    # tzbl
    def get_chart3_zzb(self, obj):
        b = (
            Bar()
            .add_xaxis([item[0] for item in obj])
            .add_yaxis('<=80%', [item[81] for item in obj], stack='stack1', gap='0%')
            .add_yaxis('80%~100%', [item[82] for item in obj], stack='stack1', gap='0%')
            .add_yaxis('=100%', [item[83] for item in obj], stack='stack1', gap='0%')
            .add_yaxis('<=80%', [item[84] for item in obj], stack='stack2', gap='0%')
            .add_yaxis('80%~100%', [item[85] for item in obj], stack='stack2', gap='0%')
            .add_yaxis('=100%', [item[86] for item in obj], stack='stack2', gap='0%')
            .set_global_opts(xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=30)))
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        )
        return b

    # nl
    def get_chart4_zzb(self, obj):
        b = (
            Bar()
            .add_xaxis([item[0] for item in obj])
            .add_yaxis('<=50岁', [item[15] for item in obj], stack='stack1', gap='0%')
            .add_yaxis('30~40岁', [item[16] for item in obj], stack='stack1', gap='0%')
            .add_yaxis('40~50岁', [item[17] for item in obj], stack='stack1', gap='0%')
            .add_yaxis('>50岁', [item[18] for item in obj], stack='stack1', gap='0%')
            .add_yaxis('<=50岁', [item[19] for item in obj], stack='stack2', gap='0%')
            .add_yaxis('30~40岁', [item[20] for item in obj], stack='stack2', gap='0%')
            .add_yaxis('40~50岁', [item[21] for item in obj], stack='stack2', gap='0%')
            .add_yaxis('>50岁', [item[22] for item in obj], stack='stack2', gap='0%')
            .set_global_opts(xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=30)))
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        )
        return b

    # qbxse
    def get_chart5_zzb(self, obj):
        b = (
            Bar()
            .add_xaxis([item[0] for item in obj])
            .add_yaxis('<=5w', [item[23] for item in obj], stack='stack1', gap='0%')
            .add_yaxis('5~36w', [item[24] for item in obj], stack='stack1', gap='0%')
            .add_yaxis('36~120w', [item[25] for item in obj], stack='stack1', gap='0%')
            .add_yaxis('>120w', [item[26] for item in obj], stack='stack1', gap='0%')
            .add_yaxis('<=5w', [item[27] for item in obj], stack='stack2', gap='0%')
            .add_yaxis('5~36w', [item[28] for item in obj], stack='stack2', gap='0%')
            .add_yaxis('36~120w', [item[29] for item in obj], stack='stack2', gap='0%')
            .add_yaxis('>120w', [item[30] for item in obj], stack='stack2', gap='0%')
            .set_global_opts(xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=30)))
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        )
        return b

    # sfl
    def get_chart6_zzb(self, obj):
        b = (
            Bar()
            .add_xaxis([item[0] for item in obj])
            .add_yaxis('<=0', [item[31] for item in obj], stack='stack1', gap='0%')
            .add_yaxis('0~0.01', [item[32] for item in obj], stack='stack1', gap='0%')
            .add_yaxis('0.01~0.03', [item[33] for item in obj], stack='stack1', gap='0%')
            .add_yaxis('>0.03', [item[34] for item in obj], stack='stack1', gap='0%')
            .add_yaxis('<=0', [item[35] for item in obj], stack='stack2', gap='0%')
            .add_yaxis('0~0.01', [item[36] for item in obj], stack='stack2', gap='0%')
            .add_yaxis('0.01~0.03', [item[37] for item in obj], stack='stack2', gap='0%')
            .add_yaxis('>0.03', [item[38] for item in obj], stack='stack2', gap='0%')
            .set_global_opts(xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=30)))
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        )
        return b

    # xwfk
    def get_chart7_zzb(self, obj):
        b = (
            Bar()
            .add_xaxis([item[0] for item in obj])
            .add_yaxis('1次', [item[39] for item in obj], stack='stack1', gap='0%')
            .add_yaxis('2次', [item[40] for item in obj], stack='stack1', gap='0%')
            .add_yaxis('>2次', [item[41] for item in obj], stack='stack1', gap='0%')
            .add_yaxis('1次', [item[42] for item in obj], stack='stack2', gap='0%')
            .add_yaxis('2次', [item[43] for item in obj], stack='stack2', gap='0%')
            .add_yaxis('>2次', [item[44] for item in obj], stack='stack2', gap='0%')
            .set_global_opts(xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=30)))
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        )
        return b

    # znj
    def get_chart8_zzb(self, obj):
        b = (
            Bar()
            .add_xaxis([item[0] for item in obj])
            .add_yaxis('1次', [item[45] for item in obj], stack='stack1', gap='0%')
            .add_yaxis('2次', [item[46] for item in obj], stack='stack1', gap='0%')
            .add_yaxis('>2次', [item[47] for item in obj], stack='stack1', gap='0%')
            .add_yaxis('1次', [item[48] for item in obj], stack='stack2', gap='0%')
            .add_yaxis('2次', [item[49] for item in obj], stack='stack2', gap='0%')
            .add_yaxis('>2次', [item[50] for item in obj], stack='stack2', gap='0%')
            .set_global_opts(xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=30)))
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        )
        return b

    # jlr
    def get_chart9_zzb(self, obj):
        b = (
            Bar()
            .add_xaxis([item[0] for item in obj])
            .add_yaxis('<0', [item[51] for item in obj], stack='stack1', gap='0%')
            .add_yaxis('=0', [item[52] for item in obj], stack='stack1', gap='0%')
            .add_yaxis('>0', [item[53] for item in obj], stack='stack1', gap='0%')
            .add_yaxis('<0', [item[54] for item in obj], stack='stack2', gap='0%')
            .add_yaxis('=0', [item[55] for item in obj], stack='stack2', gap='0%')
            .add_yaxis('>0', [item[56] for item in obj], stack='stack2', gap='0%')
            .set_global_opts(xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=30)))
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        )
        return b

    # yysr
    def get_chart10_zzb(self, obj):
        b = (
            Bar()
            .add_xaxis([item[0] for item in obj])
            .add_yaxis('<=0', [item[57] for item in obj], stack='stack1', gap='0%')
            .add_yaxis('0~120w', [item[58] for item in obj], stack='stack1', gap='0%')
            .add_yaxis('>120w', [item[59] for item in obj], stack='stack1', gap='0%')
            .add_yaxis('<=0', [item[60] for item in obj], stack='stack2', gap='0%')
            .add_yaxis('0~120w', [item[61] for item in obj], stack='stack2', gap='0%')
            .add_yaxis('>120w', [item[62] for item in obj], stack='stack2', gap='0%')
            .set_global_opts(xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=30)))
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        )
        return b

    # fzhj
    def get_chart11_zzb(self, obj):
        b = (
            Bar()
            .add_xaxis([item[0] for item in obj])
            .add_yaxis('<=10w', [item[63] for item in obj], stack='stack1', gap='0%')
            .add_yaxis('10~100w', [item[64] for item in obj], stack='stack1', gap='0%')
            .add_yaxis('>100w', [item[65] for item in obj], stack='stack1', gap='0%')
            .add_yaxis('<=10w', [item[66] for item in obj], stack='stack2', gap='0%')
            .add_yaxis('10~100w', [item[67] for item in obj], stack='stack2', gap='0%')
            .add_yaxis('>100w', [item[68] for item in obj], stack='stack2', gap='0%')
            .set_global_opts(xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=30)))
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        )
        return b

    # xyze
    def get_chart12_zzb(self, obj):
        b = (
            Bar()
            .add_xaxis([item[0] for item in obj])
            .add_yaxis('<=36w', [item[69] for item in obj], stack='stack1', gap='0%')
            .add_yaxis('36~500w', [item[70] for item in obj], stack='stack1', gap='0%')
            .add_yaxis('>500w', [item[71] for item in obj], stack='stack1', gap='0%')
            .add_yaxis('<=36w', [item[72] for item in obj], stack='stack2', gap='0%')
            .add_yaxis('36~500w', [item[73] for item in obj], stack='stack2', gap='0%')
            .add_yaxis('>500w', [item[74] for item in obj], stack='stack2', gap='0%')
            .set_global_opts(xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=30)))
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        )
        return b

    # wfwz
    def get_chart13_zzb(self, obj):
        b = (
            Bar()
            .add_xaxis([item[0] for item in obj])
            .add_yaxis('1次', [item[75] for item in obj], stack='stack1', gap='0%')
            .add_yaxis('2次', [item[76] for item in obj], stack='stack1', gap='0%')
            .add_yaxis('>2次', [item[77] for item in obj], stack='stack1', gap='0%')
            .add_yaxis('1次', [item[78] for item in obj], stack='stack2', gap='0%')
            .add_yaxis('2次', [item[79] for item in obj], stack='stack2', gap='0%')
            .add_yaxis('>2次', [item[80] for item in obj], stack='stack2', gap='0%')
            .set_global_opts(xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=30)))
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        )
        return b

    # jcaj
    def get_chart14_zzb(self, obj):
        b = (
            Bar()
            .add_xaxis([item[0] for item in obj])
            .add_yaxis('1次', [item[87] for item in obj], stack='stack1', gap='0%')
            .add_yaxis('2次', [item[88] for item in obj], stack='stack1', gap='0%')
            .add_yaxis('>2次', [item[89] for item in obj], stack='stack1', gap='0%')
            .add_yaxis('1次', [item[90] for item in obj], stack='stack2', gap='0%')
            .add_yaxis('2次', [item[91] for item in obj], stack='stack2', gap='0%')
            .add_yaxis('>2次', [item[92] for item in obj], stack='stack2', gap='0%')
            .set_global_opts(xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=30)))
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        )
        return b
