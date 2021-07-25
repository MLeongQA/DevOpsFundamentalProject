from application import db

class DotaGame(db.Model):
    replay_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user_profile.user_id"), nullable=False)
    hero_name = db.Column(db.String(20))
    game_duration = db.Column(db.Integer)
    win_loss = db.Column(db.String(10))

class UserProfile(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100))
    user_region = db.Column(db.String(10), default="eu-west")
    user_mmr = db.Column(db.Integer, default=0)
    user_games = db.relationship("DotaGame", backref="userprofile")






