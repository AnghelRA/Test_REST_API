from pyats import aetest
import json
from utils import RestUtils

class TestRest(aetest.Testcase):
    @aetest.setup
    def setup(self):
        rest_util_obj = RestUtils()
        self.parent.parameters['rest_utils_obj'] = rest_util_obj
        self.json_data = json.load(open('user.json', 'r'))
        self.page = "users"

    @aetest.test
    def test_fetch(self, rest_utils_obj):
        result = rest_utils_obj.fetch_information("users")
        if result.status_code != 200:
            self.failed()

    @aetest.test
    def test_create_object(self, rest_utils_obj):
        result = rest_utils_obj.create_object(self.page, self.json_data)
        if result.status_code != 201:
            self.failed()

    @aetest.test
    def test_object_created(self, rest_utils_obj):
        self.list_id = rest_utils_obj.check_created_object(self.page, self.json_data)
        if not self.list_id:
            self.failed()

    @aetest.test
    def test_delete_object(self, rest_utils_obj):
        self.id = self.list_id[0]
        result = rest_utils_obj.delete_object(self.page, self.id)
        if result.status_code != 204:
           self.failed(result.status_code)

    @aetest.cleanup
    def cleanup(self, rest_utils_obj):
        if not self.list_id:
            for id in self.list_id:
                rest_utils_obj.delete_object(self.page, id)
        del self.id
        del self.json_data


if __name__ == '__main__':
    aetest.main()
