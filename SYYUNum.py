# -*- coding: utf-8 -*-
from flask import Flask  , redirect , url_for , render_template, jsonify, request
import viewData

import pStat

app = Flask(__name__)
vnp = viewData.viewNavProperty()


@app.route('/')
def index():
    fist_url = vnp.channels()[0].hdir
    return  redirect(fist_url)

@app.route('/s/<channel>/<brand>/<stat>',methods = [ "POST", "GET" ])
def statweb(channel, brand, stat):
    if request.method == "POST":
        dg_id = request.form.get('dg_id',type=str)
        options = request.form.getlist('options[]')
        data = vnp.statViewsGetData(channel,stat,dg_id,options)
        return jsonify(data)
    else:
        vnp.statViewsStatUp(channel,brand,stat)
        context = {
            'channels': vnp.channels(),
            'brands': vnp.brands(channel),
            'stats': vnp.stats(channel, brand),
            'acchannel':channel,
            'acbrand':brand,
            'acstat':vnp.cndict[channel]['stat'][stat]['name'],
            'groupviews':vnp.statViewsRenderEmbed()
        }
        return render_template('index.html', **context)




if __name__ == '__main__':
    app.run()
