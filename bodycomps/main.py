from flask import Flask, url_for, render_template, request, redirect, jsonify, Blueprint
from jinja2 import TemplateNotFound
import requests

from config import configs

app = Flask(__name__)

bodycomps = Blueprint('bodycomps', __name__, )

CLIENT_ID = configs['client_id']
CUSTOMER_SECRET = configs['client_secret']
STATE = configs['state']
ACCOUNT_URL = configs['account_withings_url']
WBSAPI_URL = configs['wbsapi_withings_url']
CALLBACK_URI = configs['redirect']

"""
================================================================================
                     Authorization and Withings Data Update                     
================================================================================
"""


@app.route("/weightupdate")
def get_code():
    """
    Route to get the permission from an user to take his data.
    This endpoint redirects to a Withings' login page on which
    the user has to identify and accept to share his data
    """
    payload = {'response_type': 'code',  # imposed string by the api
               'client_id': CLIENT_ID,
               'state': STATE,
               'scope': 'user.info',  # see docs for enhanced scope
               'redirect_uri': CALLBACK_URI,  # URL of this app
               'mode': 'demo'  # Use demo mode, DELETE THIS FOR REAL APP
               }

    r_auth = requests.get(f'{ACCOUNT_URL}/oauth2_user/authorize2',
                          params=payload)

    return redirect(r_auth.url)


@app.route("/wiredirect")
def get_token():
    """
    Callback route when the user has accepted to share his data.
    Once the auth has arrived Withings servers come back with
    an authentication code and the state code provided in the
    initial call
    """
    code = request.args.get('code')
    state = request.args.get('state')

    payload = {'grant_type': 'authorization_code',
               'client_id': CLIENT_ID,
               'client_secret': CUSTOMER_SECRET,
               'code': code,
               'redirect_uri': CALLBACK_URI
               }

    r_token = requests.post(f'{ACCOUNT_URL}/oauth2/token',
                            data=payload).json()

    access_token = r_token.get('access_token', '')

    # GET Some info with this token
    headers = {'Authorization': 'Bearer ' + access_token}
    payload = {'action': 'getdevice'}

    # List devices of returned user
    r_getdevice = requests.get(f'{WBSAPI_URL}/v2/user',
                               headers=headers,
                               params=payload)

    print(r_getdevice)

    return r_getdevice.json()


"""
================================================================================
                                API Data Routes                                 
================================================================================
"""


@app.route("/getweights")
def get_weights():
    data = {
        "weights": [
            {
                "value": 1,
                "date": "10-10-2020 10:20:15"
            }
        ]
    }

    return jsonify(data)


"""
================================================================================
                                Front End Routes                                
================================================================================
"""


@app.route("/")
def index():
    return "<h2>Default Header</h2>"


if __name__ == "__main__":
    print("Is the main")
    app.run(host="127.0.0.1", port=5000, debug=True)
