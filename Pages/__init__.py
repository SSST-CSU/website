from django.apps import AppConfig
import os

default_app_config = 'Pages.PrimaryBlogConfig'

VERBOSE_APP_NAME = '01-页面管理系统'


def get_current_app_name(_file):
    return os.path.split(os.path.dirname(_file))[-1]


class PrimaryBlogConfig(AppConfig):
    name = get_current_app_name(__file__)
    verbose_name = VERBOSE_APP_NAME