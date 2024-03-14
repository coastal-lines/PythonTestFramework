import base64

from core.utils.logging_manager import desktop_logger


def load_image_as_bytearray(image_path: str) -> bytearray:
    try:
        with open(image_path, "rb") as image:
            return bytearray(image.read())
    except FileNotFoundError:
        desktop_logger.exception(f"File '{image_path}' not found.")
    except Exception as e:
        desktop_logger.exception(f"Unable to read '{image_path}' file. \n {e}")

def load_image_as_base64(image_path: str) -> str:
    try:
        with open(image_path, "rb") as img_file:
            img_bytes = img_file.read()
            encoded_img = base64.b64encode(img_bytes)
            encoded_img_str = encoded_img.decode('utf-8')

            return encoded_img_str
    except FileNotFoundError:
        desktop_logger.exception(f"File '{image_path}' not found.")
    except Exception as e:
        desktop_logger.exception(f"Unable to read '{image_path}' file. \n {e}")