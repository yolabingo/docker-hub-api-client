from enum import Enum


class PostNamespacesDeleteImagesResponseErrorErrinfoDetailsErrorsItemError(str, Enum):
    NOT_FOUND = "not_found"
    UNAUTHORIZED = "unauthorized"
    CHILD_MANIFEST = "child_manifest"

    def __str__(self) -> str:
        return str(self.value)
