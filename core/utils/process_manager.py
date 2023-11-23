import platform
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
