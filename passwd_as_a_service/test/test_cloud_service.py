import unittest
from passwd_as_a_service.cloud_service import CloudService

class TestCloudAPIService(unittest.TestCase):
    def setUp(self):
        self.func = CloudService()

    def test_number_of_passwd_users(self):
        self.assertNotEqual(len(self.func.get_passwd_users()),  0)

    def test_invalid_username(self):
        self.assertIsNot(self.func.get_passwd_users_using_query_parameters({'name':'rootts'})
                , {'names':'root'})
    def test_valid_username(self):
        self

if __name__=='__main__':
    unittest.main()
