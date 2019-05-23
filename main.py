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

if __name__ == "__main__":
  app.run()