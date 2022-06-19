
from flask import Blueprint, jsonify, request, session, redirect, url_for, abort
from app.models import User, db, GameRequest, Game, Library
from passlib.hash import sha256_crypt


game_request_routes = Blueprint('gameRequests', __name__)

@game_request_routes.errorhandler(400)
def resource_not_found(e):
    return jsonify(error=str(e)), 400

@game_request_routes.route('/', methods=["GET", "POST"])
def getAllRequests():
  if (request.method == 'GET'):
    requestsFrom = GameRequest.query.all()
    if requests:
      return {'requests': requests}
    return "No requests"
  if(request.method == "POST"):
    data = request.json
    userName = data["requestOf"].split(" ")
    requestOf = User.query.filter(User.firstName == userName[0]).filter(User.lastName== userName[1]).first()
    if requestOf.id ==data["requestFrom"]:
      return abort(400, description="You cannot request games from yourself")
    game = Game.query.filter(Game.name == data['game']).first()
    maybeRequest = GameRequest.query.filter(GameRequest.gameId==game.id, GameRequest.userLibraryId==requestOf.id, GameRequest.userRequestId==data['requestFrom'], GameRequest.requestStatus=="Pending").first()
    if maybeRequest:
      return abort(400, description="You have already requested this game")
    newRequest = GameRequest(gameId=game.id, userLibraryId=requestOf.id, userRequestId=data['requestFrom'], requestStatus="Pending")
    db.session.add(newRequest)
    db.session.commit()
    return jsonify({'message': 'Sucess'}), 200
  else:
    return "No Requests"


@game_request_routes.route('/<userId>', methods=['GET', 'DELETE', 'PUT'])
def requestID(userId):
  if (request.method == 'GET'):
    requestsFrom = GameRequest.query.filter(GameRequest.userLibraryId == userId).all()
    requestsTo = GameRequest.query.filter(GameRequest.userRequestId == userId).all()
    requestsFromPendingArray =[]
    requestsFromCompletedArray =[]
    requestsFromBorrowedArray = []
    requestsToPendingArray =[]
    requestsToCompletedArray =[]
    requestsToBorrowedArray = []
    if requestsFrom:
      for grequest in requestsFrom:
        print(grequest)
        game = Game.query.filter(grequest.gameId== Game.id).first()
        user = User.query.filter(User.id == grequest.userRequestId).first()
        userName = user.firstName +" " + user.lastName
        requestsFromObj ={"game": game.name, "requestFrom": userName, "status": grequest.requestStatus, "requestId": grequest.id}
        if grequest.requestStatus == 'Pending':
          requestsFromPendingArray.append(requestsFromObj)
        elif grequest.requestStatus == 'Borrowed':
          requestsFromBorrowedArray.append(requestsFromObj)
        elif grequest.requestStatus == 'Completed':
          requestsFromCompletedArray.append(requestsFromObj)
    if requestsTo:
      for grequest in requestsTo:
        game = Game.query.filter(grequest.gameId== Game.id).first()
        user = User.query.filter(User.id == grequest.userLibraryId).first()
        userName = user.firstName +" " + user.lastName
        requestsToObj ={"game": game.name, "requestTo": userName, "status": grequest.requestStatus, "requestId": grequest.id}
        if grequest.requestStatus == 'Pending':
          requestsToPendingArray.append(requestsToObj)
        elif grequest.requestStatus == 'Borrowed':
          requestsToBorrowedArray.append(requestsToObj)
        elif grequest.requestStatus == 'Completed':
          requestsToCompletedArray.append(requestsToObj)
    return {"requestsFromPending": requestsFromPendingArray, "requestsToPending": requestsToPendingArray, "requestsFromCompleted": requestsFromCompletedArray, "requestsToCompleted": requestsToCompletedArray, "requestsFromBorrowed": requestsFromBorrowedArray, "requestsToBorrowed": requestsToBorrowedArray}
    return "No Request"
    # if (request.method == 'DELETE'):
    #     request = GameRequest.query.filter(GameRequest.id == requestId).one()
    #     if request:
    #         requestId = request.id
    #         db.session.delete(request)
    #         db.session.commit
    #         return {'requestId': requestId}
    # if (request.method == 'PUT'):
    #     request = GameRequest.query.filter(GameRequest.id == requestId).one()
    #     if request:
    #         status = request.requestStatus
    #         if status == 'Pending':
    #             request.requestStatus = 'Complete'
    #         return {"requestStatus": 'Complete'}
    return "No Request"
