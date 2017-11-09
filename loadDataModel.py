# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 15:01:01 2017

@author: xbproj02
"""
import pandas as pd
import pStat

class baseData(object):
    def __init__(self, path, dataSource):
        self._dataSource = dataSource
        self._cList = {'年度':int,'月份':int,'零售吊牌金额':'float64'}
        self._path = path
        self.data = self.bdOutPutResult ( self._path )
    @property
    def cList( self ):
        return self._cList
    
    @property
    def data( self ):
        return self._data
    
    @data.setter
    def data( self , value):
        self._data = value
        self.bdMtype()
        
    @property
    def dataSource( self ):
        return self._dataSource
    
    @dataSource.setter
    def dataSource( self , value ):
        self._dataSource = value
        self.data = self.bdOutPutResult ( self._path )
    
    def bdPathMesh( self , path ):
        fullPath = path + '\\' + self._dataSource
        return fullPath

    def bdOutPutResult ( self , path ):
        bd = pd.read_excel( self.bdPathMesh( path) , skiprows = range(8) )
        return bd.drop( len(bd.index) - 1 )

    def bdAllOfColNames( self ):
        return self._data.columns.tolist()

    def bdMtype(self):
        for name in self.bdAllOfColNames():
            if name in self.cList.keys():
                self._data[[name]] = self._data[[name]].astype(self.cList[name])



class dataStat(object):
    def __init__( self , path, dataSource):
        self._bData = baseData(path, dataSource)

    @property
    def bData( self ):
        return self._bData
        
    @property
    def sData( self ):
        return self._sData
    
    def dsSearch( self ,colNames):
        return pStat.statSearch(self.sData,colNames).to_dict()

    def dsGetLevelIndex(self , level):
        return sorted(list(set(self.sData.index.get_level_values(level))))
    
    def dsSum( self , colNames , dataNames ):
        self._sData = pStat.statSum(self._bData.data , colNames , dataNames)
        return self.sData
    
    def dsCal( self , newDataName , baseDataNames , datatypes):
        evalstr = 'self._sData[newDataName]='
        ndn = []
        for baseDataName in baseDataNames :
            ndn.append('self._sData[\''+baseDataName +'\']')
        evalstr += datatypes.format(*ndn)
        exec(evalstr)
        return self.sData

    def dsLoc(self, newDataNames):
        self._sData = self.sData.loc[ : , newDataNames ]
        return self.sData

    def dsReName(self, newDataName, baseDataNames):
        if newDataName != baseDataNames:
            self._sData[newDataName] = self.sData[baseDataNames]
        return self.sData
    
    def dsCount( self , colNames ):
        self._sData = pStat.statCount(self._bData.data , colNames , dataNames)
        return self.sData

    def dsRank( self , dataNames , rankCount = 0 ) :
        self._sData = pStat.statSort(self._sData , dataNames , False)
        if rankCount == 0:
            return self.sData
        else:
            return self.sData.iloc[ :rankCount , : ]


if __name__=='__main__':
    path = r'C:\Users\xbproj02\Desktop\ZYXS\SM'
    ds = dataStat(path , '小类.xlsx')
    colNames = ['年度','月份','店仓区域名称']
    dataNames = ['零售数量']
    ds.dsSum(colNames , dataNames)
    # print(ds.dsCal('平均数',['零售金额','零售数量',],['/']))
    # a = pStat.statSum(bd.data , colNames , dataNames)
    print(ds.dsSearch([2015,1]))
    # print(ds.dsRank('零售数量'))
    # print(ds.dsSearch([2015,1]))
    # print(ds.dsGetLevelIndex('月份'))
    # print(ds.dsLoc(['零售数量']))