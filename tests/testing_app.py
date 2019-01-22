import unittest

from app import app

class Mytdd(unittest.TestCase):
    """This class made to make all our tests for the project"""
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        
        
    def test_vue_runing(self):
        result = self.app.get("/")
        assert result.status_code == 200
    

    
if __name__ == '__main__':
    unittest.main()