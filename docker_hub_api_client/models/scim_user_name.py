from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ScimUserName")


@attr.s(auto_attribs=True)
class ScimUserName:
    """
    Attributes:
        given_name (Union[Unset, str]):  Example: Jon.
        family_name (Union[Unset, str]):  Example: Snow.
    """

    given_name: Union[Unset, str] = UNSET
    family_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        given_name = self.given_name
        family_name = self.family_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if given_name is not UNSET:
            field_dict["givenName"] = given_name
        if family_name is not UNSET:
            field_dict["familyName"] = family_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        given_name = d.pop("givenName", UNSET)

        family_name = d.pop("familyName", UNSET)

        scim_user_name = cls(
            given_name=given_name,
            family_name=family_name,
        )

        scim_user_name.additional_properties = d
        return scim_user_name

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
