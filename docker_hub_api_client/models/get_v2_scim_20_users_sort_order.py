from enum import Enum


class GetV2Scim20UsersSortOrder(str, Enum):
    ASCENDING = "ascending"
    DESCENDING = "descending"

    def __str__(self) -> str:
        return str(self.value)
