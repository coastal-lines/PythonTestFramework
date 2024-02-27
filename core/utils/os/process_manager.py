import platform
import subprocess
import time

import psutil


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
            proc.terminate()

def start_process(command: str):
    """
    'shell=True' - support shell features like '&', '|', redirect streaming, etc.
    """
    subprocess.run(command, shell=True)

def start_process_and_wait(command: str, process_name:str, wait_time=20):
    start_process(command)

    start_time = time.time()
    while True:
        if (check_process_existed(process_name)):
            break
        else:
            if time.time() - start_time >= wait_time:
                print(f"Application '{process_name}' was not started after {timeout} seconds.")
                break

        time.sleep(3)

