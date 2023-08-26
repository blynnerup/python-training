import unittest
from daily_activities import work, can_take_nap

class TestDailyActivities(unittest.TestCase):
    def test_should_be_working(self):
        self.assertEqual(
            work(9),
            True
        )

    def test_should_not_be_working(self):
        self.assertEqual(
            work(18),
            False
        )

    def test_can_nap(self):
        self.assertEqual(
            can_take_nap(17),
            'Ok, I can take a nap.'             
        )

if __name__ == "__main__":
    unittest.main()