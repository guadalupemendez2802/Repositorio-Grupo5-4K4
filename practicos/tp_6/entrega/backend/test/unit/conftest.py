import os
import sys


def pytest_configure():
    tests_dir = os.path.dirname(__file__)
    backend_root = os.path.abspath(os.path.join(tests_dir, "../.."))
    src_root = os.path.join(backend_root, "src")
    for path in (backend_root, src_root):
        if path not in sys.path:
            sys.path.insert(0, path)
