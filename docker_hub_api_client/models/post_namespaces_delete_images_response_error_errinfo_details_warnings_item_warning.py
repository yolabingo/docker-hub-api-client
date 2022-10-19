from enum import Enum


class PostNamespacesDeleteImagesResponseErrorErrinfoDetailsWarningsItemWarning(str, Enum):
    IS_ACTIVE = "is_active"
    CURRENT_TAG = "current_tag"

    def __str__(self) -> str:
        return str(self.value)
