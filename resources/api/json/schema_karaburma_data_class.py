from dataclasses import dataclass


@dataclass
class SchemaKaraburmaResponseDataClass:
    simple_element = {
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

    button_elements_only = {
        "w": {"type": "integer", "required": True},
        "h": {"type": "integer", "required": True},
        "elements": {
            "type": "list",
            "schema": {
                "type": "dict",
                "schema": {
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
            }
        },
        "listbox_elements": {"type": "list"},
        "table_elements": {"type": "list"},
        "debug_screenshot": {"type": "string", "required": True}
    }

    all_elements = {
        "type": "object",
        "properties": {
            "w": {"type": "integer"},
            "h": {"type": "integer"},
            "elements": {
                "type": "array",
                "items": {
                    "id": {"type": "string"},
                    "x": {"type": "integer"},
                    "y": {"type": "integer"},
                    "w": {"type": "integer"},
                    "h": {"type": "integer"},
                    "label": {"type": "string"},
                    "prediction": {"type": "string"},
                    "orig_img_base64": {"type": "string"},
                    "text": {"type": "string"}
                },
                "required": ["id", "x", "y", "w", "h", "label", "prediction", "orig_img_base64", "text"]
            },
            "listbox_elements": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string"},
                        "x": {"type": "integer"},
                        "y": {"type": "integer"},
                        "w": {"type": "integer"},
                        "h": {"type": "integer"},
                        "label": {"type": "string"},
                        "prediction": {"type": "string"},
                        "orig_img_base64": {"type": "string"},
                        "text": {"type": "string"},
                        "v_scroll": {
                            "type": "object",
                            "properties": {
                                "id": {"type": "string"},
                                "x": {"type": "integer"},
                                "y": {"type": "integer"},
                                "w": {"type": "integer"},
                                "h": {"type": "integer"},
                                "label": {"type": "string"},
                                "prediction": {"type": "string"},
                                "orig_img_base64": {"type": "string"},
                                "first_button": {
                                    "type": "object",
                                    "properties": {
                                        "centre_x": {"type": "integer"},
                                        "centre_y": {"type": "integer"}
                                    },
                                    "required": ["centre_x", "centre_y"]
                                },
                                "second_button": {
                                    "type": "object",
                                    "properties": {
                                        "centre_x": {"type": "integer"},
                                        "centre_y": {"type": "integer"}
                                    },
                                    "required": ["centre_x", "centre_y"]
                                }
                            },
                            "required": ["id", "x", "y", "w", "h", "label", "prediction", "orig_img_base64",
                                         "first_button",
                                         "second_button"]
                        },
                        "full_img_base64": {"type": "string"},
                        "full_listbox": {
                            "type": "object",
                            "properties": {
                                "id": {"type": "string"},
                                "x": {"type": "integer"},
                                "y": {"type": "integer"},
                                "w": {"type": "integer"},
                                "h": {"type": "integer"},
                                "label": {"type": "string"},
                                "prediction": {"type": "string"},
                                "orig_img_base64": {"type": "string"},
                                "text": {"type": "string"},
                                "full_img_base64": {"type": "string"}
                            },
                            "required": ["id", "x", "y", "w", "h", "label", "prediction", "orig_img_base64", "text",
                                         "full_img_base64"]
                        }
                    },
                    "required": ["id", "x", "y", "w", "h", "label", "prediction", "orig_img_base64", "text", "v_scroll",
                                 "full_listbox"]
                }
            },
            "table_elements": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string"},
                        "x": {"type": "integer"},
                        "y": {"type": "integer"},
                        "w": {"type": "integer"},
                        "h": {"type": "integer"},
                        "label": {"type": "string"},
                        "prediction": {"type": "string"},
                        "orig_img_base64": {"type": "string"},
                        "v_scroll": {
                            "type": "object",
                            "properties": {
                                "id": {"type": "string"},
                                "x": {"type": "integer"},
                                "y": {"type": "integer"},
                                "w": {"type": "integer"},
                                "h": {"type": "integer"},
                                "label": {"type": "string"},
                                "prediction": {"type": "string"},
                                "orig_img_base64": {"type": "string"},
                                "first_button": {
                                    "type": "object",
                                    "properties": {
                                        "centre_x": {"type": "integer"},
                                        "centre_y": {"type": "integer"}
                                    },
                                    "required": ["centre_x", "centre_y"]
                                },
                                "second_button": {
                                    "type": "object",
                                    "properties": {
                                        "centre_x": {"type": "integer"},
                                        "centre_y": {"type": "integer"}
                                    },
                                    "required": ["centre_x", "centre_y"]
                                }
                            },
                            "required": ["id", "x", "y", "w", "h", "label", "prediction", "orig_img_base64",
                                         "first_button",
                                         "second_button"]
                        },
                        "h_scroll": {
                            "type": "object",
                            "properties": {
                                "id": {"type": "string"},
                                "x": {"type": "integer"},
                                "y": {"type": "integer"},
                                "w": {"type": "integer"},
                                "h": {"type": "integer"},
                                "label": {"type": "string"},
                                "prediction": {"type": "string"},
                                "orig_img_base64": {"type": "string"},
                                "first_button": {
                                    "type": "object",
                                    "properties": {
                                        "centre_x": {"type": "integer"},
                                        "centre_y": {"type": "integer"}
                                    },
                                    "required": ["centre_x", "centre_y"]
                                },
                                "second_button": {
                                    "type": "object",
                                    "properties": {
                                        "centre_x": {"type": "integer"},
                                        "centre_y": {"type": "integer"}
                                    },
                                    "required": ["centre_x", "centre_y"]
                                }
                            },
                            "required": ["id", "x", "y", "w", "h", "label", "prediction", "orig_img_base64",
                                         "first_button",
                                         "second_button"]
                        },
                        "cells": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "centre_x": {"type": "integer"},
                                    "centre_y": {"type": "integer"},
                                    "text": {"type": "string"},
                                    "address": {
                                        "type": "array",
                                        "items": {"type": "integer"}
                                    }
                                },
                                "required": ["centre_x", "centre_y", "text", "address"]
                            }
                        },
                        "full_table": {
                            "type": "object",
                            "properties": {
                                "id": {"type": "string"},
                                "x": {"type": "integer"},
                                "y": {"type": "integer"},
                                "w": {"type": "integer"},
                                "h": {"type": "integer"},
                                "label": {"type": "string"},
                                "prediction": {"type": "string"},
                                "orig_img_base64": {"type": "string"},
                                "cells": {
                                    "type": "array",
                                    "items": {
                                        "type": "object",
                                        "properties": {
                                            "centre_x": {"type": "integer"},
                                            "centre_y": {"type": "integer"},
                                            "text": {"type": "string"},
                                            "address": {
                                                "type": "array",
                                                "items": {"type": "integer"}
                                            }
                                        },
                                        "required": ["centre_x", "centre_y", "text", "address"]
                                    }
                                }
                            },
                            "required": ["id", "x", "y", "w", "h", "label", "prediction", "orig_img_base64", "cells"]
                        }
                    },
                    "required": ["id", "x", "y", "w", "h", "label", "prediction", "orig_img_base64", "v_scroll",
                                 "h_scroll",
                                 "cells", "full_table"]
                }
            },
            "debug_screenshot": "string"
        },
        "required": ["w", "h", "elements", "listbox_elements", "table_elements", "debug_screenshot"]
    }