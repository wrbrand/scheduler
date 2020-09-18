import unittest
import scheduler

class TestScheduler(unittest.TestCase):
    def test_parsing(self):
        parsed = scheduler.parse('inputs/good.txt')
        self.assertEqual(parsed[0].__repr__(), "There's Something About Mary - Rated R, 2:14")
        
if __name__ == "__main__":
    unittest.main()