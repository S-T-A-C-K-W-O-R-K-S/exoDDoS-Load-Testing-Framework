import csv

from environment import env
from hooks import login, logout
from tasks import referrals, employees, absences

from locust import HttpLocust, TaskSet
from locust import between, task

from pathlib import Path
