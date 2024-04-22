import base64
import io

from PIL import Image

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
        raise FileNotFoundError
    except Exception as e:
        desktop_logger.exception(f"Unable to read '{image_path}' file. \n {e}")
        raise Exception

def save_bytes_as_png_image(image_bytes: bytes, image_path: str):
    decoded_bytes = None

    try:
        decoded_bytes = base64.b64decode(image_bytes)
    except base64.binascii.Error as ex:
        desktop_logger.exception(f"Invalid base64-encoded image bytes for '{image_path}'. \n {ex}")

    if decoded_bytes is not None:
        try:
            with io.BytesIO(decoded_bytes) as bytes_io:
                img = Image.open(bytes_io)
                img.save(image_path, format="PNG")
        except IOError as ex:
            desktop_logger.exception(f"Unable to save '{image_path}' file. \n {ex}")

def save_base64_as_png_image(image_base64: str, image_path: str):
    binary_data = None

    try:
        binary_data = base64.b64decode(image_base64)
    except Exception as ex:
        desktop_logger.exception(f"Invalid converting base64 into bytes for '{image_path}'. \n {ex}")

    if binary_data is not None:
        try:
            with open(image_path, "wb") as f:
                f.write(binary_data)
        except IOError as ex:
            desktop_logger.exception(f"Unable to save '{image_path}' file. \n {ex}")