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
                ve = viewElement(key, hdir)
                self._stats.append(ve)
        else:
            self._stats.append(viewElement('null','/NULL'))
        return self._stats

    def statViewsRenderEmbed(self, channel, brand , stat):
        views_render_embed = ''
        tPath = cd.path +'\\'+ channel + '\\' + brand
        for dg in self._cndict[channel]['stat'][stat]:
            views_render_embed += dg.groupViewRenderEmbed(tPath) + '\n'
        return views_render_embed


if __name__ == '__main__':
    vmp = viewNavProperty()
    print([[i.name,i.hdir] for i in vmp.stats('ZYXS','SM')])
    print([[i.name,i.hdir] for i in vmp.brands('ZYXS')])
    print([[i.name,i.hdir] for i in vmp.channels()])