import unittest

from bilifm.season import Season


class TestSeason(unittest.TestCase):
    def test_get_video_id(self):
        sea = Season(uid="3493297045637304", sid="1704442")
        sea.get_videos()
        self.assertGreater(sea.total, 0)
        self.assertEqual(sea.total, len(sea.videos))


if __name__ == "__main__":
    unittest.main()
