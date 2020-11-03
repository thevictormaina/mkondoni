from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required
from . import auth
# from ..models import 
# from .forms import 
from .. import db

@auth.route("/login", methods=["GET", "POST"])
def login(): 
    pass

@auth.route("/sign-out")
# @login_required
def logout():
    pass

@auth.route("/sign-in", methods = ["GET", "POST"])
def sign_in():
    pass