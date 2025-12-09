import os

os.environ.setdefault("USE_FAKE_ASSISTANT", "1")
os.environ.setdefault("QDRANT_IN_MEMORY", "1")
os.environ.setdefault("TEST_USE_SQLITE", "1")

from .settings import *  # noqa

PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]

ROOT_URLCONF = "app.urlconf_testing"
