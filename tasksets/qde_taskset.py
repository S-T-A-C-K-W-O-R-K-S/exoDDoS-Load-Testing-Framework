from locust import tag, task, TaskSet

from tasks.qde.get_qde import get_qde


class QDE(TaskSet):

    @task(1)
    @tag("qde")
    def get_qde_task(self):
        get_qde(self, self.user.session_id, self.user.session_cookie, self.user.username, self.user.user_collaboration_id)
    
    @task(1)  # 50% chance for the taskset to be interrupted
    @tag("qde")
    def stop_qde_taskset(self):
        self.interrupt()
