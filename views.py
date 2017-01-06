#from flask import request
from flask import render_template
from red7 import app


@app.route('/')
def index():
    user = {'name': 'Alicja'}
    navigation = [
        {
            'href': 'omnie',
            'caption': 'O mnie'
        },
        {
            'href': 'kontakt',
            'caption': 'Kontakt'
        }
    ]
    return render_template('index.html', user=user, navigation=navigation)
