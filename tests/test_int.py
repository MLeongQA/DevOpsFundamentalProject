from flask_testing import LiveServerTestCase
from flask import url_for
from selenium import webdriver
from urllib.request import urlopen

from application import app,db
from application.models import DotaGame, UserProfile

class TestBase(LiveServerTestCase):
    TEST_PORT = 5050 

    def create_app(self):
        app.config.update(
            SQL_ALCHEMY_DATABASE_URI="sqlite:///test.db",
            SQLALCHEMY_TRACK_MODIFICATIONS = False,
            LIVESERVER_PORT=self.TEST_PORT,

            DEBUG = True,
            TESTING = True
        )

        return app

    def setUp(self):
        chrome_options = webdriver.chrome.options.Options()
        chrome_options.add_argument('--headless')

        self.driver = webdriver.Chrome(options=chrome_options) 

        db.create_all()

        db.session.add(UserProfile(user_name="Testname", user_region="eu-west", user_mmr = 100))
        db.session.add(DotaGame(user_id=1, hero_name="Testheroname", game_duration=30, win_loss = "win"))
        db.session.commit()

        self.driver.get(f'http://localhost:{self.TEST_PORT}')

    def tearDown(self):
        self.driver.quit()
        db.drop_all()

    def test_server_status(self):
        response = urlopen(f"http://localhost:{self.TEST_PORT}")
        self.assertEqual(response.code, 200)


class TestLinks(TestBase):
    def test_create_profile_link(self):
        self.driver.find_element_by_xpath('/html/body/a[1]').click()
        self.assertIn(url_for("create"), self.driver.current_url)

    def test_create_game_link(self):
        self.driver.find_element_by_xpath('/html/body/a[2]').click()
        self.assertIn(url_for("create_game"), self.driver.current_url)

    def test_user_game_link(self):
        self.driver.find_element_by_xpath('/html/body/a[3]').click()
        self.assertIn(url_for("user_games"), self.driver.current_url)

    def test_update_profile_link(self):
        self.driver.find_element_by_xpath('/html/body/div[2]/a[1]').click()
        self.assertIn(url_for("update", user_id = 1), self.driver.current_url)
    
    def test_game_link(self):
        self.driver.find_element_by_xpath('/html/body/div[2]/a[3]').click()
        self.assertIn(url_for("games", user_id = 1), self.driver.current_url)

    def test_game_update_link(self):
        self.driver.find_element_by_xpath('/html/body/div[2]/a[3]').click()
        self.driver.find_element_by_xpath('/html/body/div[2]/a[1]').click()
        self.assertIn(url_for("updategame", game_id = 1), self.driver.current_url)

class TestCreateProfile(TestBase):
    def test_create_profile(self):
        self.driver.find_element_by_xpath('/html/body/a[1]').click()
        self.driver.find_element_by_xpath('//*[@id="user_name"]').send_keys("int_test")
        self.driver.find_element_by_xpath('//*[@id="user_mmr"]').send_keys(0)
        self.driver.find_element_by_xpath('//*[@id="submit_user"]').click()
        elements = self.driver.find_element_by_xpath('/html/body/div[3]')
        assert "int_test" in elements.text
        
class TestCreateGame(TestBase):
    def test_create_game(self):
        self.driver.find_element_by_xpath('/html/body/a[2]').click()
        self.driver.find_element_by_xpath('//*[@id="user_id"]').send_keys(1)
        self.driver.find_element_by_xpath('//*[@id="hero_name"]').send_keys("int_test_hero")
        self.driver.find_element_by_xpath('//*[@id="submit_game"]').click()
        elements = self.driver.find_element_by_xpath('/html/body/div[3]')
        assert "int_test_hero" in elements.text

class TestViewGame(TestBase):
    def test_view_game(self):
        self.driver.find_element_by_xpath('/html/body/a[3]').click()
        self.driver.find_element_by_xpath('//*[@id="user_id"]').send_keys(1)
        self.driver.find_element_by_xpath('//*[@id="view_game"]').click()
        elements = self.driver.find_element_by_xpath('/html/body/div[2]')
        assert "Testheroname" in elements.text

class UpdateProfile(TestBase):
    def update_profile(self):
        self.driver.find_element_by_xpath('/html/body/div[2]/a[1]').click()
        self.driver.find_element_by_xpath('//*[@id="user_name"]').send_keys("update_test")
        self.driver.find_element_by_xpath('//*[@id="submit_user"]').click()
        elements = self.driver.find_element_by_xpath('/html/body/div[3]')
        assert "update_test" in elements.text

class UpdateGame(TestBase):
    def update_game(self):
        self.driver.find_element_by_xpath('/html/body/div[2]/a[3]').click()
        self.driver.find_element_by_xpath('/html/body/div[2]/a[1]').click()
        self.driver.find_element_by_xpath('//*[@id="hero_name"]').send_keys("int_test_hero_update")
        self.driver.find_element_by_xpath('//*[@id="submit_game"]').click()
        elements = self.driver.find_element_by_xpath('/html/body/div[2]')
        assert "int_test_hero_update" in elements.text

class DeleteGame(TestBase):
    def update_game(self):
        self.driver.find_element_by_xpath('/html/body/div[2]/a[3]').click()
        self.driver.find_element_by_xpath('/html/body/div[2]/a[2]').click()
        elements = self.driver.find_element_by_xpath('/html/body/div[2]')
        assert "Testheroname" not in elements.text

class DeleteProfile(TestBase):
    def update_profile(self):
        self.driver.find_element_by_xpath('/html/body/div[2]/a[2]').click()
        elements = self.driver.find_element_by_xpath('/html/body/div[3]')
        assert "Testname" not in elements.text
        