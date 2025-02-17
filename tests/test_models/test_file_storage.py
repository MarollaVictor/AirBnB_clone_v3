import unittest
from models import storage
from models.state import State

@unittest.skipIf(storage._Storage__storage_type != 'file', 'FileStorage test')
class TestFileStorageGetCount(unittest.TestCase):
    def setUp(self):
        self.storage = storage
        self.storage.reload()
        self.state = State(name="Nevada")
        self.storage.new(self.state)
        self.storage.save()

    def test_get_existing_object(self):
        retrieved = self.storage.get(State, self.state.id)
        self.assertEqual(retrieved.id, self.state.id)

    def test_count_with_class(self):
        self.assertEqual(self.storage.count(State), 1)

    def test_count_without_class(self):
        self.assertGreaterEqual(self.storage.count(), 1)

    def tearDown(self):
        self.storage.delete(self.state)
        self.storage.save()
