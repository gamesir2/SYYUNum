# -*- coding: utf-8 -*-
from flask import Flask  , redirect , url_for , render_template
import viewModel

app = Flask(__name__)
vnp = viewModel.viewNavProperty()


@app.route('/')
def index():
    fist_url = vnp.channels()[0].hdir
    return  redirect(fist_url)

@app.route('/<channel>/<brand>/<stat>')
def statweb(channel, brand, stat):
    context = {
        'channels': vnp.channels(),
        'brands': vnp.brands(channel),
        'stats': vnp.stats(channel, brand),
        'acstat':stat
    }
    return render_template('index.html', **context)


if __name__ == '__main__':
    app.run()
