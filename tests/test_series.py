import unittest

from bilifm.series import Series


class TestSeries(unittest.TestCase):
    def test_get_video_id(self):
        sea = Series(uid="488978908", series_id="888433")
        sea.get_videos()
        self.assertGreater(sea.total, 0)
        self.assertEqual(sea.total, len(sea.videos))


if __name__ == "__main__":
    unittest.main()
