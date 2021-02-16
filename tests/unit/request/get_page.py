import unittest
from rq_scraper.request import get_page

class GetPageTest(unittest.TestCase):
    """
    Tests the functionality of rq_scraper.request.get_page method
    """

    @classmethod
    def setUpClass(cls):

        # define uri for testing
        cls.uri = ('https://www.espn.com/mens-college-basketball'
                   '/game?gameId=401265413')

    def test_get_page(self):

        page = get_page(self.uri)
        print(page)

if __name__ == '__main__':
    unittest.main()
