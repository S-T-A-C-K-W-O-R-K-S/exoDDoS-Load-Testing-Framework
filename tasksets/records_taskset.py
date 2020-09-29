from locust import SequentialTaskSet, tag, task

from tasks.records.get_document_class import get_document_class
from tasks.records.post_create_record import post_create_record
from tasks.records.get_workflow_steps import get_workflow_steps
from tasks.records.put_send_to_workflow import put_send_to_workflow


class Records(SequentialTaskSet):

    @task
    @tag("records")
    def get_document_class_task(self):
        self.document_classes = get_document_class(self)

    @task
    @tag("records")
    def post_create_record_task(self):
        if len(self.document_classes) > 0:
            self.record_id = post_create_record(self, self.document_classes)
        else:
            self.interrupt()

    @task
    @tag("records")
    def get_workflow_steps_task(self):
        if self.record_id is not None:
            self.workflow_steps = get_workflow_steps(self, self.record_id)
        else:
            self.interrupt()

    @task
    @tag("records")
    def put_send_to_workflow_task(self):
        if len(self.workflow_steps) > 0:
            put_send_to_workflow(self, self.record_id, self.workflow_steps)
        else:
            self.interrupt()

    @task
    @tag("records")
    def stop_records_taskset(self):
        self.interrupt()
