from enum import Enum


class PostNamespacesDeleteImagesRequestIgnoreWarningsItemWarning(str, Enum):
    IS_ACTIVE = "is_active"
    CURRENT_TAG = "current_tag"

    def __str__(self) -> str:
        return str(self.value)
