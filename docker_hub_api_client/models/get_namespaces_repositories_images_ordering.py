from enum import Enum


class GetNamespacesRepositoriesImagesOrdering(str, Enum):
    LAST_ACTIVITY = "last_activity"
    VALUE_1 = "-last_activity"
    DIGEST = "digest"
    VALUE_3 = "-digest"

    def __str__(self) -> str:
        return str(self.value)
