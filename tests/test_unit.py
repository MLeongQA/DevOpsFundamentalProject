from flask_testing import TestCase
from flask import url_for

from application import app,db
from application.models import DotaGame, UserProfile

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQL_ALCHEMY_DATABASE_URI="sqlite:///test.db",
            SQLALCHEMY_TRACK_MODIFICATIONS = False,
            WTF_CSRF_ENABLED = True
        )

        return app

    def setUp(self):
        db.create_all()

        db.session.add(UserProfile(user_name="Testname", user_region="eu-west", user_mmr = 100))
        db.session.add(DotaGame(user_id=1, hero_name="Testheroname", game_duration=30, win_loss = "win"))
        db.session.commit()

    def tearDown(self):
        db.drop_all()

class TestRead(TestBase):
    def test_home(self):
        response = self.client.get(url_for("home"))
        assert "1 | Testname | eu-west | 100 |" in response.data.decode()

    def test_game(self):
        response = self.client.get(url_for("games", user_id=1))
        assert "1 | Testheroname | 30 | win |" in response.data.decode()

    def test_user_games(self):
        response = self.client.get(url_for("user_games"))
        self.assertEqual(response.status_code, 200)

        response = self.client.post(
            url_for("user_games"),
            data= {"user_id":1},
            follow_redirects = True
        )
        assert "1 | Testheroname | 30 | win |" in response.data.decode()


class TestCreate(TestBase):
    def test_create(self):
        
        response = self.client.get(url_for("create"))
        self.assertEqual(response.status_code, 200)

        response = self.client.post(
            url_for("create"),
            data= {"user_name": "Testname2", "user_region": "eu-east", "user_mmr": 0},
            follow_redirects = True
        )

        assert "2 | Testname2 | eu-east | 0 |" in response.data.decode()

    def test_create_game(self):
        response = self.client.get(url_for("create_game"))
        self.assertEqual(response.status_code, 200)

        response = self.client.post(
            url_for("create_game"),
            data= {"user_id":1, "hero_name":"Testheroname2", "game_duration":40, "win_loss": "win"},
            follow_redirects = True
        )
        
        assert "2 | Testheroname2 | 40 | win" in response.data.decode()

class TestUpdate(TestBase):
    def test_update(self):
        response = self.client.get(url_for("update", user_id = 1))
        self.assertEqual(response.status_code, 200)

        response = self.client.post(
            url_for("update", user_id = 1),
            data={"user_name": "update_name", "user_region": "eu-west", "user_mmr": 100},
            follow_redirects=True
        )

        assert "1 | update_name | eu-west | 100 |" in response.data.decode()
        assert "1 | Testname | eu-west | 100 |" not in response.data.decode()

    def test_update_game(self):
        response = self.client.get(url_for("updategame", game_id = 1))
        self.assertEqual(response.status_code, 200)

        response = self.client.post(
            url_for("updategame", game_id=1),
            data={"user_id": 1, "hero_name":"update_hero_name", "game_duration": 35, "win_loss": "loss"},
            follow_redirects=True
        )

        assert "update_hero_name" in response.data.decode()
        assert "2 | Testheroname2 | 40 | win" not in response.data.decode() 

class TestDelete(TestBase):
    def test_delete_game(self):
        response = self.client.get(url_for("deletegame", game_id=1),
        follow_redirects = True)
        assert "1 | Testheroname | 30 | win |" not in response.data.decode()

    def test_delete(self):
        response = self.client.get(url_for("delete", user_id=1),
        follow_redirects = True)
        assert "1 | update_name | eu-west | 100 |" not in response.data.decode()