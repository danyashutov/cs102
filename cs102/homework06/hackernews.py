from bottle import (
    route, run, template, request, redirect
)
from sqlalchemy.testing import db
from cs102.homework06.bayes import NaiveBayesClassifier
from cs102.homework06.scraputils import get_news
from cs102.homework06.db import News, session


@route("/news")
def news_list():
    s = session()
    rows = s.query(News).filter(News.label == None).all()
    return template('./news_template.tpl.html', rows=rows)


@route("/add_label/")
def add_label():
    # PUT YOUR CODE HERE
    redirect("/news")


@route("/update")
def update_news():
    # PUT YOUR CODE HERE
    redirect("/news")


@route("/classify")
def classify_news():
    # PUT YOUR CODE HERE
    redirect("/news")

if __name__ == "__main__":
    run(host="localhost", port=8080)

