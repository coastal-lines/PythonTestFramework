import subprocess
import time

from core.utils.config_manager import ConfigUtils
from core.utils.os import process_manager

wait_time = int(ConfigUtils.get_config().mobile.emulator_loading_timeout)


def start_emulator(command: str):
    subprocess.Popen(command,
                    shell=True,
                    stdin=subprocess.PIPE,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE)

def waiting_android_emulator_is_started(emulator_port_number:str):
    global wait_time

    start_time = time.time()
    while True:
        output = process_manager.start_process("adb devices", start_in_new_process=False, is_captured_output=True)
        str_output = str(output.stdout)
        if ("List of devices attached" in str_output
                #and "emulator-5554" in str_output
                and emulator_port_number in str_output
                and "offline" not in str_output):
            break
        else:
            if time.time() - start_time >= wait_time:
                raise TimeoutError

        time.sleep(3)

def waiting_android_system_is_loaded():
    global wait_time

    start_time = time.time()
    while True:
        output = process_manager.start_process("adb shell getprop sys.boot_completed", start_in_new_process=False, is_captured_output=True)
        if ("1" in str(output.stdout)):
            break
        else:
            if time.time() - start_time >= wait_time:
                raise TimeoutError

        time.sleep(3)

def waiting_android_emulator_is_ready_for_test(emulator_process_name: str, emulator_port_number: str):
    process_manager.wait_process(emulator_process_name)
    waiting_android_emulator_is_started(emulator_port_number)
    waiting_android_system_is_loaded()
