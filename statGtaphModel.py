# -*- coding: utf-8 -*-
import loadDataModel as ldm
import pStat

'''
sdataType类属性解析（用于计算获取数据）:
    basedatas:原始数据名(str or list)
    dataname:创建的统计数据名(str)
    datatype:数据计算方式（str） ，默认为空
            当basedatas属性为list，该属性需填写
'''
class sDataType(object):
    def __init__(self , baseDataNames , newDataName , dataType = '' ):
        self._baseDataNames = pStat.statChangeListType(baseDataNames)
        self._newDataName = newDataName
        self._dataType = pStat.statChangeListType(dataType)

    @property
    def baseDataNames( self ):
        return self._baseDataNames

    @property
    def newDataName( self ):
        return self._newDataName

    @property
    def dataType( self ):
        return self._dataType

'''
dataStatGraphProperty类属性解析（）:
    datadir：数据地址(str)
    stype：视图类型(str) (Bar:柱状图 Line:折线图 Pie:饼状图 Rank:排行榜)
    series：视图系列(str)
    category：视图类别(str)
    sdatatype：视图数据类型(sdataType or list（sdataType）)
'''
class dataStatGraphProperty(object):
    def __init__(self , dataDir, sType , series , category , sDataType:sDataType):
        self._dataDir = dataDir
        self._sType = sType
        self._series = series
        self._category = category
        self._sDataType = sDataType
        self._statData = None

    @property
    def dataDir( self ):
        return self._dataDir

    @property
    def sType( self ):
        return self._sType

    @property
    def series( self ):
        return self._series

    @property
    def category( self ):
        return self._category

    @property
    def sDataType( self ):
        return self._sDataType

    @property
    def statData(self):
        return self._statData

    @statData.setter
    def statData(self,value):
        self._statData = value

    def dataGet(self,path,options):
        sdt = self.sDataType
        self._statData = ldm.dataStat(path, self.dataDir)
        colNames = options + [self.series, self.category]
        dataNames = sdt.baseDataNames
        self._statData.dsSum(colNames, dataNames)
        if sdt.dataType:
            self._statData.dsCal(sdt.newDataName, sdt.baseDataNames, sdt.dataType)
        else:
            self._statData.dsReName(sdt.newDataName, sdt.baseDataNames)
        self._statData.dsLoc(colNames, sdt.newDataName)




class dsgpGroup(object):
    def __init__(self , *dsgps:dataStatGraphProperty , options = [] ):
        self._dsgps = list(dsgps)
        self._options = pStat.statChangeListType(options)

    @property
    def dsgps( self ):
        return self._dsgps

    @property
    def options( self ):
        return self._options

    def append(self , dsgp):
        self._dsgps.append(dsgp)

    def groupViewRenderEmbed(self, path):

        pass

    def groupDataGet(self, path):
        for dsgp in self.dsgps:
            dsgp.dataGet(path,self.options)