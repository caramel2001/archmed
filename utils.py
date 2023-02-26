from pathlib import Path
from os import getenv

# from base import load_env
from dotenv import load_dotenv

ROOT_DIR = Path.cwd()
print(ROOT_DIR)
load_dotenv(ROOT_DIR.joinpath(".env"))

settings = {
    "SCOPUS": getenv("SCOPUS"),
    "IEEE": getenv("IEEE"),
    "AWS_ID": getenv("AWS_ID"),
    "AWS_SECRET": getenv("AWS_SECRET"),
}

import base64
from dotenv import set_key


def base64_encode(string: str):
    return base64.encode(string)


def base64_decode(string: str):
    return base64.decode(string)


def set_env(env_path: str, key: str, value: str):
    set_key(env_path, key_to_set=key, value_to_set=value)
