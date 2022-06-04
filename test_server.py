import unittest
from server import create_response_message
from config import TIME, RESPONSE
from time import time


class serverTest(unittest.TestCase):
    def test_create_response_message(self):
        responce_200 = create_response_message(200)
        responce_200_time = time()
        self.assertEqual(responce_200_time - responce_200[TIME] < 0.1, True)
        self.assertEqual(responce_200, {RESPONSE: 200, TIME:responce_200[TIME]})

if __name__ == "__main__":
    unittest.main()
