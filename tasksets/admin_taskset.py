from locust import SequentialTaskSet, tag, task, TaskSet, user

from environment.exoddos import exoddos

from tasks.admin.get_admin_section import get_admin_section
from tasks.admin.get_user_settings import get_user_settings
from tasks.admin.get_group_settings import get_group_settings
from tasks.admin.get_organisation_settings import get_organisation_settings
from tasks.admin.get_collaboration_preferences import get_collaboration_preferences
from tasks.admin.get_organisation_preferences import get_organisation_preferences


class Admin(SequentialTaskSet):

    @task
    @tag("admin")
    def get_admin_section_task(self):
        if self.user.has_elevated_privileges is not False:
            self.user.has_elevated_privileges = get_admin_section(self)
        else:
            self.interrupt()

    @task
    @tag("admin")
    class AdminTasks(TaskSet):

        @task(3)
        @tag("admin")
        def get_user_settings_task(self):
            if self.user.has_elevated_privileges:
                get_user_settings(self, top=exoddos.results)
            else:
                self.interrupt()

        @task(3)
        @tag("admin")
        def get_group_settings_task(self):
            if self.user.has_elevated_privileges:
                get_group_settings(self, top=exoddos.results)
            else:
                self.interrupt()

        @task(3)
        @tag("admin")
        def get_organisation_settings_task(self):
            if self.user.has_elevated_privileges:
                get_organisation_settings(self, top=exoddos.results)
            else:
                self.interrupt()

        @task(3)
        @tag("admin")
        def get_collaboration_preferences_task(self):
            if self.user.has_elevated_privileges:
                get_collaboration_preferences(self)
            else:
                self.interrupt()

        @task(3)
        @tag("admin")
        def get_organisation_preferences_task(self):
            if self.user.has_elevated_privileges:
                get_organisation_preferences(self)
            else:
                self.interrupt()

        @task(5)  # 25% chance for the taskset to be interrupted
        @tag("admin")
        def stop_admin_tasks_taskset(self):
            self.interrupt()

    @task  
    @tag("admin")
    def stop_admin_taskset(self):
        self.interrupt()
