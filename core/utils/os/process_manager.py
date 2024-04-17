import platform
import subprocess
import time
import os
from typing import Union

import psutil

from utils.logging_manager import desktop_logger


def check_platform_for_process(func):
    def wrapper(process_name):
        if (platform.system() == 'Windows'):
            process_name += ".exe"

        return func(process_name)
    return wrapper

@check_platform_for_process
def check_process_existed(process_name):
    for process in psutil.process_iter():
        if process.name() == process_name:
            return True

    return False

@check_platform_for_process
def stop_process(process_name):
    for proc in psutil.process_iter():
        if proc.name() == process_name:
            try:
                proc.terminate()
            except Exception:
                desktop_logger.exception(f"Application '{process_name}' was not closed correctly.")

def start_process(command: str, start_in_new_process=True, is_captured_output=False) -> Union[str, bytes]:
    result = ""

    """
    'shell=True' - support shell features like '&', '|', redirect streaming, etc.
    """
    if start_in_new_process:
        subprocess.Popen(command, shell=True)
    else:
        result = subprocess.run(command, shell=True, capture_output=is_captured_output)

    return result

def wait_process(process_name:str, wait_time=20):
    start_time = time.time()
    while True:
        if (check_process_existed(process_name)):
            break
        else:
            if time.time() - start_time >= wait_time:
                desktop_logger.exception(f"Application '{process_name}' was not started after {wait_time} seconds.")
                raise TimeoutError

        time.sleep(3)

def start_process_and_wait(command: str, process_name:str, wait_time=20):
    start_process(command, True)
    wait_process(process_name, wait_time)

def start_python_application_with_venv(work_dir: str, main_script_path: str, args: list):
    os.chdir(work_dir)
    os.environ['PYTHONPATH'] = os.getcwd()

    python_executable = f'{work_dir}/venv/Scripts/python.exe'
    script_path = f'{work_dir}\\{main_script_path}'

    process = subprocess.Popen([python_executable, script_path] + args, stdout=None, stderr=None, stdin=None, close_fds=True, shell=True)

    return process
