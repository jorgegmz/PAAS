import unittest
from passwd_as_a_service.cloud_service import CloudService

class TestCloudAPIService(unittest.TestCase):
    def setUp(self):
        self.func = CloudService()

    def test_1(self):
        self.assertNotEqual(len(self.func.get_passwd_users()),  0)

    def test_2(self):
        self.assertIsNot(self.func.get_passwd_users_using_query_parameters({'name':'rootts'})
                , {'names':'root'})

if __name__=='__main__':
    unittest.main()
