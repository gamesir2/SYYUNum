# -*- coding: utf-8 -*-
import loadDataModel as ldm
import pStat
from sqlalchemy import create_engine

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
    def __init__(self , dataDir, sType , series , category , *sDataTypes:sDataType):
        self._dataDir = dataDir
        self._sType = sType
        self._series = series
        self._category = category
        self._sDataTypes = list(sDataTypes)
        self._allBaseDataNames = []
        self._allNewDataNames = []

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
    def sDataTypes( self ):
        return self._sDataTypes

    @property
    def allBaseDataNames(self):
        if self._allBaseDataNames:
            return self._allBaseDataNames
        else:
            bds = []
            for sdt in self.sDataTypes:
                bds += sdt.baseDataNames
            self._allBaseDataNames = list(set(bds))
            return self._allBaseDataNames

    @property
    def allNewDataNames(self):
        if self._allNewDataNames:
            return self._allNewDataNames
        else:
            nds = []
            for sdt in self.sDataTypes:
                nds.append(sdt.newDataName)
            self._allNewDataNames = nds
            return self._allNewDataNames



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

    def dataView(self, path, firstnam):
        pass

    def dataGet(self, path, firstname):
        for dsgp in self.dsgps:
            ds = ldm.dataStat(path, dsgp.dataDir)
            colNames = self.options + [dsgp.sType , dsgp.series]
            dataNames = dsgp.allBaseDataNames
            ds.dsSum(colNames,dataNames)
            for sdt in dsgp.sDataTypes:
                if sdt.dataType:
                    ds.dsCal(sdt.newDataName,sdt.baseDataNames,sdt.dataType)
                else:
                    ds.dsReName(sdt.newDataName,sdt.baseDataNames)
            ds.dsLoc(colNames,dsgp.allNewDataNames)


    def toSql(self, name, data):
        conn = create_engine('mysql+mysqldb://root:password@localhost:3306/databasename?charset=utf8')
        data.to_sql(name, conn, if_exists='replace')