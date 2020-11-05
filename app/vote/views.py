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

@vote.route("/senator", methods=["GET", "POST"])
def vote_senator():
    """
    """
    senator_id = request.form["senator"]

    print("\nSenator ID: ", senator_id, "\n")

    senator = Senator.query.filter_by(id = senator_id).first()

    senator.add_vote()
    print("\nSenator Votes: ", senator.first_name, " ", senator.votes)

    return redirect(url_for("main.governor"))

@vote.route("/governor", methods=["GET", "POST"])
def vote_governor():
    
    governor_id = request.form["governor"]

    governor = Governor.query.filter_by(id = governor_id).first()

    governor.add_vote()
    print("\nGovernor Votes: ", governor.first_name, " ", governor.votes)

    return redirect(url_for("main.finish"))