from django.test import TestCase
from django.utils import timezone
from unipath import Path
from portfolio.utils import create_photo_directory
from freezegun import freeze_time


class UtilsTest(TestCase):

    def setUp(self):
        self.headline = 'Test headline'

    def tearDown(self):
        created_dir = Path(
            './portfolio/static/portfolio/media/2016_08_19_Test_headline')
        created_dir.rmdir()

    @freeze_time("2016-08-19")
    def test_create_photo_directory(self):
        create_photo_directory(self.headline)
        created_dir = Path(
            './portfolio/static/portfolio/media/2016_08_19_Test_headline')
        self.assertTrue(created_dir.exists())
