from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RestrictedImages")


@attr.s(auto_attribs=True)
class RestrictedImages:
    """
    Attributes:
        enabled (Union[Unset, bool]): Whether or not to restrict image usage for users in the organization. Example:
            True.
        allow_official_images (Union[Unset, bool]): Allow usage of official images if "enabled" is `true`. Example:
            True.
        allow_verified_publishers (Union[Unset, bool]): Allow usage of verified publisher images if "enabled" is `true`.
            Example: True.
    """

    enabled: Union[Unset, bool] = UNSET
    allow_official_images: Union[Unset, bool] = UNSET
    allow_verified_publishers: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enabled = self.enabled
        allow_official_images = self.allow_official_images
        allow_verified_publishers = self.allow_verified_publishers

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if allow_official_images is not UNSET:
            field_dict["allow_official_images"] = allow_official_images
        if allow_verified_publishers is not UNSET:
            field_dict["allow_verified_publishers"] = allow_verified_publishers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        enabled = d.pop("enabled", UNSET)

        allow_official_images = d.pop("allow_official_images", UNSET)

        allow_verified_publishers = d.pop("allow_verified_publishers", UNSET)

        restricted_images = cls(
            enabled=enabled,
            allow_official_images=allow_official_images,
            allow_verified_publishers=allow_verified_publishers,
        )

        restricted_images.additional_properties = d
        return restricted_images

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
