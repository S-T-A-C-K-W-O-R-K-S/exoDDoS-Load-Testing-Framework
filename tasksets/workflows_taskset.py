from locust import tag, task, TaskSet

from tasks.workflows.get_workflow import get_workflow


class Workflows(TaskSet):

    @task(1)
    @tag("workflows")
    def get_workflow_task(self):
        get_workflow(self, self.user.session_id, self.user.session_cookie, self.user.username, self.user.user_collaboration_id)
    
    @task(1)  # 50% chance for the taskset to be interrupted
    @tag("workflows")
    def stop_workflows_taskset(self):
        self.interrupt()
