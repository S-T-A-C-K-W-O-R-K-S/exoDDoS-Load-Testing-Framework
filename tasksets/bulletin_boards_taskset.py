from locust import tag, task, TaskSet

from tasks.bulletin_boards.get_bulletin_board_list import get_bulletin_board_list
from tasks.bulletin_boards.get_bulletin_board_tree import get_bulletin_board_tree


class BulletinBoards(TaskSet):

    @task(1)
    @tag("bb")
    def get_bulletin_board_list_task(self):
        get_bulletin_board_list(self, self.user.session_id, self.user.session_cookie, self.user.username, self.user.user_collaboration_id)

    @task(1)
    @tag("bb")
    def get_bulletin_board_tree_task(self):
        get_bulletin_board_tree(self, self.user.session_id, self.user.session_cookie, self.user.username, self.user.user_collaboration_id)
    
    @task(2)  # 50% chance for the taskset to be interrupted
    @tag("bb")
    def stop_bulletin_boards_taskset(self):
        self.interrupt()
