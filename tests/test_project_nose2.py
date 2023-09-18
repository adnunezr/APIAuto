import unittest
import requests


### Test for Nose2
class projects():

    def setUp():
        print ("setup")
        self.token ="9d0eb672e2b8cb2b6febf3a4a49f652d7c6506ef"
        self.headers = {
            "Authorization": "Bearer {}".format(self.token)
        }
        self.url_base = "https://api.todoist.com/rest/v2/projects"
   
    @classmethod
    def setUpClass(cls):
        print("Setup Class")

    def test_one(self):
        print("Test one")

    def test_two(self):
        print("Test two")
    
    def tearDown(self):
        print("teardown")

    @classmethod
    def tearDownClass(cls):
        print("TearDown Class")
        

