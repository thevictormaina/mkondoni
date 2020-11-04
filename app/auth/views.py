from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required
from . import auth
from .. models import Voter
from .forms import LoginForm
from .. import db

@auth.route("/login", methods=["GET", "POST"])
def login(): 
    title = "Mkondoni"
    login_form = LoginForm()
    if login_form.validate_on_submit():
        voter =Voter.query.filter_by(passport=login_form.passport.data).first()
        if voter is not None:
            login_user(voter)
            return redirect(request.args.get('next') or url_for('main.index'))

    return render_template("auth/login.html", title = title,login_form=login_form)
    
@auth.route("/sign-out")
# @login_required
def logout():
    pass

@auth.route("/sign-in", methods = ["GET", "POST"])
def sign_in():
    pass