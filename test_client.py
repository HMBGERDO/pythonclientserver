import unittest
from client import create_presence_message
from config import TIME, USER, ACCOUNT_NAME, ACTION, PRECENSE
from time import time


class clientTest(unittest.TestCase):
    def test_create_presence_message(self):
        message_guest = create_presence_message()
        message_time_guest = time()
        self.assertEqual(message_time_guest - message_guest[TIME] < 0.1, True)
        message_john = create_presence_message("John")
        message_time_john = time()
        self.assertEqual(message_time_john - message_john[TIME] < 0.1, True)
        self.assertEqual(message_guest, {ACTION: PRECENSE, TIME:message_guest[TIME], USER:{ACCOUNT_NAME:"guest"}})
        self.assertEqual(message_john, {ACTION: PRECENSE, TIME:message_john[TIME], USER:{ACCOUNT_NAME:"John"}})

if __name__ == "__main__":
    unittest.main()
