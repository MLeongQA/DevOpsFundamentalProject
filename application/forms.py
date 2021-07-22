from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateTimeField, SelectField, IntegerField

class DotaGameForm(FlaskForm):
    replay_id = StringField("Insert Replay ID")
    user_id = StringField("Insert User ID")
    hero_name = StringField("Insert Hero Played")
    game_duration = IntegerField("Insert Game Duration")
    win_loss = SelectField("Win/Loss", choices=[("win", "Win"), ("loss", "Loss")])
    submit_game = SubmitField("Add Game Record")

class UserProfileForm(FlaskForm):
    user_name = StringField("Insert Username")
    user_region = SelectField("Insert User Region", choices=[("europe-west", "EU West"), ("europe-east", "EU East"), ("russia", "Russia")])
    user_mmr = IntegerField("Insert mmr")
    submit_user = SubmitField("Add User")