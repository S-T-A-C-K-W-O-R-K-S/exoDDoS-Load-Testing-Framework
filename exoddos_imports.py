import csv

from exoddos_environment import env
from exoddos_hooks import create_temp_directory, delete_temp_directory, login, logout
from exoddos_tasks import OpenReferrals, ClosedReferrals

from locust import HttpLocust, TaskSet
from locust import between

from pathlib import Path
