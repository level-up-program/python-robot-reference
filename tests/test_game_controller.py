from unittest import TestCase
from levelup.controller import GameController

class TestGameController(TestCase):
    def test_init(self):
        testobj = GameController()
        assert testobj.status != None

    def test_create_character_updates_status(self):
        testobj = GameController()
        arbitrary_name = "ARBITRARY"
        testobj.create_character(arbitrary_name)
        self.assertEqual(arbitrary_name, testobj.status.character_name)
        self.assertIsNotNone(testobj.character)
        
        
