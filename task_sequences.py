from locust import TaskSequence
from locust import seq_task


class FirstTaskSequence(TaskSequence):

    @seq_task(1)
    def do_something(self):
        print("1.1")

    @seq_task(2)
    def do_something_else(self):
        print("1.2")

    @seq_task(3)
    def return_to_parent(self):
        TaskSequence.interrupt(self, reschedule=True)


class SecondTaskSequence(TaskSequence):

    @seq_task(1)
    def do_something(self):
        print("2.1")

    @seq_task(2)
    def do_something_else(self):
        print("2.2")

    @seq_task(3)
    def return_to_parent(self):
        TaskSequence.interrupt(self, reschedule=True)
