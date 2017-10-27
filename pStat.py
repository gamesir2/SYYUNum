# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 14:00:11 2017

@author: xbproj02
"""
import pandas as pd
#data是pd.DataFrame类型
def statSearch( data , colNames):
    cns = statChangeListType(colNames) 
    return data.xs( tuple(cns) )

def statSum( data , colNames , dataNames ):
    cns = statChangeListType(colNames)
    dns = statChangeListType(dataNames)
    return data.loc[ : , cns + dns ].groupby(cns).sum()

def statCount( data ,  colNames , dataNames ):
    cns = statChangeListType(colNames)
    dns = statChangeListType(dataNames)
    return data.loc[ : , cns + dns ].groupby(cns).count()

def statSort( data , colNames , ascendType):
    return data.sort_index( by = colNames , ascending = ascendType)

#str转list
def statChangeListType( s ):
    if type(s) == list:
        return s
    else:
        return [s]

if __name__=='__main__':
    df = pd.DataFrame( {'state' : ['Ohio','Ohio','Ohio','Nevada','Nevada'],
        'year' : [2000,2001,2002,2001,2002],
        'po' : [1.5,1.7,3.6,2.4,2.9],})
    #print(df)
    #print(statCount(df,['state'],['year','po']))
    print(statSort(df,'po',False))