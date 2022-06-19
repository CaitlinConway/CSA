
from flask import Blueprint, jsonify, request, session, redirect, url_for
from app.models import User, db
from passlib.hash import sha256_crypt


user_routes = Blueprint('users', __name__)


@user_routes.route('/')
def index():
    if 'userId' in session:
        response = User.query.all()
        return {"users": [user.to_dict() for user in response]}


@user_routes.route("/login", methods=["POST"])
def login():
    data = request.json
    user = User.query.filter(User.email == data["email"] and
                             sha256_crypt.verify(data.password, User.password)).one()
    # user_data = user.to_dict()
    if user:
        session["userId"] = user.id
        session["userEmail"] = user.email
        session['userFirstName'] = user.firstName
        session['userLastName'] = user.lastName
        session['userZipCode'] = user.zipCode
        print(f"success, {user.id, user.email}")
        return {"id": str(user.id), "email": str(user.email), "zipCode": str(user.zipCode),
                "firstName": str(user.firstName), "lastName": str(user.lastName)}
        # return{'user': session['user']}, 200
    return "error, user not found"


@user_routes.route("/logout", methods=["DELETE"])
def logout():
    if "userId" in session:
        session.pop('userId', None)
        return {'msg': 'successfully logged out'}
    return "error, already logged out"


@user_routes.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()
    user = User.query.filter(User.email == data["email"]).first()
    if user:
        return {"error": "This user account already exists."}
    if (len(data["password"]) < 8):
        return {"error": "Password must be at least 8 characters."}
    elif data:
        newUser = User(email=data["email"],
                       password=sha256_crypt.hash(data["password"]),
                       firstName=data["firstName"],
                       lastName=data["lastName"],
                       zipCode=(data["zipCode"]))
        db.session.add(newUser)
        db.session.commit()
        created = User.query.filter(User.email == data["email"]).first()
        return {"id": created.id, "email": created.email, "zipCode": str(created.zipCode)}


@user_routes.route('/current', methods=['GET'])
def load_user():
    print(session["userId"])
    if 'userId' in session:
        return {"userId": session['userId'], 'userEmail': session['userEmail'],  "userFirstName": session['userFirstName'], "userLastName": session['userLastName'], "zipCode": session['userZipCode']}, 200
    else:
        return {"msg": "user not loaded"}
