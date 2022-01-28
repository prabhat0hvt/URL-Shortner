from shortner import app, db
from flask import render_template, redirect
from shortner.models import Shortner
from shortner.forms import ShortForm


def shorting(id):
    map = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    str = ""
    while(id > 0):
        str = str + map[id % 62]
        id = id//62
    return str[::-1]



@app.route("/", methods=['GET','POST'])
def home():
    form = ShortForm()
    link=""
    if form.validate_on_submit():
        str = Shortner.query.filter_by(url=form.url.data).first()
        if str:
            link = str.short
        else:
            user = Shortner(url=form.url.data)
            db.session.add(user)
            db.session.commit()
            user = Shortner.query.filter_by(url=form.url.data).first()
            user.short = shorting(int(user.id))
            db.session.commit()
            link = user.short
    return render_template('home.html', form=form, link=link)

@app.route("/<link>")
def mov(link):
    a = Shortner.query.filter_by(short=link).first()
    if a:
        return redirect(a.url)
    else:
        return render_template('404.html')


