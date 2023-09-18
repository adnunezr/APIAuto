import unittest


class TestProject(unittest.TestCase):

    def setUp(self):
        print("Setup")

    def Test_one(self):
        print("test one")

    def Test_two(self):
        print("test two")
    
    #fixture
    def teardown(self):
        print("teardown")
        