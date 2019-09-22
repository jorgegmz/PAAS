import os

class CloudService:
    def __init__(self):
        self.file_passwd = '/etc/passwd'
        self.file_group = '/etc/group'
        self.passwd_arr = []
        self.group_arr = []
        self.valid_params = {}
        self.passwd_users_match_params = []
        self.group_users_match_params = []
        self.single_user_uid_response = []
        self.single_group_gid_response = []
        self.all_groups_user_uid_response = []

    def get_passwd_users(self):
        if len(self.passwd_arr) > 0:
            self.passwd_arr = []

        if os.path.exists(self.file_passwd):
            with open(self.file_passwd) as f:
                for line in f:
                    users_passwd_config = {'name':line.split(':')[0]
                            ,'uid':line.split(':')[2]
                            ,'gid':line.split(':')[3]
                            ,'comment':line.split(':')[4]
                            ,'home':line.split(':')[5]
                            ,'shell':line.split(':')[-1]
                            }
                    self.passwd_arr.append(users_passwd_config)

        return self.passwd_arr

    def get_group_users(self):
        if len(self.group_arr) > 0:
            self.group_arr = []

        if os.path.exists(self.file_group):
            with open(self.file_group) as f:
                for line in f:
                    users_group_config = {'name':line.split(':')[0]
                            ,'gid':line.split(':')[2]
                            , 'members':line.split(':')[-1]
                            }
                    self.group_arr.append(users_group_config)

        return self.group_arr

    def get_passwd_users_using_query_parameters(self, params):
        self.get_passwd_users()

        if len(self.passwd_users_match_params) > 0:
            self.passwd_users_match_params = []

        for val in self.passwd_arr:
            if not set(params.keys()).issubset(val.keys()):
                return 'incorrect url values'
            if self.compare_dict_values(val, params):
                self.passwd_users_match_params.append(val)

    def get_group_users_using_query_parameters(self, params):
        self.get_group_users()

        if len(self.group_users_match_params) > 0:
            self.group_users_match_params = []

        for val in self.group_arr:
            if not set(params.keys()).issubset(val.keys()):
                return 'incorrect url values'
            if self.compare_dict_values(val, params):
                self.group_users_match_params.append(val)

    def compare_dict_values(self, group_users_dict, params_url_dict):
        for key in group_users_dict.items():
            if key[0] in params_url_dict:
                if ('uid' == key[0] or 'gid' == key[0]) and (params_url_dict[key[0]] != key[1]):
                    return False
                elif isinstance(params_url_dict[key[0]], list):
                    for val in params_url_dict[key[0]]:
                        if val not in key[1]:
                            return False
                elif params_url_dict[key[0]] not in key[1]:
                    return False
        return True

    def validate_query_parameters(self, query_params):
        if len(self.valid_params) > 0:
            self.valid_params = {}

        for val in query_params.items():
            if val[1] is not None:
                self.valid_params.update({val[0]: val[1]})

    def get_single_user_from_uid(self, param_uid):
        if len(self.single_user_uid_response) > 0:
            self.single_user_uid_response = []

        self.get_passwd_users()

        for val in self.passwd_arr:
            if param_uid == val['uid']:
                #print('let match: {}'.format(val))
                self.single_user_uid_response.append(val)

        if len(self.single_user_uid_response) > 0:
            return self.single_user_uid_response
        else:
            return '404: '+param_uid+' is not found'


    def get_single_group_from_gid(self, param_gid):
        if len(self.single_group_gid_response) > 0:
            self.single_group_gid_response = []

        self.get_group_users()

        for val in self.group_arr:
            if param_gid == val['gid']:
                #print('let match: {}'.format(val))
                self.single_group_gid_response.append(val)

        if len(self.single_group_gid_response) > 0:
            return self.single_group_gid_response
        else:
            return '404: '+param_gid+' is not found'

    def get_all_groups_for_user_from_uid(self, param_uid):
        if len(self.all_groups_user_uid_response) > 0:
            self.all_groups_user_uid_response = []

        single_user_response = self.get_single_user_from_uid(param_uid)
        all_groups = self.get_group_users()

        for val in single_user_response:
            if isinstance(val, dict):
                for grp in all_groups:
                    if val['name'] in grp['members'] or val['name'] in grp['name']:
                        self.all_groups_user_uid_response.append(grp)

        return self.all_groups_user_uid_response


