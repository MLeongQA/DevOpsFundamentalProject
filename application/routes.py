from application import app, db
from application.models import UserProfile, DotaGame
from application.forms import DotaGameForm, UserProfileForm
from flask import redirect, url_for, request, render_template

@app.route("/")
@app.route("/home")
def home():
    user_list = UserProfile.query.all()
    return render_template("home.html", users=user_list)

@app.route("/user_games", methods=["GET", "POST"])
def user_games():
    game_form = DotaGameForm()
    if request.method == "POST":
        request_user = game_form.user_id.data
        game_list = DotaGame.query.filter_by(user_id=request_user)
        return render_template("gamelist.html", games=game_list)
    
    else:
        return render_template("user_game.html", form=game_form)

@app.route("/games/<int:user_id>")
def games(user_id):
    game_list = DotaGame.query.filter_by(user_id=user_id)
    return render_template("gamelist.html", games=game_list)

@app.route("/create", methods=["GET", "POST"])
def create():
    user_form = UserProfileForm()

    if request.method == "POST":
        new_user = UserProfile(user_name=user_form.user_name.data, user_region=user_form.user_region.data, user_mmr=user_form.user_mmr.data)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for("home"))
    
    else:
        return render_template("create.html", form=user_form)

@app.route("/create_game", methods=["GET", "POST"])
def create_game():
    game_form = DotaGameForm()

    if request.method == "POST":
        new_game = DotaGame(user_id=game_form.user_id.data, hero_name=game_form.hero_name.data, game_duration=game_form.game_duration.data, win_loss=game_form.win_loss.data)
        db.session.add(new_game)
        db.session.commit()

        return redirect(url_for("games", user_id=game_form.user_id.data))
    
    else:
        return render_template("create_game.html", form=game_form)

@app.route("/update/<int:user_id>", methods = ["GET", "POST"])
def update(user_id):
    user = UserProfile.query.get(user_id)
    user_form = UserProfileForm()

    if request.method == "POST":
        user.user_name = user_form.user_name.data
        user.user_region = user_form.user_region.data
        user.user_mmr = user_form.user_mmr.data
        db.session.add(user)
        db.session.commit()

        return redirect(url_for("home"))
    
    else:
        return render_template("create.html", form=user_form)
    

@app.route("/delete/<int:user_id>")
def delete(user_id):
    user = UserProfile.query.get(user_id)
    games = DotaGame.query.filter(user_id==user_id).delete()
    db.session.delete(user) 
    db.session.commit()

    return redirect(url_for("home"))

@app.route("/updategame/<int:game_id>", methods = ["GET", "POST"])
def updategame(game_id):
    game = db.session.query(DotaGame).filter_by(replay_id=game_id).first()
    game_form = DotaGameForm()

    if request.method == "POST":
        game.user_id = game_form.user_id.data
        game.hero_name = game_form.hero_name.data
        game.game_duration = game_form.game_duration.data
        game.win_loss = game_form.win_loss.data
        db.session.add(game)
        db.session.commit()

        return redirect(url_for("games", user_id = game.user_id))
    
    else:
        return render_template("create_game.html", form=game_form)
    

@app.route("/delete_game/<int:game_id>")
def deletegame(game_id):
    game = DotaGame.query.get(game_id)
    id = game.user_id
    db.session.delete(game)
    db.session.commit()

    return redirect(url_for("games", user_id = id))
