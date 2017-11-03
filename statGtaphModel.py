# -*- coding: utf-8 -*-
import loadDataModel as ldm
import pStat
import json
import chartView
import uuid
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
        self._options = []

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
    def serieDict(self):
        return self._serieDict

    @property
    def categoryDict(self):
        return self._categoryDict

    @property
    def chart(self):
        return self._chart

    @property
    def options(self):
        return self._options

    @options.setter
    def options(self,value):
        self._options = value

    def dataGet(self,path):
        sdt = self.sDataType
        self._statData = ldm.dataStat(path, self.dataDir)
        if self.sType == 'Rank' or bool(self.series) == False :
            self._series = 'All'
            self._statData.bData.data[self.series] = self.sDataType.newDataName
        colNames = self.options + [self.series, self.category]
        dataNames = sdt.baseDataNames
        self._statData.dsSum(colNames, dataNames)
        if sdt.dataType:
            self._statData.dsCal(sdt.newDataName, sdt.baseDataNames, sdt.dataType)
        else:
            self._statData.dsReName(sdt.newDataName, sdt.baseDataNames)
        self._statData.dsLoc(sdt.newDataName)

        self._optionSelects = []
        for option in self.options:
            self._optionSelects.append({str(i): i for i in self._statData.dsGetLevelIndex(option)})

        self._serieDict = {str(i): i for i in self._statData.dsGetLevelIndex(self.series)}
        self._categoryDict = {str(i):i for i in self._statData.dsGetLevelIndex(self.category)}
        self._chartBuild()



#图形创建添加
    def _chartBuild(self):
        isRank = False
        xaxis_name = self.category
        Axis = 'xAxis'
        if self.sType == 'Bar':
            self._chart = chartView.myBar(self.sDataType.newDataName)
        elif self.sType == 'Line':
            self._chart = chartView.myLine(self.sDataType.newDataName)
        elif self.sType == 'Rank':
            self._chart = chartView.myBar(self.sDataType.newDataName)
            isRank = True
            xaxis_name = None
            Axis='yAxis'
        gvd = self.getFirstOptionData()
        i=0
        for key, value in self.serieDict.items():
            self._chart.add(key, gvd[Axis]['data'],gvd['series'][i]['data'],xaxis_name=xaxis_name,is_convert=isRank)
            i+=1

    def getFirstOptionData(self):
        firstOptionSelect = []
        for optionSelect in self.optionSelects:
            firstOptionSelect.append(pStat.dictKeysList(optionSelect)[0])
        return self.getOptionData(firstOptionSelect)

    def getOptionData(self,optionKeys):
        optionSelect=[]
        for i in range(len(optionKeys)):
            optionSelect.append(self.optionSelects[i][optionKeys[i]])

        if self.sType == 'Rank':
            gvd = {'yAxis': {}, 'series': []}
            l={}
            for ckey, cvalue in self.categoryDict.items():
                colname = optionSelect + [pStat.dictValueList(self.serieDict)[0], cvalue]
                l.update({ckey:self._statData.dsSearch(colname)})
            l = pStat.dictSorted(l)
            gvd['yAxis'].update({'data':pStat.dictKeysList(l)})
            gvd['series'].append({'name':pStat.dictKeysList(self.serieDict)[0],'data':pStat.dictValueList(l)})
        else:
            gvd = {'xAxis': {}, 'series': []}
            gvd['xAxis']={'data':list(self.categoryDict.keys())}
            for skey, svalue in self.serieDict.items():
                dic={'name':skey}
                l=[]
                for ckey, cvalue in self.categoryDict.items():
                    colname = optionSelect + [svalue , cvalue]
                    l.append(self._statData.dsSearch(colname))
                dic.update({'data': l})
                gvd['series'].append(dic)
        return gvd

    def getOptionJson(self,optionSelect):
        gvd =self.getOptionData(optionSelect)
        return json.dumps(gvd,indent=4)


    def chartRenderEmbed(self):
        return self.chart.render_embed()

    def chart_id(self):
        return self.chart.chart_id




class dsgGroup(object):
    def __init__(self , *dsgs:dataStatGraph , options = None ):
        self._dg_id = uuid.uuid4().hex
        self._dsgs = list(dsgs)
        self._options = options
        self._optionSelects ={}
        self._allCharts = []
        for dsg in self._dsgs:
            dsg.options = self.options

    @property
    def dg_id(self):
        return self._dg_id

    @property
    def dsgs(self):
        return self._dsgs

    @property
    def options(self):
        return pStat.statChangeListType(self._options)

    @property
    def optionSelects(self):
        return self._optionSelects

    @property
    def allCharts(self):
        return self._allCharts

    def startUp(self,path):
        self._allCharts = []
        for dsp in self._dsgs:
            dsp.dataGet(path)
            self._allCharts.append(dsp.chart)

        self._optionSelects = {}
        for optionSelect in self._dsgs[0].optionSelects:
            self._optionSelects.update({uuid.uuid4().hex:optionSelect})

    def groupViewRenderEmbed(self):
        embed = 'groupviews.html'
        tmp = pStat.JINJA2_ENV.get_template(embed)
        html = tmp.render(dg_id=self.dg_id,
                          optionSelects=self.optionSelects,
                          allcharts=self.allCharts

                          )
        return html

    def getSelectDatas(self,optionSelect):
        datadic = {}
        for dsp in self._dsgs:
            datadic.update({dsp.chart_id():dsp.getOptionData(optionSelect)})
        return datadic


if __name__=='__main__':
    path = r'C:\Users\xbproj02\Desktop'
    tPath = path + '\\' + 'ZYXS' + '\\' + 'SM'
    dg = dsgGroup
    dsg = dataStatGraph
    sdt = sDataType
    # ds = dsgGroup(
    #                 dataStatGraph('小类.xlsx', 'Line', '年度', '月份', sDataType('零售金额', '销售额') ),
    #                 dataStatGraph('小类.xlsx', 'Line', '年度', '月份', sDataType(['零售金额', '零售数量'],'零售单价',dataType='/')),
    #                 options='店仓区域名称'
    #             )
    ds = dg(
                dsg('小类.xlsx', 'Rank', '', '店仓区域名称', sdt('零售金额', '销售额')),
                options='年度'
            )
    ds.startUp(tPath)
    # ds.dsgs[0].chart.render()
    # print(ds.dsgs[0].chartRenderEmbed())
    # print(ds.optionSelects)
    # print(ds.getSelectDatas(['2015']))
    print(ds.groupViewRenderEmbed())