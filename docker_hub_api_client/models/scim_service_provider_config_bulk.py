from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ScimServiceProviderConfigBulk")


@attr.s(auto_attribs=True)
class ScimServiceProviderConfigBulk:
    """
    Attributes:
        supported (Union[Unset, bool]):
        max_operations (Union[Unset, int]):
        max_payload_size (Union[Unset, int]):
    """

    supported: Union[Unset, bool] = UNSET
    max_operations: Union[Unset, int] = UNSET
    max_payload_size: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        supported = self.supported
        max_operations = self.max_operations
        max_payload_size = self.max_payload_size

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if supported is not UNSET:
            field_dict["supported"] = supported
        if max_operations is not UNSET:
            field_dict["maxOperations"] = max_operations
        if max_payload_size is not UNSET:
            field_dict["maxPayloadSize"] = max_payload_size

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        supported = d.pop("supported", UNSET)

        max_operations = d.pop("maxOperations", UNSET)

        max_payload_size = d.pop("maxPayloadSize", UNSET)

        scim_service_provider_config_bulk = cls(
            supported=supported,
            max_operations=max_operations,
            max_payload_size=max_payload_size,
        )

        scim_service_provider_config_bulk.additional_properties = d
        return scim_service_provider_config_bulk

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
