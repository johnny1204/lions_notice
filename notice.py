from app.game import Game
import os
import time
from datetime import datetime
from flask import Flask, jsonify, abort, make_response

api = Flask(__name__)
path = "gameisover.txt"

def get_game_info():
  game = Game()
  live = game.live()
  if isinstance(live, str):
    open(path, "w")
  return jsonify({ "result": live })
  
@api.route('/notice/', methods=['GET'])
def notice():
  if os.path.exists(path):
    if datetime(*time.localtime(os.path.getctime(path))[:6]) < datetime.now():
      os.remove(path)
      return get_game_info()
  else:
    return get_game_info()

if __name__ == '__main__':
  api.run(debug=True)
