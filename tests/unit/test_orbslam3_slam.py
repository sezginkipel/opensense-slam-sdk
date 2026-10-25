import unittest
from neuronav.algorithms.orbslam3_slam import ORBSLAM3

class TestORBSLAM3(unittest.TestCase):
    def setUp(self):
        self.slam = ORBSLAM3()

    def test_configure(self):
        config = {'mode': 'RGB-D-Inertial'}
        self.slam.configure(config)
        self.assertEqual(self.slam.config['mode'], 'RGB-D-Inertial')

    def test_set_sensor_topics(self):
        topics = {'color': '/camera/color/image_raw', 'depth': '/camera/aligned_depth_to_color/image_raw', 'imu': '/imu/data'}
        self.slam.set_sensor_topics(topics)
        self.assertEqual(self.slam.sensor_topics, topics)

    def test_get_algorithm_name(self):
        self.assertEqual(self.slam.get_algorithm_name(), 'ORB-SLAM3')

    def test_get_version(self):
        self.assertIsNotNone(self.slam.get_version())

if __name__ == '__main__':
    unittest.main()