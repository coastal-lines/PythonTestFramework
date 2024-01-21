import os


ROOT_FOLDER_NAME = "PythonTestFramework"

def get_project_path() -> str:
    return os.path.join(os.path.realpath(__file__).split(ROOT_FOLDER_NAME)[0], ROOT_FOLDER_NAME)

def get_resource_path(user_resource: str) -> str:
    return os.path.join(get_project_path(), user_resource)

def screenshot_path_for_logs(pytest_node):
    log_files_path = ""

    if ("desktop" in pytest_node.location[0]):
        log_files_path = os.path.join(get_project_path(), "resources\\logs\\desktop\\screenshots")
    elif ("web_tests" in pytest_node.location[0]):
        log_files_path = os.path.join(get_project_path(), "resources\\logs\\web\\screenshots")

    screenshot_path = f"{log_files_path}\\{pytest_node.name}.png"

    return screenshot_path