from locust import tag, task, TaskSet

from tasks.reports.get_report import get_report


class Reports(TaskSet):

    @task(1)
    @tag("reports")
    def get_report_task(self):
        get_report(self, self.user.session_id, self.user.session_cookie, self.user.username, self.user.user_collaboration_id, filters="?")
    
    @task(1)  # 50% chance for the taskset to be interrupted
    @tag("reports")
    def stop_reports_taskset(self):
        self.interrupt()
