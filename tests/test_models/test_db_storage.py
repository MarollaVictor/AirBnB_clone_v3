import unittest
from models import storage
from models.state import State

@unittest.skipIf(models.storage.__class__.__name__ != 'DBStorage', 'DBStorage test')
class TestDBStorageGetCount(unittest.TestCase):
    def setUp(self):
        self.storage = storage
        self.storage.reload()
        self.state = State(name="California")
        self.storage.new(self.state)
        self.storage.save()

    def test_get_existing_object(self):
        retrieved = self.storage.get(State, self.state.id)
        self.assertEqual(retrieved.id, self.state.id)

    def test_get_non_existing_object(self):
        self.assertIsNone(self.storage.get(State, "invalid_id"))

    def test_count_with_class(self):
        self.assertEqual(self.storage.count(State), 1)

    def test_count_without_class(self):
        self.assertGreaterEqual(self.storage.count(), 1)

    def tearDown(self):
        self.storage.delete(self.state)
        self.storage.save()
