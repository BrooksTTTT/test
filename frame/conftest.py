import os
import subprocess
import signal

import pytest

# @pytest.fixture(scope="module", autouse=True)
# def record_video():
#     command = "scrcpy --record tmp.mp4"
#     p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
#     print(p)
#     yield
#     os.kill(p.pid, signal.SIGINT)
