import pyshorteners as ps
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired, url


app = Flask(__name__)
app.config['SECRET_KEY'] = 'zxcxzcxzcxzc'

class LoginForm(FlaskForm):
    url = StringField('url', validators=[InputRequired(), url()])

@app.route('/', methods=['GET', 'POST'])
def form():
    form = LoginForm()
    if form.validate_on_submit():
        shorten = ps.Shortener().tinyurl.short
        return f'<h3>The short url is {shorten(form.url.data)}</h3>'
    return render_template('form.html', form=form)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

