from flask import render_template, request, redirect, url_for, abort
import datetime
from . import main
from ..models import Voter, President, Senator, Governor, Party, Deputy
from flask_login import login_required
from .. import db
from flask_login import login_required, current_user

@main.route("/", methods=["GET", "POST"])
def index():
    title = "Mkondoni"
    return render_template("index.html", title = title)

@main.route("/president", methods=["GET", "POST"])
@login_required
def president():
    """
    View function for loading president template
    """
    presidents = President.query.all()

    title = "Mkondoni - Presidential Vote"

    return render_template("vote/president.html", title = title, presidents = presidents)

@main.route("/senator", methods=["GET", "POST"])
@login_required
def senator():
    """
    View function for loading senator page
    """
    senators = Senator.query.all()

    title = "Mkondoni - Senatorial Vote"
    return render_template("vote/senator.html", senators = senators)

@main.route("/governor", methods=["GET", "POST"])
@login_required
def governor():
    """
    View function for loading senator page
    """
    governors = Governor.query.all()

    title = "Mkondoni - Gubernatorial Vote"
    return render_template("vote/governor.html", governors = governors)

@main.route("/finish", methods=["GET", "POST"])
@login_required
def finish():
    """
    View function for loading senator page
    """
    title = "Mkondoni - Thank You For Voting"
    return render_template("finish.html")

@main.route("/results", methods=["GET", "POST"])
def results():
    """
    """
    presidents = President.query.all()
    governors = Governor.query.all()
    senators = Senator.query.all()

    title = "Mkondoni - Results"

    return render_template("results.html", senators = senators, governors = governors, presidents = presidents)