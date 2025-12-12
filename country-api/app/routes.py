from flask import Blueprint, jsonify
from .service import CountryService

api_blueprint = Blueprint("api", __name__)

@api_blueprint.route("/country/<code>", methods=["GET"])
def get_country(code):
    result = CountryService.get_country_details(code)
    if result:
        return jsonify({"status": "success", "data": result})
    return jsonify({"status": "error", "message": "Invalid or unsupported country code"}), 400


@api_blueprint.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to Country Info API"})
