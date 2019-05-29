from flask import Blueprint
from flask import jsonify, request, json, make_response

# Google Api related packages
from apiclient import discovery
from oauth2client import client

#   Import user servies
from ..services.user import UserClass
userServices = UserClass()

from flask_jwt_extended import jwt_required, get_jwt_identity, jwt_refresh_token_required, create_access_token

Auth = Blueprint('auth', __name__)

@Auth.route('/refresh', methods=['POST'])
@jwt_refresh_token_required
def refresh():
    current_user = get_jwt_identity()
    ret = {
        'access_token': create_access_token(identity=current_user)
    }
    return jsonify(ret), 200

@Auth.route('/signin',methods=["POST"])
def firebaseAuth():
    request_data = request.get_json()
    result = userServices.firebaseUser(request_data['id_token'])
    return jsonify(result), result['status']
