from flask import Blueprint, jsonify, request, session, redirect, url_for, abort
from app.models import User, db, Farm, AddOn, FarmAddOn
import requests
farm_routes = Blueprint('farms', __name__)

@farm_routes.errorhandler(400)
def resource_not_found(e):
    return jsonify(error=str(e)), 400

# @game_routes.route('/', methods=["POST", "GET"])
# def getAllGames():
#   if(request.method == "GET"):
#     games = Game.query.all()
#     gameArray =[]
#     if games:
#       for game in games:
#         gameName = Game.query.filter(Game.id == game.id).first()
#         gameObj = {"name": gameName.name, "id": game.id}
#         gameArray.append(gameObj)
#       return {"games": gameArray}
#     return "No games"
#   if (request.method == "POST"):
#     data = request.json
#     gameMaybe = Game.query.filter(Game.name==data["gameName"], Game.consoleId==data["consoleId"]).first()
#     if not gameMaybe:
#       game = Game(name=data["gameName"], consoleId=data["consoleId"])
#       db.session.add(game)
#     gameId = Game.query.filter(Game.name == data["gameName"]).first()
#     maybeLibrary = Library.query.filter(Library.userId==data["userId"], Library.gameId==gameId.id).first()
#     if not maybeLibrary:
#       newLibrary = Library(userId=data["userId"], gameId=gameId.id)
#       db.session.add(newLibrary)
#     if maybeLibrary:
#       return abort(400, description="You already own this game")
#     db.session.commit()
#     return jsonify({'message': 'Sucess'}), 200


# @game_routes.route('/<gameName>')
# def getGame(gameName):
#   r = requests.get(f'http://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={gameName}&format=json')
#   res = r.json()
#   return {gameName: res}

# @game_routes.route('/owners/<gameName>')
# def getGameOwner(gameName):
#   game = Game.query.filter(gameName == Game.name).first()
#   libraries = Library.query.filter(Library.gameId == game.id).all()
#   ownersArray =[]
#   for library in libraries:
#     owners = User.query.filter(User.id == library.userId).all()
#     for owner in owners:
#       name = owner.firstName + " " + owner.lastName
#       ownersArray.append(name)
#   return {"owners": ownersArray}



# @game_routes.route('/consoles')
# def getAllConsoles():
#   consoleArray = []
#   # gamesObj = {}
#   consoles = Console.query.all()
#   if consoles:
#     for console in consoles:
#       consoleName = Console.query.filter(
#       Console.id == console.id).first()
#       consoleArray.append(consoleName.name)
#         #     games = Game.query.filter(console.id == Game.consoleId).all()
#         #     gamesObj[consoleName.name] = []
#         #     array = gamesObj[consoleName.name]
#         #     print(array)
#         #     for game in games:
#         #         array.append(game.name)
#         # print(games)
#         # return {"consoles": consoleArray, "games": gamesObj}
#     return{"consoles": consoleArray}
#   return "No consoles"


# @game_routes.route('/console/<consoleName>')
# def getGamesByConsole(consoleName):
#   console = Console.query.filter(Console.name == consoleName).first()
#   consoleId = console.id
#   games = Game.query.filter(Game.consoleId == console.id).all()
#   gameArray =[]
#   if games:
#     for game in games:
#       gameName = game.name
#       gameArray.append(gameName)
#     return {console.name: gameArray}
#   return "No games"


# @game_routes.route('/library/<userId>')
# def getLibrary(userId):
#   libraries = Library.query.filter(Library.userId == userId).all()
#   library = []
#   if libraries:
#     for libraryGame in libraries:
#       game = Game.query.filter(Game.id == libraryGame.gameId).first()
#       gameName = game.name
#       library.append(gameName)
#     return {"library": library}
#   return {}
