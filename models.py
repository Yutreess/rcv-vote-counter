# Import database object from app.py
from app import db

class Candidate(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80))
  
  rank_one_votes = db.Column(db.Integer)
  rank_two_votes = db.Column(db.Integer)
  rank_three_votes = db.Column(db.Integer)
  rank_four_votes = db.Column(db.Integer)
  rank_five_votes = db.Column(db.Integer)
  """
  # For Write Ins with 5 Declared Candidates
  rank_six_votes = db.Column(db.Integer)
  """

  def __init__(self, name):
    self.name = name

class Voter(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(120))
  rank_one_vote = db.Column(db.Integer, db.ForeignKey('candidate.id'))
  rank_two_vote = db.Column(db.Integer, db.ForeignKey('candidate.id'))
  rank_three_vote = db.Column(db.Integer, db.ForeignKey('candidate.id'))
  rank_four_vote = db.Column(db.Integer, db.ForeignKey('candidate.id'))
  rank_five_vote = db.Column(db.Integer, db.ForeignKey('candidate.id'))

  def __init__(self, name):
    self.name = name