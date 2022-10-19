from enum import Enum


class ScimSchemaAttributeType(str, Enum):
    STRING = "string"
    BOOLEAN = "boolean"
    COMPLEX = "complex"

    def __str__(self) -> str:
        return str(self.value)
