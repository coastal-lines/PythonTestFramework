import os


ROOT_FOLDER_NAME = "PythonTestFramework"

def get_project_path() -> str:
    return os.path.join(os.path.realpath(__file__).split(ROOT_FOLDER_NAME)[0], ROOT_FOLDER_NAME)

def read_resource(user_resource: str) -> str:
    return os.path.join(get_project_path(), user_resource)