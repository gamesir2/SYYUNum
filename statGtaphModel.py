# -*- coding: utf-8 -*-
import loadDataModel as ldm
import pStat
import pyecharts

'''
sdataType类属性解析（用于计算获取数据）:
    basedatas:原始数据名(str or list)
    dataname:创建的统计数据名(str)
    datatype:数据计算方式（str） ，默认为空
            当basedatas属性为list，该属性需填写
'''
class sDataType(object):
    def __init__(self , baseDataNames , newDataName , dataType = None ):
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
dataStatGraph类属性解析（）:
    datadir：数据地址(str)
    stype：视图类型(str) (Bar:柱状图 Line:折线图 Pie:饼状图 Rank:排行榜)
    series：视图系列(str)
    category：视图类别(str)
    sdatatype：视图数据类型(sdataType)
'''
class dataStatGraph(object):
    def __init__(self , dataDir, sType , series , category , sDataType:sDataType):
        self._dataDir = dataDir
        self._sType = sType
        self._series = series
        self._category = category
        self._sDataType = sDataType
        self._statData:ldm.dataStat = None

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

    @property
    def optionSelects(self):
        return self._optionSelects

    @property
    def serieList(self):
        return self._serieList

    @property
    def categoryList(self):
        return self._categoryList

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

        self._optionSelects = []
        for option in options:
            self._optionSelects.append(self._statData.dsGetLevelIndex(option))

        self._serieList = self._statData.dsGetLevelIndex(self.series)
        self._categoryList = self._statData.dsGetLevelIndex(self.category)


    def getOptionData(self,optionSelect):
        gvd =[]
        for serie in self.serieList:
            l=[]
            for category in self._categoryList:
                colname = optionSelect + [serie , category]
                l.append(self._statData.dsSearch(colname))
            gvd.append({serie:l})
        return gvd

    def graphViewRenderEmbed(self):
        pass

    def setViewData(self,optionData):
        pass



class dsgGroup(object):
    def __init__(self , *dsgs:dataStatGraph , options = None ):
        self._dsgs = list(dsgs)
        self._options = options
        self._optionSelects = []

    @property
    def dsgs( self ):
        return self._dsgs

    @property
    def options( self ):
        return pStat.statChangeListType(self._options)

    @property
    def optionSelects(self):

        return self._optionSelects

    def groupViewRenderEmbed(self, path):
        for dsp in self.dsgs:
            dsp.dataGet(path,self.options)
        pass