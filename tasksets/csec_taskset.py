from locust import tag, task, SequentialTaskSet

from tasks.csec.default_query import default_query
from tasks.csec.detailed_tables_view import detailed_tables_view
from tasks.csec.hierarchical_view import hierarchical_view
from tasks.csec.hierarchy_drilldown import hierarchy_drilldown
from tasks.csec.instrument_components_drilldown_bottom import instrument_components_drilldown_bottom
from tasks.csec.instrument_components_drilldown_top import instrument_components_drilldown_top
from tasks.csec.instrument_drilldown_bottom import instrument_drilldown_bottom
from tasks.csec.instrument_drilldown_top import instrument_drilldown_top


class CSEC(SequentialTaskSet):

    @task
    @tag("csec")
    def default_query_task(self):
        default_query(self)

    @task
    @tag("csec")
    def detailed_tables_view_task(self):
        detailed_tables_view(self)

    @task
    @tag("csec")
    def hierarchical_view_task(self):
        hierarchical_view(self)

    @task
    @tag("csec")
    def hierarchy_drilldown_task(self):
        hierarchy_drilldown(self)

    @task
    @tag("csec")
    def instrument_components_drilldown_bottom_task(self):
        instrument_components_drilldown_bottom(self)

    @task
    @tag("csec")
    def instrument_components_drilldown_top_task(self):
        instrument_components_drilldown_top(self)

    @task
    @tag("csec")
    def instrument_drilldown_bottom_task(self):
        instrument_drilldown_bottom(self)

    @task
    @tag("csec")
    def instrument_drilldown_top_task(self):
        instrument_drilldown_top(self)

    @task
    @tag("csec")
    def stop_query_taskset(self):
        self.interrupt()
