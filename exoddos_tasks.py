from locust import TaskSequence
from locust import seq_task


class OpenReferrals(TaskSequence):

    @seq_task(1)
    def do_something(self):
        print("first task: FIND_A_WAY_TO_PASS_THE_SESSION_TOKEN_TO_THIS_FUNCTION")

    @seq_task(2)
    def return_to_parent(self):
        TaskSequence.interrupt(self, reschedule=True)


class ClosedReferrals(TaskSequence):

    @seq_task(1)
    def do_something(self):
        print("second task")

    @seq_task(2)
    def return_to_parent(self):
        TaskSequence.interrupt(self, reschedule=True)
