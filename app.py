import flask
from flask import Blueprint, jsonify
from controller.OnBoardingController import onboarding_api
import exceptions.travel_base_exception as travel_exception

app = flask.Flask(__name__)
app.register_blueprint(onboarding_api, url_prefix='/onboarding')
app.secret_key = "secret key"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)