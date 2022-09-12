class RestUtils:
    def __init__(self):
        self.url = "https://gorest.co.in/public/v2/"
        self.headers = {
                        "Accept": "application/json",
                        "Content-Type": "application/json",
                        "Authorization": "Bearer " + "f34a54cb0d65306812337c51922d6839bc60c50f1147a62c45f3732d49de7fbd"
                       }


    def fetch_information(self, page):
        response = requests.get(self.url + page, headers=self.headers, verify=False)
        return response

    def create_object(self, page, json_data):
        response = requests.post(self.url + page, json=json_data, headers=self.headers, verify=False)
        return response

    def delete_object(self, page, id):
        response = requests.delete(self.url + page + "/" + id, headers=self.headers, verify=False)
        return response

    def check_created_object(self, page, json_data):
        list_id = []
        response = self.fetch_information(page)
        site_data = response.json()
        for data in site_data:
            if json_data.items() <= data.items():
                id = data["id"]
                list_id.append(str(id))
        return list_id
