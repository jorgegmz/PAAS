import unittest
from src.cloud_service import CloudService

class TestCloudAPIService(unittest.TestCase):
    def setUp(self):
        self.func = CloudService()

    def test_number_of_passwd_users(self):
        self.assertNotEqual(len(self.func.get_passwd_users()),  0)

    def test_invalid_username(self):
        self.assertIsNot(self.func.get_passwd_users_using_query_parameters({'name':'rootts'})
                , {'names':'root'})
    def test_valid_username(self):
        self.func.get_passwd_users_using_query_parameters({'name':'root'})
        self.assertEqual(self.func.passwd_users_match_params, [{"comment": "root"
            ,"gid": "0"
            ,"home": "/root"
            ,"name": "root"
            ,"shell": "/bin/bash\n"
            ,"uid": "0"
            }])

if __name__=='__main__':
    unittest.main()
