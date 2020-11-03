from flask import render_template, request, redirect, url_for, abort
import datetime
from . import main
# from .forms import 
# from ..models import 
from flask_login import login_required
from .. import db
from flask_login import login_required, current_user

@main.route("/", methods=["GET", "POST"])
def index():
    title = "Mkondoni"
    return render_template("index.html", title = title)