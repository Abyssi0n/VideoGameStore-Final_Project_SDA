from django.test import TestCase
from selenium import webdriver

from viewer.forms import GenreModelForm, PublisherModelForm, GameModelForm
from viewer.models import Genre, Publisher, Developer, Game


# FORM TESTS
class GenreFormTest(TestCase):
    def test_genre_valid(self):
        form = GenreModelForm(
            data={
                "name": "testing",
                "description": "success"
            }
        )
        self.assertTrue(form.is_valid())

    def test_genre_missing_name(self):
        form = GenreModelForm(
            data={
                "name": "",
                "description": "no name"
            }
        )
        self.assertFalse(form.is_valid())


class DeveloperFormTest(TestCase):
    def test_developer_valid(self):
        form = PublisherModelForm(
            data={
                "name": "Real one",
                "website": "seznam.cz",
                "about": "good!"
            }
        )
        self.assertTrue(form.is_valid())

    def test_developer_missing_name(self):
        form = PublisherModelForm(
            data={
                "name": "",
                "website": "google.com",
                "about": "bad"
            }
        )
        self.assertFalse(form.is_valid())

    def test_developer_invalid_url(self):
        form = PublisherModelForm(
            data={
                "name": "real dev",
                "website": "nope",
                "about": "badurl"
            }
        )
        self.assertFalse(form.is_valid())

    def test_developer_invalid_url2(self):
        form = PublisherModelForm(
            data={
                "name": "real dev",
                "website": "Hi?!.gov",
                "about": "shouldn't be"
            }
        )
        self.assertFalse(form.is_valid())


class PublisherFormTest(TestCase):
    def test_publisher_valid(self):
        form = PublisherModelForm(
            data={
                "name": "Real one",
                "website": "youtube.com",
                "about": "good!"
            }
        )
        self.assertTrue(form.is_valid())

    def test_publisher_missing_name(self):
        form = PublisherModelForm(
            data={
                "name": "",
                "website": "google.com",
                "about": "bad"
            }
        )
        self.assertFalse(form.is_valid())

    def test_publisher_invalid_url(self):
        form = PublisherModelForm(
            data={
                "name": "real pub",
                "website": "nah",
                "about": "badurl"
            }
        )
        self.assertFalse(form.is_valid())

    def test_publisher_invalid_url2(self):
        form = PublisherModelForm(
            data={
                "name": "real pub",
                "website": "Hi?!.gov",
                "about": "shouldn't be"
            }
        )
        self.assertFalse(form.is_valid())


class GameFormTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Genre.objects.create(name="Action")
        Genre.objects.create(name="Horror")
        Genre.objects.create(name="Sports")

        Publisher.objects.create(name="Pub1",
                                 website="google.com")
        Publisher.objects.create(name="Pub2",
                                 website="seznam.cz")
        Publisher.objects.create(name="Pub3",
                                 website="youtube.com")

        Developer.objects.create(name="Dev1",
                                 website="google.com")
        Developer.objects.create(name="Dev2",
                                 website="seznam.cz")
        Developer.objects.create(name="Dev3",
                                 website="google.com")

    def test_game_missing_name(self):
        form = GameModelForm(
            data={
                "name": "Game name",
                "genres": ["1", "2"],
                "price": "25.52",
                "developers": ["1"],
                "publishers": ["3"],
                "release_date": "2005-05-12",
                "description:": "This is a game",
                "system_reqs:": "System reqs or whatever",
            }
        )
        self.assertFalse(form.is_valid())

    def test_game_missing_genres(self):
        form = GameModelForm(
            data={
                "name": "Game name",
                "genres": "",
                "price": "25.52",
                "developers": ["1"],
                "publishers": ["3"],
                "release_date": "2005-05-12",
                "description:": "This is a game",
                "system_reqs:": "System reqs or whatever",
            }
        )
        self.assertFalse(form.is_valid())

    def test_game_missing_price(self):
        form = GameModelForm(
            data={
                "name": "Game name",
                "genres": ["3", "2"],
                "price": "",
                "developers": ["1"],
                "publishers": ["3"],
                "release_date": "2005-05-12",
                "description:": "This is a game",
                "system_reqs:": "System reqs or whatever",
            }
        )
        self.assertFalse(form.is_valid())

    def test_game_invalid_price_decimals(self):
        form = GameModelForm(
            data={
                "name": "Game name",
                "genres": ["3", "2"],
                "price": "5.362",
                "developers": ["1"],
                "publishers": ["3"],
                "release_date": "2005-05-12",
                "description:": "This is a game",
                "system_reqs:": "System reqs or whatever",
            }
        )
        self.assertFalse(form.is_valid())

    def test_game_invalid_price_digits(self):
        form = GameModelForm(
            data={
                "name": "Game name",
                "genres": ["3", "2"],
                "price": "500.362",
                "developers": ["1"],
                "publishers": ["3"],
                "release_date": "2005-05-12",
                "description:": "This is a game",
                "system_reqs:": "System reqs or whatever",
            }
        )
        self.assertFalse(form.is_valid())

    def test_game_not_real_devs(self):
        form = GameModelForm(
            data={
                "name": "Game name",
                "genres": ["3", "2"],
                "price": "50.362",
                "developers": ["1", "4"],
                "publishers": ["3"],
                "release_date": "2005-05-12",
                "description:": "This is a game",
                "system_reqs:": "System reqs or whatever",
            }
        )
        self.assertFalse(form.is_valid())

    def test_game_missing_date(self):
        form = GameModelForm(
            data={
                "name": "Game name",
                "genres": ["3", "2"],
                "price": "50.362",
                "developers": ["1"],
                "publishers": ["3"],
                "release_date": "",
                "description:": "This is a game",
                "system_reqs:": "System reqs or whatever",
            }
        )
        self.assertFalse(form.is_valid())

    def test_game_wrong_date_format(self):
        form = GameModelForm(
            data={
                "name": "Game name",
                "genres": ["3", "2"],
                "price": "500.62",
                "developers": ["1"],
                "publishers": ["3"],
                "release_date": "25-05-2012",
                "description:": "This is a game",
                "system_reqs:": "System reqs or whatever",
            }
        )
        self.assertFalse(form.is_valid())

    def test_game_missing_requirements(self):
        form = GameModelForm(
            data={
                "name": "Game name",
                "genres": ["3", "2"],
                "price": "500.36",
                "developers": ["1"],
                "publishers": ["3"],
                "release_date": "2025-01-01",
                "description:": "This is a game",
                "system_reqs:": "",
            }
        )
        self.assertFalse(form.is_valid())

# MODEL TESTS
class GameModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        game = Game.objects.create(
            name="testing game",
            price="25.25",
            release_date="2024-12-12",
            description="Test game",
            system_reqs="Whatever",
        )

        game2 = Game.objects.create(
            name="also testing",
            price="0.5",
            release_date="2000-07-11",
            description="Testing too",
            system_reqs="Nothing",
        )

        genre_horror = Genre.objects.create(name="Horror")
        genre_action = Genre.objects.create(name="Action")
        genre_sports = Genre.objects.create(name="Sports")

        pub_one = Publisher.objects.create(name="Pub1",
                                           website="google.com")
        pub_two = Publisher.objects.create(name="Pub2",
                                           website="seznam.cz")

        dev_one = Developer.objects.create(name="Dev1",
                                           website="google.com")
        dev_two = Developer.objects.create(name="Dev2",
                                           website="seznam.cz")

        game.genres.add(genre_horror)
        game.genres.add(genre_action)
        game2.genres.add(genre_horror)
        game2.genres.add(genre_sports)
        game2.genres.add(genre_action)

        game.publishers.add(pub_one)
        game2.publishers.add(pub_one)
        game2.publishers.add(pub_two)

        game.developers.add(dev_one)
        game.developers.add(dev_two)
        game2.developers.add(dev_two)
    def test_game_name(self):
        game = Game.objects.get(id=1)
        game2 = Game.objects.get(id=2)
        self.assertEqual(game.name, "testing game")
        self.assertEqual(game2.name, "also testing")

    def test_game_repr(self):
        game = Game.objects.get(id=1)
        game2 = Game.objects.get(id=2)
        self.assertEqual(game.__repr__(),"Game(name=testing game)")
        self.assertEqual(game2.__repr__(),"Game(name=also testing)")

    def test_game_str(self):
        game = Game.objects.get(id=1)
        game2 = Game.objects.get(id=2)
        self.assertEqual(game.__str__(),"testing game")
        self.assertEqual(game2.__str__(),"also testing")

    def test_game_genre_count(self):
        game = Game.objects.get(id=1)
        numgenres = game.genres.count()
        game2 = Game.objects.get(id=2)
        numgenres2 = game2.genres.count()
        self.assertEqual(numgenres, 2)
        self.assertEqual(numgenres2, 3)

    def test_game_dev_count(self):
        game = Game.objects.get(id=1)
        numdevs = game.developers.count()
        game2 = Game.objects.get(id=2)
        numdevs2 = game2.developers.count()
        self.assertEqual(numdevs, 2)
        self.assertEqual(numdevs2, 1)

    def test_game_pub_count(self):
        game = Game.objects.get(id=1)
        numpubs = game.publishers.count()
        game2 = Game.objects.get(id=2)
        numpubs2 = game2.publishers.count()
        self.assertEqual(numpubs, 1)
        self.assertEqual(numpubs2, 2)