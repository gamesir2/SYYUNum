# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 15:01:01 2017

@author: xbproj02
"""
import pandas as pd
import pStat

class baseData(object):
    def __init__( self , path , dataSource ):
        self._dataSource = dataSource
        self._cList = {'年度':'int64','月份':'int64','零售吊牌金额':'float64'}
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
        fullPath = path + '/' + self._dataSource
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
    def __init__( self , bData ):
        self._bData = bData

    @property
    def bData( self ):
        return self._bData
        
    @property
    def sData( self ):
        return self._sData
    
    def dsSearch( self , colNames ):
        return pStat.statSearch( self._sData , colNames )
    
    def dsSum( self , colNames , dataNames):
        self._sData = pStat.statSum(self._bData.data , colNames , dataNames)
        return self.sData
    
    def dsAve( self , colNames, fName , sName , newColName):
        self.dsSum(colNames , [ sName , fName ])
        self._sData[newColName] =  self._sData[fName] / self._sData[sName]
        return self.sData
    
    def dsCount( self , colNames ):
        self._sData = pStat.statCount(self._bData.data , colNames , dataNames)
        return self.sData

    def dsRank( self , colNames , rankCount = 0 ) :
        self._sData = pStat.statSort(self._sData , colNames , False)
        if rankCount == 0:
            return self.sData
        else:
            return self.sData.iloc[ :rankCount , : ]


if __name__=='__main__':
    path = r'C:\Users\xbproj02\Desktop\SM'
    bd = baseData(path , '小类.xlsx')
    ds = dataStat(bd)
    colNames = ['年度','月份','店仓区域名称']
    dataNames = ['零售数量','零售金额', '零售吊牌金额']
    #ds.dsSum(colNames , dataNames)
    ds.dsSum(colNames , dataNames)
    print(ds.dsRank('零售金额' , rankCount=10))
    #a = pStat.statSum(bd.data , colNames , dataNames)
    #print(pStat.statSearch(a,[2015,1.0,'上海']))