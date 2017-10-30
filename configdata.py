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
            '销售分析':[
                dg(
                    dsg('小类.xlsx', 'Line', '年', '月', sdt('零售金额', '销售额') ),
                    dsg('小类.xlsx', 'Line', '年', '月', sdt(['零售金额', '零售数量'],'零售单价',dataType='/')),
                    options='店仓区域名称'
                ),
                dg(
                    dsg('小类.xlsx', 'Rank', '年', '店仓区域名称', sdt('零售金额', '销售额'))
                )
            ],
            '客户分析':[
                dg(
                    dsg('客户.xlsx', 'Line', '年', '月', sdt('零售单数', '客流量')),
                    dsg('客户.xlsx', 'Line', '年', '月', sdt(['零售金额', '零售单数'], '客单价', dataType='/')),
                    options='店仓区域名称'
                ),
                dg(
                    dsg('客户.xlsx', 'Bar', '年', '店仓区域名称', sdt('零售单数', '客流量')),
                    dsg('客户.xlsx', 'Bar', '年', '店仓区域名称', sdt(['零售金额', '零售单数'], '客单价', dataType='/')),
                    options='月'
                ),
            ],
            '类别分析':[
                dg(
                    dsg('小类.xlsx', 'Pie', '店仓区域名称', '大分类名称', sdt('零售金额', '销售额')),
                    dsg('小类.xlsx', 'Pie', '店仓区域名称', '大分类名称', sdt('零售数量', '销售量')),
                    options='年'
                ),
                dg(
                    dsg('小类.xlsx', 'Bar', '年', '店仓区域名称', sdt(['零售金额', '零售数量'],'零售单价', dataType='/')),
                    options='大分类名称'
                ),
                dg(
                    dsg('小类.xlsx', 'Rank', '大分类名称', '小分类名称', sdt('零售金额', '销售额', dataType='%')) ,
                    options=['年', '店仓区域名称']
                )
            ],
            '季节分析':[
                dg(
                    dsg('波段.xlsx', 'Bar' ,'季节名称', '月', sdt('销售数量','销售量')),
                    dsg('波段.xlsx', '%Bar','季节名称', '月', sdt('销售数量','销售量')),
                    options=['年', '店仓区域名称', '大分类名称']
                )
            ],
            '尺码&颜色分析':[
                dg(
                    dsg('尺寸.xlsx', 'Pie', '大分类名称', '尺码名称', sdt('销售数量','销售量')),
                    dsg('颜色.xlsx', 'Pie', '大分类名称', '颜色名称', sdt('销售数量','销售量')),
                    options=['年', '店仓区域名称']
                )
            ]
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