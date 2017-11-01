# -*- coding: utf-8 -*-
from flask import Flask  , redirect , url_for , render_template, jsonify, request
import viewModel

app = Flask(__name__)
vnp = viewModel.viewNavProperty()


@app.route('/')
def index():
    fist_url = vnp.channels()[0].hdir
    return  redirect(fist_url)

@app.route('/s/<channel>/<brand>/<stat>',methods = [ "POST", "GET" ])
def statweb(channel, brand, stat):
    if request.method == "POST":
        data = {

        }
        return jsonify(**data)
    else:
        context = {
            'channels': vnp.channels(),
            'brands': vnp.brands(channel),
            'stats': vnp.stats(channel, brand),
            'acchannel':channel,
            'acbrand':brand,
            'acstat':stat
        }
        return render_template('index.html', **context)


if __name__ == '__main__':
    app.run()
