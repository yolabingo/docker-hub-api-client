from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetNamespaceRepositoryImagesSummaryResponseStatistics")


@attr.s(auto_attribs=True)
class GetNamespaceRepositoryImagesSummaryResponseStatistics:
    """
    Attributes:
        total (Union[Unset, int]): Number of images in this repository. Example: 3.
        active (Union[Unset, int]): Number of images counted as active in this repository. Example: 2.
        inactive (Union[Unset, int]): Number of images counted as inactive in this repository. Example: 1.
    """

    total: Union[Unset, int] = UNSET
    active: Union[Unset, int] = UNSET
    inactive: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total = self.total
        active = self.active
        inactive = self.inactive

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total is not UNSET:
            field_dict["total"] = total
        if active is not UNSET:
            field_dict["active"] = active
        if inactive is not UNSET:
            field_dict["inactive"] = inactive

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        total = d.pop("total", UNSET)

        active = d.pop("active", UNSET)

        inactive = d.pop("inactive", UNSET)

        get_namespace_repository_images_summary_response_statistics = cls(
            total=total,
            active=active,
            inactive=inactive,
        )

        get_namespace_repository_images_summary_response_statistics.additional_properties = d
        return get_namespace_repository_images_summary_response_statistics

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
