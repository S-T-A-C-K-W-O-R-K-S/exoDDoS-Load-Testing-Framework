import csv

from exoddos_environment import env
from exoddos_hooks import login, logout
from exoddos_tasks import OpenReferrals, ClosedReferrals

from locust import HttpLocust, TaskSet
from locust import between
