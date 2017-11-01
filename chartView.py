import pyecharts

class myBar(pyecharts.Bar):
    def __init__(self, subtitle, **kwargs):
        title = None
        super(myBar, self).__init__(title , subtitle, **kwargs)


class myLine(pyecharts.Line):
    def __init__(self, subtitle, **kwargs):
        title = None
        super(myLine, self).__init__(title , subtitle, **kwargs)

