import flask
from flask import Blueprint, jsonify
from controller.OnBoardingController import onboarding_api
import exceptions.travel_base_exception as travel_exception
from flask_jwt_extended import JWTManager

app = flask.Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
jwt = JWTManager(app)
app.secret_key = "secret key"

app.register_blueprint(onboarding_api, url_prefix='/onboarding')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)