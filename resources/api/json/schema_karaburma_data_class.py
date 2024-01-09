from dataclasses import dataclass


@dataclass
class SchemaKaraburmaDataClass:
    SIMPLE_ELEMENT = {
        "id": {"type": "string", "required": True},
        "x": {"type": "integer", "required": True},
        "y": {"type": "integer", "required": True},
        "w": {"type": "integer", "required": True},
        "h": {"type": "integer", "required": True},
        "label": {"type": "string", "required": True},
        "prediction": {"type": "string", "required": True},
        "orig_img_base64": {"type": "string", "required": True},
        "text": {"type": "string", "required": True}
    }