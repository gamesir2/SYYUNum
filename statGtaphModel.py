# -*- coding: utf-8 -*-


'''
sdataType类属性解析（用于计算获取数据）:
    basedatas:原始数据名(str or list)
    dataname:创建的统计数据名(str)
    datatype:数据计算方式（str） ，默认为空
            当basedatas属性为list，该属性需填写
'''
class sdataType(object):
    def __init__(self , basedatas , dataname , datatype = None  ):
        self._basedatas = basedatas
        self._dataname = dataname
        self._datatype = datatype

    @property
    def basedatas( self ):
        return self._basedatas

    @property
    def dataname( self ):
        return self._dataname

    @property
    def datatype( self ):
        return self._datatype

'''
dataStatGraphProperty类属性解析（）:
    datadir：数据地址(str)
    stype：视图类型(str) (Bar:柱状图 Line:折线图 Pie:饼状图 Rank:排行榜)
    series：视图系列(str)
    category：视图类别(str)
    sdatatype：视图数据类型(sdataType or list（sdataType）)
'''
class dataStatGraphProperty(object):
    def __init__(self , datadir, stype , series , category , sdatatype):
        self._datadir = datadir
        self._stype = stype
        self._series = series
        self._category = category
        self._sdatatype = sdatatype

    @property
    def datadir( self ):
        return self._datadir

    @property
    def stype( self ):
        return self._stype

    @property
    def series( self ):
        return self._series

    @property
    def category( self ):
        return self._category

    @property
    def sdatatype( self ):
        return self._sdatatype


class dsgpGroup(object):
    def __init__(self , *dsgps , options = None ):
        self._dsgps = [dsgp for dsgp in dsgps]
        self._options = options

    @property
    def dsgps( self ):
        return self._dsgps

    @property
    def options( self ):
        return self._options

    def append(self , dsgp):
        self._dsgps.append(dsgp)