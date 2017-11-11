from pyecharts.chart import Chart
from pyecharts.option import get_all_options
import pStat

class myBar(Chart):
    def __init__(self, title, subtitle='', **kwargs):
        super(myBar, self).__init__(title , subtitle, **kwargs)

    def add(self, *args, **kwargs):
        self.__add(*args, **kwargs)

    def addData(self, serisesName, data,
                is_stack=False,
                bar_category_gap="20%",**kwargs):
        chart = get_all_options(**kwargs)
        is_stack = "stack_" + str(self._option['series_id']) if is_stack else ""
        self._option.get('legend')[0].get('data').append(serisesName)
        self._option.get('series').append({
            "type": "bar",
            "name": serisesName,
            "data": data,
            "stack": is_stack,
            "barCategoryGap": bar_category_gap,
            "label": chart['label'],
            "markPoint": chart['mark_point'],
            "markLine": chart['mark_line'],
            "seriesId": self._option.get('series_id'),
        })


    def __add(self, x_axis, **kwargs):
        kwargs.update(x_axis=x_axis)
        chart = get_all_options(**kwargs)

        xaxis, yaxis = chart['xy_axis']
        self._option.update(xAxis=xaxis, yAxis=yaxis)

        self._config_components(**kwargs)




class myLine(Chart):
    def __init__(self, title, subtitle = '',**kwargs):
        super(myLine, self).__init__(title , subtitle, **kwargs)

    def add(self, *args, **kwargs):
        self.__add(*args, **kwargs)

    def addData(self, serisesName, data,
              is_symbol_show=True,
              is_smooth=False,
              is_stack=False,
              is_step=False,
              is_fill=False,**kwargs):
        chart = get_all_options(**kwargs)
        is_stack = "stack_" + str(self._option['series_id']) if is_stack else ""
        _area_style = {"normal": chart['area_style']} if is_fill else {}
        self._option.get('legend')[0].get('data').append(serisesName)
        self._option.get('series').append({
            "type": "line",
            "name": serisesName,
            "symbol": chart['symbol'],
            "smooth": is_smooth,
            "step": is_step,
            "stack": is_stack,
            "showSymbol": is_symbol_show,
            "data": data,
            "label": chart['label'],
            "lineStyle": chart['line_style'],
            "areaStyle": _area_style,
            "markPoint": chart['mark_point'],
            "markLine": chart['mark_line'],
            "seriesId": self._option.get('series_id'),
        })
        self._config_components(**kwargs)

    def __add(self, x_axis, **kwargs):
        kwargs.update(x_axis=x_axis, type="line")
        chart = get_all_options(**kwargs)

        xaxis, yaxis = chart['xy_axis']
        self._option.update(xAxis=xaxis, yAxis=yaxis)

        self._config_components(**kwargs)

class myPie(Chart):
    """
    <<< 饼图 >>>
    饼图主要用于表现不同类目的数据在总和中的占比。每个的弧度表示数据数量的比例。
    """
    def __init__(self, title, subtitle="", **kwargs):
        super(myPie, self).__init__(title, subtitle, **kwargs)

    def add(self, *args, **kwargs):
        self.__add(*args, **kwargs)


    def addData(self, serisesName, value,
              radius=None,
              center=None,
              rosetype=None,
              **kwargs):
        kwargs.update(type="pie")
        chart = get_all_options(**kwargs)
        assert len(self._attr) == len(value)
        _data = []
        for data in zip(self._attr, value):
            _name, _value = data
            _data.append({"name": _name, "value": _value})

        _rmin, _rmax = "0%", "75%"
        if radius:
            if len(radius) == 2:
                _rmin, _rmax = ["{}%".format(r) for r in radius]

        _cmin, _cmax = "50%", "50%"
        if center:
            if len(center) == 2:
                _cmin, _cmax = ["{}%".format(c) for c in center]

        if rosetype:
            if rosetype not in ("radius", "area"):
                rosetype = "radius"

        self._option.get('series').append({
            "type": "pie",
            "name": serisesName,
            "data": _data,
            "radius": [_rmin, _rmax],
            "center": [_cmin, _cmax],
            "roseType": rosetype,
            "label": chart['label'],
            "seriesId": self._option.get('series_id'),
        })

    def __add(self, attr, **kwargs):
        """
        :param name:
            系列名称，用于 tooltip 的显示，legend 的图例筛选。
        :param attr:
            属性名称。
        :param value:
            属性所对应的值。
        :param radius:
            饼图的半径，数组的第一项是内半径，第二项是外半径，默认为 [0, 75]
            默认设置成百分比，相对于容器高宽中较小的一项的一半。
        :param center:
            饼图的中心（圆心）坐标，数组的第一项是横坐标，第二项是纵坐标，默认为 [50, 50]
            默认设置成百分比，设置成百分比时第一项是相对于容器宽度，第二项是相对于容器高度。
        :param rosetype:
           是否展示成南丁格尔图，通过半径区分数据大小，有'radius'和'area'两种模式。
           默认为'radius'
                radius：扇区圆心角展现数据的百分比，半径展现数据的大小。
                area：所有扇区圆心角相同，仅通过半径展现数据大小。
        :param kwargs:
        """
        kwargs.update(type="pie")
        self._attr = attr

        for a in attr:
            self._option.get('legend')[0].get('data').append(a)

        _dlst = self._option.get('legend')[0].get('data')
        _dset = list(set(_dlst))
        _dset.sort(key=_dlst.index)
        self._option.get('legend')[0].update(data=list(_dset))

        self._config_components(**kwargs)

class mychart(object):
    def __init__(self, cType , title , attr , category_name):
        self._cType = cType
        self._title = title
        self._attr = attr
        self._category_name = category_name
        self.chartBulid()

    @property
    def chart(self):
        return self._chart

    def chartBulid(self):
        if self._cType == 'Bar':
            self._chart = myBar(self._title)
            self._chart.add(self._attr, xaxis_name=self._category_name)
        elif self._cType == 'Line':
            self._chart = myLine(self._title)
            self._chart.add(self._attr, xaxis_name=self._category_name)
        elif self._cType == 'Rank':
            self._chart = myBar(self._title)
            self._chart.add(self._attr,is_convert=True)
        elif self._cType == 'Pie':
            self._chart = myPie(self._title)
            self._chart.add(self._attr)

    def dataChange(self , data:dict):
        gvd = { 'series': []}
        for dkey, dvalue in data.items():
            value = pStat.dictIntValue(dvalue)
            if self._cType == 'Rank':
                value = pStat.dictSorted(value)
                ydata = pStat.dictKeysList(value)
                sdata = pStat.dictValueList(value)
                if len(value)>15:
                    ydata = ydata[-15:]
                    sdata = sdata[-15:]
                gvd.update({'yAxis': {'data':ydata}})
                gvd['series'].append({'name': dkey, 'data': sdata})
            elif self._cType == 'Pie':
                pieData = []
                for pkey, pvlaue in value.items():
                    pieData.append({"name": pkey, "value": pvlaue})
                gvd['series'].append({'name': dkey, 'data': pieData})
            else:
                gvd['series'].append({'name': dkey, 'data': pStat.dictValueList(value)})
        return gvd

    def addData(self, serisesName, value, **kwargs):
        self._chart.addData(serisesName, value, **kwargs)