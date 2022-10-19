from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ScimEmail")


@attr.s(auto_attribs=True)
class ScimEmail:
    """
    Attributes:
        value (Union[Unset, str]):  Example: jon.snow@docker.com.
        display (Union[Unset, str]):  Example: jon.snow@docker.com.
        primary (Union[Unset, bool]):  Example: True.
    """

    value: Union[Unset, str] = UNSET
    display: Union[Unset, str] = UNSET
    primary: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        value = self.value
        display = self.display
        primary = self.primary

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if value is not UNSET:
            field_dict["value"] = value
        if display is not UNSET:
            field_dict["display"] = display
        if primary is not UNSET:
            field_dict["primary"] = primary

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        value = d.pop("value", UNSET)

        display = d.pop("display", UNSET)

        primary = d.pop("primary", UNSET)

        scim_email = cls(
            value=value,
            display=display,
            primary=primary,
        )

        scim_email.additional_properties = d
        return scim_email

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
