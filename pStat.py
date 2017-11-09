# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 14:00:11 2017

@author: xbproj02
"""
import pandas as pd
from jinja2 import Environment, FileSystemLoader
import os
import json
import datetime
#data是pd.DataFrame类型

def statSearch( data:pd.DataFrame , colNames):
    cns = statChangeListType(colNames)
    return data.xs( tuple(cns) )

def statSum( data:pd.DataFrame , colNames , dataNames ):
    cns = statChangeListType(colNames)
    dns = statChangeListType(dataNames)
    return data.loc[ : , cns + dns ].groupby(cns).sum()

def statCount( data:pd.DataFrame , colNames , dataNames ):
    cns = statChangeListType(colNames)
    dns = statChangeListType(dataNames)
    return data.loc[ : , cns + dns ].groupby(cns).count()

def statSort( data:pd.DataFrame , dataNames , ascendType):
    dns = statChangeListType(dataNames)
    return data.sort_values(by=dns ,ascending= ascendType)

#str转list
def statChangeListType( s ):
    if type(s) == list:
        return s
    elif s:
        return [s]
    else:
        return []

def get_resource_dir(folder):
    """
    :param folder:
    :return:
    """
    current_path = os.path.dirname(__file__)
    resource_path = os.path.join(current_path, folder)
    return resource_path

JINJA2_ENV = Environment(
    loader=FileSystemLoader(get_resource_dir('templates')),
    keep_trailing_newline=True,
    trim_blocks=True,
    lstrip_blocks=True)


def NonetoZero(num):
    if num == None:
        return 0
    else:
        return num

def dictSorted(dic:dict,reverse=False):
    newdic ={}
    for i in sorted(dic.items(), key=lambda d:NonetoZero(d[1]), reverse=reverse):
        newdic.update({i[0]:i[1]})
    return newdic

def dictKeysList(dic:dict):
    return list(dic.keys())

def dictValueList(dic:dict):
    return list(dic.values())

class UnknownTypeEncoder(json.JSONEncoder):
    """
    `UnknownTypeEncoder`类用于处理数据的编码，使其能够被正常的序列化
    """
    def default(self, obj):
        if isinstance(obj, (datetime.datetime, datetime.date)):
            return obj.isoformat()
        else:
            try:
                return obj.astype(float).tolist()
            except:
                try:
                    return obj.astype(str).tolist()
                except:
                    return json.JSONEncoder.default(self, obj)

def json_dumps(data, indent=0):
    """ json 序列化编码处理

    :param data: 字典数据
    :param indent: 缩进量
    :return:
    """
    return json.dumps(data, indent=indent,
                      cls=UnknownTypeEncoder)


if __name__=='__main__':
    df = pd.DataFrame( {'state' : ['Ohio','Ohio','Ohio','Nevada','Nevada'],
        'year' : [2000,2001,2002,2001,2002],
        'po' : [1.5,1.7,3.6,2.4,2.9],
        'jd': [1, 2, 3, 4, 5],})
    print(df)
    #print(statCount(df,['state'],['year','po']))
    print(list(df['po']/df['jd']))
    print(df[df['po']>2])
    # print(statSort(df,'po',False))