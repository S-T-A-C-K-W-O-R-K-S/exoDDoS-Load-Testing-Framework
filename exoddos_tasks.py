from exoddos_environment import env

from locust import TaskSequence
from locust import seq_task

from pathlib import Path

"""
session_file = open(Path(f"sessions/{asp_net_session_id}"),"r")
session_token = session_file.read()
session_file.close()
"""

session_token = "HOW_THE_HELL_DO_I_PASS_STATE_IN_THIS_RETARDED_PROGRAMMING_LANGUAGE?"

class OpenReferrals(TaskSequence):

    @seq_task(1)
    def do_something(self):
        print(f"first task: {session_token}")

    @seq_task(2)
    def return_to_parent(self):
        TaskSequence.interrupt(self, reschedule=True)


class ClosedReferrals(TaskSequence):

    @seq_task(1)
    def do_something(self):
        print(f"second task: {session_token}")

    @seq_task(2)
    def return_to_parent(self):
        TaskSequence.interrupt(self, reschedule=True)
