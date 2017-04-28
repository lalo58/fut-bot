#!/usr/bin/env python

import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = makeWebhookResult(req)

    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def makeWebhookResult(req):
    if req.get("result").get("action") == "fixture":
    result = req.get("result")
    parameters = result.get("parameters")
    equipo = parameters.get("equipo")

    #hora = {'America':"viernes a las 9 pm", 'Chiapas':"sabado a las 5 pm", 'Cruz Azul':"sabado a las 7 pm", 'Atlas':"viernes a las 9 pm", 'Guadalajara':"sabado a las 7 pm", 'Queretaro':"domingo a las 12 pm", 'Monterrey':"viernes a las 8 pm", 'Morelia':"sabado a las 7 pm", 'Pachuca':"sabado a las 7 pm", 'Puebla':"domingo a las 6 pm", 'Tijuana':"sabado a las 7 pm", 'Toluca':"domingo a las 12 pm", 'U.A.N.L':"sabado a las 7 pm", 'U.N.A.M':"sabado a las 7 pm", 'Veracruz':"viernes a las 8:30 pm", 'Necaxa':"domingo a las 12 pm"}
    #contra = {'America':'Atlas', 'Chiapas':'Santos', 'Cruz Azul':'Pachuca', 'Atlas':'América', 'Guadalajara':'León', 'Queretaro':'Toluca', 'Monterrey':'Veracruz', 'Pachuca':'CruzAzul', 'Puebla':'Necaxa', 'Tijuana':'Tigres', 'Toluca':'Querétaro', 'U.A.N.L':'Tijuana', 'U.N.A.M':'Morelia', 'Veracruz':"Monterrey", 'Necaxa':'Puebla'}
    
    #speech = "El " + equipo + " juega el " + hora[equipo] + " contra " + contra[equipo]  
     speech ="hola"
    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        #"data": {},
        # "contextOut": [],
        "source": "apiai-onlinestore-shipping"
    }

#aqui estab el codigo que quite
  
else:
    return {}


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print "Starting app on port %d" % port

    app.run(debug=True, port=port, host='0.0.0.0')
