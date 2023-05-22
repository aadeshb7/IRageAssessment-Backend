import os
from configparser import RawConfigParser


def get_configparser():
    config = RawConfigParser()
    config.read(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'config.properties'))
    return config