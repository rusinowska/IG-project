#from flask import request
from flask import render_template
from red7 import app


@app.route('/')
def index():
    aplication = {'name': 'Red7'}
    user = {'name': 'Zosia Rusinowska'}
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
    return render_template('index.html', aplication=aplication, user=user, navigation=navigation)
