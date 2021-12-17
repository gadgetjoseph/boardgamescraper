#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : GadgetJoseph
# Created Date: December 17, 2021
# =============================================================================
"""boardgame scraper project"""
# =============================================================================
# Imports
# =============================================================================
import requests
from bs4 import BeautifulSoup

URL = "https://boardgamegeek.com/browse/boardgame"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_games = soup.find_all(name="a", class_="primary")

game_titles = [game.getText() for game in all_games]
games = game_titles[::-1]

with open("games.txt", mode="w") as file:
    for game in games:
        file.write(f"{game}\n")

