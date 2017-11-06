# -*- coding: utf-8 -*-
import statGtaphModel as sgm


sdt = sgm.sDataType
dsg = sgm.dataStatGraph
dg = sgm.dsgGroup

path = r'C:\Users\xbproj02\Desktop'
cndict = {
    'ZYXS':{
        'name':'直营销售分析',
        'brand':{
            'SM':'三木',
            'SB':'圣宝'
        },
        'stat':{
            'XSFX':{
                'name':'销售分析',
                'view':[{
                    'dsg':[{
                        'datadir':'小类.xlsx',
                        'stype':'Line',
                        'serise':'年度',
                        'category':'月份',
                        'sdt':{
                            'baseDataName':['零售金额'],
                            'newDataName':'销售额',
                            'dataType':None
                            }},
                        {
                        'datadir': '小类.xlsx',
                        'stype': 'Line',
                        'serise': '年度',
                        'category': '月份',
                        'sdt': {
                            'baseDataName': ['零售金额', '零售数量'],
                            'newDataName': '零售单价',
                            'dataType': '{}/{}'
                        }}],
                    'options':'店仓区域名称'
                    },
                    {
                    'dsg':[{
                        'datadir': '小类.xlsx',
                        'stype': 'Rank',
                        'serise': None,
                        'category': '店仓区域名称',
                        'sdt': {
                            'baseDataName': '零售金额',
                            'newDataName': '销售额',
                            'dataType': None
                        }}],
                    'options':'年度'
                    }
                ]
            },
            'KHFX':{
                'name':'客户分析',
                'view':[{
                    'dsg':[{
                        'datadir':'客户.xlsx',
                        'stype':'Line',
                        'serise':'年度',
                        'category':'月份',
                        'sdt':{
                            'baseDataName':['零售单数'],
                            'newDataName':'客流量',
                            'dataType':None
                            }},
                        {
                        'datadir': '客户.xlsx',
                        'stype': 'Line',
                        'serise': '年度',
                        'category': '月份',
                        'sdt': {
                            'baseDataName':['零售金额', '零售单数'],
                            'newDataName': '客单价',
                            'dataType': '{}/{}'
                        }}],
                    'options':'店仓区域名称'
                    },
                    {
                    'dsg': [{
                        'datadir': '客户.xlsx',
                        'stype': 'Bar',
                        'serise': '年度',
                        'category': '店仓区域名称',
                        'sdt': {
                            'baseDataName': ['零售单数'],
                            'newDataName': '客流量',
                            'dataType': None
                        }},
                        {
                            'datadir': '客户.xlsx',
                            'stype': 'Bar',
                            'serise': '年度',
                            'category': '店仓区域名称',
                            'sdt': {
                                'baseDataName':['零售金额', '零售单数'],
                                'newDataName': '客单价',
                                'dataType': '{}/{}'
                            }}],
                    'options': '月份'
                    }
                ]
            },
            'LBFX':{
                'name':'类别分析',
                'view':[{
                    'dsg':[{
                        'datadir':'小类.xlsx',
                        'stype':'Pie',
                        'serise':'店仓区域名称',
                        'category':'大分类名称',
                        'sdt':{
                            'baseDataName':['零售金额'],
                            'newDataName':'销售额',
                            'dataType':None
                            }},
                        {
                        'datadir': '小类.xlsx',
                        'stype': 'Pie',
                        'serise': '店仓区域名称',
                        'category': '大分类名称',
                        'sdt': {
                            'baseDataName':['零售数量'],
                            'newDataName': '销售量',
                            'dataType': None
                        }}],
                    'options':'年度'
                    },
                    {
                    'dsg': [{
                            'datadir': '小类.xlsx',
                            'stype': 'Bar',
                            'serise': '年度',
                            'category': '店仓区域名称',
                            'sdt': {
                                'baseDataName':['零售金额', '零售数量'],
                                'newDataName': '零售单价',
                                'dataType': '{}/{}'
                            }}],
                    'options': '大分类名称'
                    },
                    {
                    'dsg': [{
                            'datadir': '小类.xlsx',
                            'stype': 'Rank',
                            'serise': None,
                            'category': '店仓区域名称',
                            'sdt': {
                                'baseDataName':['零售金额', '零售数量'],
                                'newDataName': '零售单价',
                                'dataType': '{}/{}'
                            }}],
                    'options': ['年度', '店仓区域名称','大分类名称']
                    },
                ]
            },
            'JJFX':{
                'name':'季节分析',
                'view':[{
                    'dsg':[{
                        'datadir':'波段.xlsx',
                        'stype':'Bar',
                        'serise':'季节名称',
                        'category':'月份',
                        'sdt':{
                            'baseDataName':['零售数量'],
                            'newDataName':'销售量',
                            'dataType':None
                            }},
                        {
                        'datadir': '波段.xlsx',
                        'stype': '%Bar',
                        'serise': '季节名称',
                        'category': '月份',
                        'sdt': {
                            'baseDataName':['零售数量'],
                            'newDataName': '销售量',
                            'dataType': None
                        }}],
                    'options':['年度', '店仓区域名称', '大分类名称']
                    }
                ]
            },
            'CMYS': {
                'name': '尺码&颜色分析',
                'view': [{
                    'dsg': [{
                        'datadir': '尺码.xlsx',
                        'stype': 'Pie',
                        'serise': '大分类名称',
                        'category': '尺码名称',
                        'sdt': {
                            'baseDataName': ['零售数量'],
                            'newDataName': '销售量',
                            'dataType': None
                        }},
                        {
                            'datadir': '颜色.xlsx',
                            'stype': 'Pie',
                            'serise': '大分类名称',
                            'category': '颜色名称',
                            'sdt': {
                                'baseDataName': ['零售数量'],
                                'newDataName': '销售量',
                                'dataType': None
                            }}],
                    'options': ['年度', '店仓区域名称']
                    }
                ]
            }
        }
   },
    'DH':{
        'name':'订货会分析',
        'brand':{
            'SM':'三木',
            'XB':'小冰熊'
        },
        'stat':{

        }
   },
    'JY':{
        'name':'经营分析',
        'brand':{
            'SM':'三木',
            'XB':'小冰熊'
        },
        'stat':{

        }
   }
}


if __name__ == '__main__':
    i = [str for str in cndict.keys()]
    print(i)