from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.get_namespace_repository_images_summary_response_statistics import (
    GetNamespaceRepositoryImagesSummaryResponseStatistics,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetNamespaceRepositoryImagesSummaryResponse")


@attr.s(auto_attribs=True)
class GetNamespaceRepositoryImagesSummaryResponse:
    """Summary information for images in a repository.

    Attributes:
        active_from (Union[Unset, str]): Time from which an image must have been pushed or pulled to be counted as
            active. Example: 2021-01-25 14:25:37.076343+00:00.
        statistics (Union[Unset, GetNamespaceRepositoryImagesSummaryResponseStatistics]):
    """

    active_from: Union[Unset, str] = UNSET
    statistics: Union[Unset, GetNamespaceRepositoryImagesSummaryResponseStatistics] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        active_from = self.active_from
        statistics: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.statistics, Unset):
            statistics = self.statistics.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active_from is not UNSET:
            field_dict["active_from"] = active_from
        if statistics is not UNSET:
            field_dict["statistics"] = statistics

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        active_from = d.pop("active_from", UNSET)

        _statistics = d.pop("statistics", UNSET)
        statistics: Union[Unset, GetNamespaceRepositoryImagesSummaryResponseStatistics]
        if isinstance(_statistics, Unset):
            statistics = UNSET
        else:
            statistics = GetNamespaceRepositoryImagesSummaryResponseStatistics.from_dict(_statistics)

        get_namespace_repository_images_summary_response = cls(
            active_from=active_from,
            statistics=statistics,
        )

        get_namespace_repository_images_summary_response.additional_properties = d
        return get_namespace_repository_images_summary_response

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
