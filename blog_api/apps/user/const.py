json_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "hobby": {
            "type": "array",
            "minItems": 1,
            "maxItems": 3,
            "items": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "minLength": 1,
                        "maxLength": 8
                    },
                    "detail": {
                        "type": "string",
                        "minLength": 1,
                        "maxLength": 255
                    }
                },
                "additionalProperties": False,
                "required": [
                    "name",
                    "detail"
                ]
            }
        },
        "media": {
            "type": "object",
            "properties": {
                "github": {
                    "type": "string",
                    "minLength": 1,
                },
                "tiktok": {
                    "type": "string",
                    "minLength": 1,
                },
                "bilibili": {
                    "type": "string",
                    "minLength": 1,
                },
                "csdn": {
                    "type": "string",
                    "minLength": 1,
                }
            },
            "additionalProperties": False,
            "required": [
                "github",
                "tiktok",
                "bilibili",
                "csdn"
            ]
        }
    },
    "additionalProperties": False,
    "required": [
        "hobby",
        "media"
    ]
}