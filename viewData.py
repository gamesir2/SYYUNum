# -*- coding: utf-8 -*-\

import loadDataModel , statGtaphModel
import configdata as cd

ldm = loadDataModel
stat = statGtaphModel

class viewElement(object):
    def __init__(self , name , hdir):
        self._name = name
        self._hdir = hdir

    @property
    def name(self):
        return self._name

    @property
    def hdir(self):
        return self._hdir


class viewNavProperty(object):
    def __init__(self):
        self._cndict = cd.cndict

    @property
    def cndict(self):
        return self._cndict

    def channels(self):
        self._channels = []
        for key,value in self._cndict.items():
            hdir = self.brands(key)[0].hdir
            ve = viewElement(value['name'],hdir)
            self._channels.append(ve)
        return self._channels

    def brands(self, channel):
        self._brands = []
        for key,value in self._cndict[channel]['brand'].items():
            hdir = self.stats(channel, key)[0].hdir
            ve = viewElement(value, hdir)
            self._brands.append(ve)
        return self._brands

    def stats(self, channel, brand):
        self._stats = []
        if self._cndict[channel]['stat']:
            for key,value in self._cndict[channel]['stat'].items():
                hdir = '/s/' + channel + '/' + brand + '/' + key
                ve = viewElement(value['name'], hdir)
                self._stats.append(ve)
        else:
            self._stats.append(viewElement('null','/NULL'))
        return self._stats

    def statViewsRenderEmbed(self):
        views_render_embed = ''
        for dg in self._dgs:
            views_render_embed += dg.groupViewRenderEmbed() + '\n'
        return views_render_embed

    def statViewsStatUp(self, channel, brand , stat):
        self._dgs = []
        tPath = cd.path +'\\'+ channel + '\\' + brand
        for statdata in self._cndict[channel]['stat'][stat]['view']:
            dg = self.statGetDgsFromDict(statdata)
            dg.startUp(tPath)
            self._dgs.append(dg)

    def statGetDgsFromDict(self , statdata):
        dsgs = []
        for dsgdata in statdata['dsg']:
            dsg=stat.dataStatGraph(
                dsgdata.get('datadir'),
                dsgdata.get('ctype'),
                dsgdata.get('serise'),
                dsgdata.get('category'),
                stat.sDataType(
                    dsgdata['sdt'].get('baseDataName'),
                    dsgdata['sdt'].get('newDataName'),
                    dsgdata['sdt'].get('dataType'))
            )
            dsgs.append(dsg)
        dsgs=tuple(dsgs)
        return stat.dsgGroup(*dsgs,options=statdata['options'])


    def statViewsGetData(self, channel, stat , dg_id , options):
        for dg in self._dgs:
            if dg.dg_id == dg_id:
                return dg.getSelectDatasForWeb(options)

if __name__ == '__main__':
    vmp = viewNavProperty()
    vmp.statViewsStatUp('ZYXS','SM','XSFX')
    print(vmp.statViewsRenderEmbed())