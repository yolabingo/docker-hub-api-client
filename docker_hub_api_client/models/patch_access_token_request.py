from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchAccessTokenRequest")


@attr.s(auto_attribs=True)
class PatchAccessTokenRequest:
    """
    Attributes:
        token_label (Union[Unset, str]):  Example: My read only token.
        is_active (Union[Unset, bool]):
    """

    token_label: Union[Unset, str] = UNSET
    is_active: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        token_label = self.token_label
        is_active = self.is_active

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if token_label is not UNSET:
            field_dict["token_label"] = token_label
        if is_active is not UNSET:
            field_dict["is_active"] = is_active

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        token_label = d.pop("token_label", UNSET)

        is_active = d.pop("is_active", UNSET)

        patch_access_token_request = cls(
            token_label=token_label,
            is_active=is_active,
        )

        patch_access_token_request.additional_properties = d
        return patch_access_token_request

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
