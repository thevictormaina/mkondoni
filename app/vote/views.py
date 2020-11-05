from flask import render_template, request, redirect, url_for, abort
from . import vote
from ..models import Voter, President, Senator, Governor, Party, Deputy
from flask_login import login_required
from .. import db
from flask_login import login_required, current_user

@vote.route("/president", methods=["GET", "POST"])
def vote_president():
    """
    """
    president_id = request.form["president"]

    president = President.query.filter_by(id = president_id).first()

    president.add_vote()
    print("\nPresident Votes: ", president.first_name, " ", president.votes)

    return redirect(url_for("main.senator"))

@vote.route("/senator")
def vote_senator():
    """
    """
    pass

@vote.route("/governor")
def vote_governor():
    """
    """
    pass