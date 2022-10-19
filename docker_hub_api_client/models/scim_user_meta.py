from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ScimUserMeta")


@attr.s(auto_attribs=True)
class ScimUserMeta:
    """
    Attributes:
        resource_type (Union[Unset, str]):  Example: User.
        location (Union[Unset, str]):  Example:
            https://hub.docker.com/v2/scim/2.0/Users/d80f7c79-7730-49d8-9a41-7c42fb622d9c.
        created (Union[Unset, str]): The creation date for the user as a RFC3339 formatted string. Example: 2022-05-20
            00:54:18+00:00.
        last_modified (Union[Unset, str]): The date the user was last modified as a RFC3339 formatted string. Example:
            2022-05-20 00:54:18+00:00.
    """

    resource_type: Union[Unset, str] = UNSET
    location: Union[Unset, str] = UNSET
    created: Union[Unset, str] = UNSET
    last_modified: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        resource_type = self.resource_type
        location = self.location
        created = self.created
        last_modified = self.last_modified

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if resource_type is not UNSET:
            field_dict["resourceType"] = resource_type
        if location is not UNSET:
            field_dict["location"] = location
        if created is not UNSET:
            field_dict["created"] = created
        if last_modified is not UNSET:
            field_dict["lastModified"] = last_modified

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        resource_type = d.pop("resourceType", UNSET)

        location = d.pop("location", UNSET)

        created = d.pop("created", UNSET)

        last_modified = d.pop("lastModified", UNSET)

        scim_user_meta = cls(
            resource_type=resource_type,
            location=location,
            created=created,
            last_modified=last_modified,
        )

        scim_user_meta.additional_properties = d
        return scim_user_meta

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
