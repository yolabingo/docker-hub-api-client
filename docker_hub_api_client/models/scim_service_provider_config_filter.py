from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ScimServiceProviderConfigFilter")


@attr.s(auto_attribs=True)
class ScimServiceProviderConfigFilter:
    """
    Attributes:
        supported (Union[Unset, bool]):  Example: True.
        max_results (Union[Unset, int]):  Example: 99999.
    """

    supported: Union[Unset, bool] = UNSET
    max_results: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        supported = self.supported
        max_results = self.max_results

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if supported is not UNSET:
            field_dict["supported"] = supported
        if max_results is not UNSET:
            field_dict["maxResults"] = max_results

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        supported = d.pop("supported", UNSET)

        max_results = d.pop("maxResults", UNSET)

        scim_service_provider_config_filter = cls(
            supported=supported,
            max_results=max_results,
        )

        scim_service_provider_config_filter.additional_properties = d
        return scim_service_provider_config_filter

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
