import subprocess
import pytest
def _imp():

    subprocess.run(["python", "-c" "'import weldx'"])
def test_imp(benchmark):
    benchmark(_imp)
