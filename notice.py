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
  if isinstance(live, dict):
    if live['lions']['inning'] == live['opponent']['inning']:
      inning = '裏'
    elif live['lions']['inning'] > live['opponent']['inning']:
      inning = '表'

    info = '現在' + str(live['lions']['inning']) + '回' + inning + ' ' + \
  live['lions']['total_score'] + '-' + live['opponent']['total_score'] + '\n' + \
  str(live['lions']['inning']) + '回の得点' + str(live['lions']['inning_score']) + '点'
    print(info)
  else:
    open(path, "w")
    print(live)
  
@api.route('/notice/', methods=['GET'])
def notice():
  if os.path.exists(path):
    if datetime(*time.localtime(os.path.getctime(path))[:6]) < datetime.now():
      os.remove(path)
      get_game_info()
  else:
    get_game_info()
