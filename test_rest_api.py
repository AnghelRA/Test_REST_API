from pyats import aetest
from utils import Users, Posts, Comments, Todos


class ScriptCommonSetup(aetest.CommonSetup):

    @aetest.subsection
    def setup(self):
        self.parent.parameters['users'] = Users()
        self.parent.parameters['posts'] = Posts()
        self.parent.parameters['comments'] = Comments()
        self.parent.parameters['todos'] = Todos()

    @aetest.subsection
    def test_connections(self, users, posts, comments, todos):
        result1 = users.fetch_information("users")
        result2 = posts.fetch_information("posts")
        result3 = comments.fetch_information("comments")
        result4 = todos.fetch_information("todos")

        if result1.status_code != 200 or result2.status_code != 200 \
                or result3.status_code != 200 or result4.status_code != 200:
            self.failed()


class TestUser(aetest.Testcase):

    must_pass = True

    @aetest.test
    def test_create_user(self, users):
        result = users.create_user()
        if not result:
            self.failed()

        self.parent.parameters['user_id'] = result

    @aetest.test
    def test_update_user(self, users, user_id):
        result = users.update_user(user_id)
        if result.status_code != 200:
            print(result.status_code, result.content)
            self.failed()

    @aetest.test
    def test_fail_create_user(self, users):
        result = users.fail_create_user()
        if result:
            self.failed()

    @aetest.test
    def test_fail_update_user(self, users, user_id):
        result = users.fail_update_user(user_id)
        if result.status_code == 200:
            self.failed()

    @aetest.test
    def test_fail_delete_users(self, users):
        user_id = "gorila"
        result = users.delete_object("users", user_id)
        if result.status_code == 204:
            self.failed()


class TestPost(aetest.Testcase):

    must_pass = True

    @aetest.test
    def test_create_post(self, posts, user_id):
        result = posts.create_post(user_id)

        if not result:
            self.failed()

        self.parent.parameters['post_id'] = result

    @aetest.test
    def test_update_post(self, posts, post_id):
        result = posts.update_post(post_id)
        if result.status_code != 200:
            print(result.status_code, result.content)
            self.failed()

    @aetest.test
    def test_fail_create_post(self, posts):
        user_id = "banana"
        result = posts.create_post(user_id)
        if result:
            self.failed()

    @aetest.test
    def test_fail_update_post(self, posts):
        post_id = "monkey"
        result = posts.update_post(post_id)
        if result.status_code == 200:
            self.failed()

    @aetest.test
    def test_fail_delete_posts(self, posts):
        post_id = "minion"
        result = posts.delete_object("post", post_id)
        if result.status_code == 204:
            self.failed()


class TestComment(aetest.Testcase):

    must_pass = True

    @aetest.test
    def test_create_comment(self, comments, post_id):
        result = comments.create_comment(post_id)

        if not result:
            self.failed()

        self.parent.parameters['comment_id'] = result

    @aetest.test
    def test_update_comment(self, comments, comment_id):
        result = comments.update_comment(comment_id)
        if result.status_code != 200:
            print(result.status_code, result.content)
            self.failed()


class TestTodo(aetest.Testcase):

    must_pass = True

    @aetest.test
    def test_create_todo(self, todos, user_id):
        result = todos.create_todo(user_id)

        if not result:
            self.failed(result)

        self.parent.parameters['todo_id'] = result

    @aetest.test
    def test_update_todo(self, todos, todo_id):
        result = todos.update_todo(todo_id)
        if result.status_code != 200:
            print(result.status_code, result.content)
            self.failed()


class ScriptCommonCleanup(aetest.CommonCleanup):

    @aetest.subsection
    def delete_todos(self, todos, todo_id):
        result = todos.delete_object("todos", todo_id)
        if result.status_code != 204:
            self.failed(result.status_code, result.content)

    @aetest.subsection
    def delete_comments(self, comments, comment_id):
        result = comments.delete_object("comments", comment_id)
        if result.status_code != 204:
            print(result.status_code, result.content)
            self.failed()

    @aetest.subsection
    def delete_posts(self, posts, post_id):
        result = posts.delete_object("posts", post_id)
        if result.status_code != 204:
            print(result.status_code, result.content)
            self.failed()

    @aetest.subsection
    def delete_users(self, users, user_id):
        result = users.delete_object("users", user_id)
        if result.status_code != 204:
            print(result.status_code, result.content)
            self.failed()


if __name__ == '__main__':
    aetest.main()
