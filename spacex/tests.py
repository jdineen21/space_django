from django.test import TestCase

from spacex.tasks import Database

class DatabaseTestCase(TestCase):

    def test_database_update_runs(self):
        """Test that database update command runs without error"""
        self.assertRegex(Database.update(), 'Done! Deserialized [0-9]+ objects')
    
    def test_database_purge_runs(self):
        """Test that database purge command runs without error"""
        self.assertEqual(Database.purge(), 'Done! Purge completed!')
