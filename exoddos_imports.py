import csv

from exoddos_environment import env
from exoddos_hooks import login, logout
from exoddos_tasks import open_referrals, closed_referrals

from locust import HttpLocust, TaskSet
from locust import between, task

from pathlib import Path
