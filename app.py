import bs4
import requests

from bs4 import BeautifulSoup
from flask import Flask, request 
from bot import IndeedBot

app = Flask(__name__)

@app.route('/')
def index():
    iBot = IndeedBot(job_title='Web Developer')
    page = iBot.job_search()
    return

if __name__ == "__main__":
    app.run()
