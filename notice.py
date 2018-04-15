from app.game import Game
game = Game()
live = game.live()
if isinstance(live, dict):
  if live['lions']['inning'] == live['opponent']['inning']:
    inning = '裏'
  elif live['lions']['inning'] > live['opponent']['inning']:
    inning = '表'

  info = '現在' + str(live['lions']['inning']) + '回' + inning + ' ' + \
live['lions']['total_score'] + '-' + live['opponent']['total_score'] + '\n' + \
str(live['lions']['inning']) + '回の得点' + live['lions']['inning_score'] + '点'
  print(info)
else:
  print(live)