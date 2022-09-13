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
        result1 = users.fetch_users()
        result2 = posts.fetch_posts()
        result3 = comments.fetch_comments()
        result4 = todos.fetch_todos()

        if result1.status_code != 200 or result2.status_code != 200 \
                or result3.status_code != 200 or result4.status_code != 200:
            self.failed()


class TestCreateUser(aetest.Testcase):

    must_pass = True

    @aetest.test
    def test_create_user(self, users):
        result = users.create_user()
        if not result:
            self.failed()

        self.parent.parameters['user_id'] = result

class TestCreatePost(aetest.Testcase):

    must_pass = True

    @aetest.test
    def test_create_post(self, posts, user_id):
        result = posts.create_post(user_id)

        if not result:
            self.failed()

        self.parent.parameters['post_id'] = result

class TestCreateComment(aetest.Testcase):

    must_pass = True

    @aetest.test
    def test_create_post(self, comments, post_id):
        result = comments.create_comment(post_id)

        if not result:
            self.failed()

        self.parent.parameters['comment_id'] = result

class TodoCreateComment(aetest.Testcase):

    must_pass = True

    @aetest.test
    def test_create_post(self, todos, user_id):
        result = todos.create_todo(user_id)

        if not result:
            self.failed()

        self.parent.parameters['todo_id'] = result

class ScriptCommonCleanup(aetest.CommonCleanup):

    @aetest.subsection
    def delete_users(self, users, user_id):
        result = users.delete_user(user_id)
        if not result:
            self.failed(result)

    @aetest.subsection
    def delete_posts(self, posts, post_id):
        result = posts.delete_post(post_id)
        if not result:
            self.failed(result)

    @aetest.subsection
    def delete_comments(self, comments, comment_id):
        result = comments.delete_comment(comment_id)
        if not result:
            self.failed(result)

    @aetest.subsection
    def delete_todos(self, todos, todo_id):
        result = todos.delete_todo(todo_id)
        if not result:
            self.failed(result)

if __name__ == '__main__':
    aetest.main()
