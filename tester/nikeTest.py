import unittest
import json

from Nike.NikeClass import Nike
from Nike.dailyRaffle import dailyRaffle
from libs.chrome_setting import quitDriver

with open ('./.env.json') as f:
    json_data = json.load(f)
    DATA = json_data['user'][0]

class TestNikeRaffleAutomation(unittest.TestCase):
    '''Test Nike Raffle Automation '''

    def setUp(self):
        self.nike = Nike(id =DATA['id'], password=DATA['password'], size = DATA['shoes_size'])

    def test_login_returns_True(self):
        login_status = self.nike.login()
        self.assertTrue(login_status)

    def test_daily_raffle_function(self):
        dailyRaffle(DATA)
    
    


if __name__=='__main__':
    unittest.main()