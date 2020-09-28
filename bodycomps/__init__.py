# This file is imported automagically when importing the entire module
import os.path

try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import SafeConfigParser as ConfigParser

config = ConfigParser()

DEFAULT_CONFIG_FILES = []

LOCAL_CONFIG_PATH = os.path.join(os.path.dirname(), "settings.conf")

config.read(DEFAULT_CONFIG_FILES + [LOCAL_CONFIG_PATH])