# Flask FUnctionality
from flask import request, redirect, render_template, session, flash
# Import database object from app.py
from app import app, db
# Import Classes and shit
from models import Candidate, Voter

# Introduction Page
@app.route("/", methods=['GET', 'POST'])
def intro():
  candidates = Candidate.query.all()
  return render_template("introduction.html", candidates=candidates)

# Display Add Candidate Form
@app.route("/add-candidates", methods=['GET'])
def candidate_form():
  candidates = Candidate.query.all()
  return render_template("add-candidate.html", candidates=candidates)

# Process Add Candidate Form
@app.route("/add-candidates", methods=['POST'])
def add_candidate():
  candidate_name = request.form['candidate_name']

  if not candidate_name:
    flash("Please enter a Candidate Name.")
    return render_template("add-candidate.html", candidates=candidates)
  else:
    newCandidate = Candidate(candidate_name)
    db.session.add(newCandidate)
    db.session.commit()
    flash("Candidate added to Database.")
    return redirect("/add-candidates")

# Display Add Voter Form
@app.route("/add-voters", methods=['GET'])
def voter_form():
  voters = Voter.query.all()
  return render_template("add-voter.html", voters=voters)

# Process Add Voter Form
@app.route("/add-voters", methods=['POST'])
def add_voter():
  voter_name = request.form['voter_name']

  if not voter_name:
    flash("Please enter a Voter Name.")
    return render_template("add-voter.html", voters=voters)
  else:
    newVoter = Voter(voter_name)
    db.session.add(newVoter)
    db.session.commit()
    flash("Voter added to Database.")
    return redirect("/add-voters")

if __name__ == "__main__":
  app.run()