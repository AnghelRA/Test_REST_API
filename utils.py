import requests
import json


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

    def update_object(self, page, json_data, id):
        response = requests.put(self.url + page + "/" + str(id), json=json_data, headers=self.headers, verify=False)
        return response

    def delete_object(self, page, id):
        response = requests.delete(self.url + page + "/" + str(id), headers=self.headers, verify=False)
        return response

    def check_created_object(self, page, json_data):
        response = self.fetch_information(page)
        site_data = response.json()
        for data in site_data:
            if json_data.items() <= data.items():
                id = data["id"]
                return id


class Users(RestUtils):

    def __init__(self):
        self.page = "users"
        self.json_data = json.load(open('user.json', 'r'))
        super().__init__()

    def create_user(self):
        self.create_object(self.page, self.json_data)
        return self.check_created_object(self.page, self.json_data)

    def update_user(self, id):
        self.json_data["email"] = "john.doe@hotmail.com"
        return self.update_object(self.page, self.json_data, id)

    def fail_update_user(self, id):
        self.json_data["gender"] = "helicopter"
        return self.update_object(self.page, self.json_data, id)


class Posts(RestUtils):

    def __init__(self):
        self.page = "posts"
        self.json_data = json.load(open('post.json', 'r'))
        super().__init__()


    def create_post(self, id):
        self.json_data["user_id"] = id
        self.create_object(self.page, self.json_data)
        return self.check_created_object(self.page, self.json_data)

    def update_post(self, id):
        self.json_data["title"] = "New title"
        return self.update_object(self.page, self.json_data, id)


class Comments(RestUtils):

    def __init__(self):
        self.page = "comments"
        self.json_data = json.load(open('comment.json', 'r'))
        super().__init__()

    def create_comment(self, id):
        self.json_data["post_id"] = id
        self.create_object(self.page, self.json_data)
        return self.check_created_object(self.page, self.json_data)

    def update_comment(self, id):
        self.json_data["email"] = "john.doe2@mail.com"
        return self.update_object(self.page, self.json_data, id)


class Todos(RestUtils):

    def __init__(self):
        self.page = "todos"
        self.json_data = json.load(open('todo.json', 'r'))
        super().__init__()

    def create_todo(self, id):
        self.json_data["user_id"] = id
        self.create_object(self.page, self.json_data)
        return self.check_created_object(self.page, self.json_data)

    def update_todo(self, id):
        self.json_data["title"] = "New title"
        return self.update_object(self.page, self.json_data, id)
    
