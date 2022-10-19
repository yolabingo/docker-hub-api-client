from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.restricted_images import RestrictedImages
from ..types import UNSET, Unset

T = TypeVar("T", bound="OrgSettings")


@attr.s(auto_attribs=True)
class OrgSettings:
    """
    Attributes:
        restricted_images (Union[Unset, RestrictedImages]):
    """

    restricted_images: Union[Unset, RestrictedImages] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        restricted_images: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.restricted_images, Unset):
            restricted_images = self.restricted_images.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if restricted_images is not UNSET:
            field_dict["restricted_images"] = restricted_images

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _restricted_images = d.pop("restricted_images", UNSET)
        restricted_images: Union[Unset, RestrictedImages]
        if isinstance(_restricted_images, Unset):
            restricted_images = UNSET
        else:
            restricted_images = RestrictedImages.from_dict(_restricted_images)

        org_settings = cls(
            restricted_images=restricted_images,
        )

        org_settings.additional_properties = d
        return org_settings

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
