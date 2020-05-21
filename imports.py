import csv

from environment import env
from hooks import on_start_setup, on_stop_teardown
from tasks import get_inbasket, get_workzone

from locust import HttpLocust, TaskSet
from locust import between, task

from pathlib import Path
