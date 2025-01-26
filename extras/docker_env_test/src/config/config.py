import os


class Config:
    HOME = os.environ["HOME"]
    API_KEY = os.environ["API_KEY"]
    BOOL_VAR = os.environ["BOOL_VAR"] == "true"
    FROM_ENV_FILE = os.environ["FROM_ENV_FILE"]
