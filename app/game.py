import requests
import re
from bs4 import BeautifulSoup

class Game:
  def __init__(self):
    url = "http://npb.jp/games/2018/"
    soup = BeautifulSoup(requests.get(url).content, 'html.parser')
    targets = soup.select('.score_table_wrap')
    for target in targets:
      if target.select("img[alt='埼玉西武ライオンズ']"):
        self.target = target

  def live(self):
    soup = BeautifulSoup(requests.get('http://npb.jp' + self.target.parent.get('href')).content, 'html.parser')
    score_board = soup.select("#table_linescore")[0]
    # if soup.select('.game_info')[0].text.replace("\n", " ").find("試合終了") > -1:
    #   return "試合終了"
    team = {}
    for span in score_board.select('th > span'):
      scores = self.scores(span)
      if span.text == "埼玉西武ライオンズ":
        key = 'lions'
      else:
        key = 'opponent'

      team[key] = {}
      team[key]['inning'] = scores[0]
      team[key]['inning_score'] = scores[1]
      team[key]['total_score'] = scores[2]
    return team

  def scores(self, target):
    current_inning = 0
    inning_score = 0
    total_score = 0
    for i, score in enumerate(target.parent.parent.find_all('td')):
      if not score.get('class') and score.text:
        current_inning = i + 1
        inning_score = score.text
      elif score.get('class') and score.get('class')[0] == "total-1":
        total_score = score.text

    return current_inning, inning_score, total_score

            