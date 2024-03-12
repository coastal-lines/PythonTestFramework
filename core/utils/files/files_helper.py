from core.utils.logging_manager import desktop_logger


def load_image_as_bytearray(image_path: str) -> bytearray:
    try:
        with open(image_path, "rb") as image:
            return bytearray(image.read())
    except FileNotFoundError:
        desktop_logger.exception(f"File '{image_path}' not found.")
    except Exception as e:
        desktop_logger.exception(f"Unable to read '{image_path}' file. \n {e}")