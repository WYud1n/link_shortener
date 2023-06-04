from data import db_session
from data.links import Link
from forms.home import Home
import random
from flask import Flask, render_template, abort, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def hash_generator():
    return ("%032x" % random.getrandbits(128))[:11]


@app.route('/', methods=['GET', 'POST'])
def home():
    form = Home()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        short_link = hash_generator()
        user = Link(
            full=form.link.data,
            short=short_link
        )
        db_sess.add(user)
        db_sess.commit()
        return render_template('home.html', title='Создание коротких ссылок', form=form, message=short_link)
    return render_template('home.html', title='Создание коротких ссылок', form=form)


@app.route('/<index>')
def redir(index):
    db_sess = db_session.create_session()
    link = db_sess.query(Link).filter(Link.short.like(index)).first()
    try:
        full = link.full
        return redirect(full, code=302)
    except AttributeError as e:
        print(e)


if __name__ == '__main__':
    db_session.global_init('db/links.db')
    app.run(port=8080, host='127.0.0.1')
