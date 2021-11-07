import unittest
import json

from Nike.NikeClass import Nike

with open ('./.env.json') as f:
    json_data = json.load(f)
    ID = json_data['user'][0]['id']
    PASSWORD = json_data['user'][0]['password']
SIZE = 270



class TestNikeRaffleAutomation(unittest.TestCase):
    '''Test Nike Raffle Automation '''

    def setUp(self):
        self.nike = Nike(id =ID, password=PASSWORD, size = SIZE)

    def test_login_returns_True(self):
        login_return = self.nike.login()
        self.assertTrue(login_return)

if __name__=='__main__':
    unittest.main()