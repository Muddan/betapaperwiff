from flask import Blueprint
from flask import jsonify, request

# Google Api related packages
from apiclient import discovery
from oauth2client import client

#   Import user servies
from ..services.user import UserClass

from flask_jwt_extended import jwt_required, get_jwt_identity, jwt_refresh_token_required, create_access_token


Auth = Blueprint('auth', __name__)
userService = UserClass()


@Auth.route('/google', methods=["POST"])
def googleUser():
    request_data = request.get_json()

    # Exchange auth code for access token, refresh token, and ID token
    credentials = client.credentials_from_code(
        request_data['clientId'],
        'YmNtutMgrhk4qO-5Tn3o7Ki2',
        ['profile', 'email'],
        request_data["code"],
        redirect_uri=request_data['redirectUri']
    )

    # Get profile info from ID token
    userDetails = credentials.id_token
    response = userService.createGoogleUser(user=userDetails)
    return jsonify(response)


@Auth.route('/twitter', methods=["POST"])
def twitter():
    print(request.get_json())
    print('called twitter')
    return 'some data from twitter'


@Auth.route('/refresh', methods=['POST'])
@jwt_refresh_token_required
def refresh():
    current_user = get_jwt_identity()
    ret = {
        'access_token': create_access_token(identity=current_user)
    }
    return jsonify(ret), 200
