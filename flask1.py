from flask import Flask, render_template, redirect, flash, url_for
from forms import loginform

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    form = loginform()
    if form.validate_on_submit():
        flash('You have logged in successfully!', 'success')
        return redirect(url_for('home'))
    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(port='80')
