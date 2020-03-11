from bottle import (
    route, run, template, request, redirect
)
from sqlalchemy.testing import db
from cs102.homework06.bayes import NaiveBayesClassifier
from cs102.homework06.scraputils import get_news
from cs102.homework06.db import News, session
import bottle
@bottle.route('/')
@route("/news")
def news_list():
    s = session()
    rows = s.query(News).filter(News.label == None).all()
    return template('./news_template.tpl.html', rows=rows)


@route("/add_label/")
def add_label():
    s = session()
    id = request.query.id
    label = request.query.label
    news = s.query(News).get(id)
    news.label = label
    s.commit()
    redirect("/news")


@route("/update")
def update_news():
    s = session()
    base = s.query(News).all()
    new_news = get_news('https://news.ycombinator.com/newest', 34)
    for i in new_news:
        for j in base:
            if (i['title'] == j.title) and (i['author'] == j.author):
                break
            else:
                news = News(title=i['title'],
                            author=i['author'],
                            url=i["url"],
                            comments=i['comments'],
                            points=i['points'])
                s.add(news)
                s.commit()
    redirect("/news")


@route("/classify")
def classify_news():
    # PUT YOUR CODE HERE
    redirect("/news")


if __name__ == "__main__":
    run(host="localhost", port=8080)
