from django.test import TestCase

from spacex.tasks import Database

class DatabaseTestCase(TestCase):

    def test_testing_runs(self):
        self.assertTrue(Database.testing())

    def test_database_update_runs(self):
        """Test that database update command runs without error"""
        self.assertTrue(Database.update())

    def test_database_purge_runs(self):
        """Test that database purge command runs without error"""
        self.assertTrue(Database.purge())
