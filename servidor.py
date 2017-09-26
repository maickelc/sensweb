# -*- coding: utf-8 -*-

__author__ = "maickel"
__date__ = "$11/09/2017 16:18:20$"

from flask import Flask, request
from datetime import datetime
import json
import sys

app = Flask(__name__)

@app.route('/teste/https', methods=['POST', 'GET'])
def teste():
    if request.method == 'POST':
        rqst = dict(request.form.items())
        for key, value in rqst.items():
            if 'SNR' in key:
                print("******* ", key, value)
            if 'SNA' in key:
                print("** ", key, value)
            print(key, value)
    else:
        print('GET', dict(request.args.items()))
    content = {'datetime': str(datetime.now())}
    return json.dumps(content), 200, {'ContentType':'application/json'}

if __name__ == "__main__":
    try:
        host, port = sys.argv[1].split(':')
        app.run(host=host, port=port)
    except:
        print('Problems!?')
        raise SystemExit
