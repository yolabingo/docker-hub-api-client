from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.scim_email import ScimEmail
from ..models.scim_group import ScimGroup
from ..models.scim_user_meta import ScimUserMeta
from ..models.scim_user_name import ScimUserName
from ..types import UNSET, Unset

T = TypeVar("T", bound="ScimUser")


@attr.s(auto_attribs=True)
class ScimUser:
    """
    Attributes:
        schemas (Union[Unset, List[str]]):
        id (Union[Unset, str]): The unique identifier for the user. A v4 UUID. Example:
            d80f7c79-7730-49d8-9a41-7c42fb622d9c.
        user_name (Union[Unset, str]): The user's email address. This must be reachable via email. Example:
            jon.snow@docker.com.
        name (Union[Unset, ScimUserName]):
        display_name (Union[Unset, str]): The username in Docker. Also known as the "Docker ID". Example: jonsnow.
        active (Union[Unset, bool]):  Example: True.
        emails (Union[Unset, List[ScimEmail]]):
        groups (Union[Unset, List[ScimGroup]]):
        meta (Union[Unset, ScimUserMeta]):
    """

    schemas: Union[Unset, List[str]] = UNSET
    id: Union[Unset, str] = UNSET
    user_name: Union[Unset, str] = UNSET
    name: Union[Unset, ScimUserName] = UNSET
    display_name: Union[Unset, str] = UNSET
    active: Union[Unset, bool] = UNSET
    emails: Union[Unset, List[ScimEmail]] = UNSET
    groups: Union[Unset, List[ScimGroup]] = UNSET
    meta: Union[Unset, ScimUserMeta] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        schemas: Union[Unset, List[str]] = UNSET
        if not isinstance(self.schemas, Unset):
            schemas = self.schemas

        id = self.id
        user_name = self.user_name
        name: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.to_dict()

        display_name = self.display_name
        active = self.active
        emails: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.emails, Unset):
            emails = []
            for emails_item_data in self.emails:
                emails_item = emails_item_data.to_dict()

                emails.append(emails_item)

        groups: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()

                groups.append(groups_item)

        meta: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if schemas is not UNSET:
            field_dict["schemas"] = schemas
        if id is not UNSET:
            field_dict["id"] = id
        if user_name is not UNSET:
            field_dict["userName"] = user_name
        if name is not UNSET:
            field_dict["name"] = name
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if active is not UNSET:
            field_dict["active"] = active
        if emails is not UNSET:
            field_dict["emails"] = emails
        if groups is not UNSET:
            field_dict["groups"] = groups
        if meta is not UNSET:
            field_dict["meta"] = meta

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        schemas = cast(List[str], d.pop("schemas", UNSET))

        id = d.pop("id", UNSET)

        user_name = d.pop("userName", UNSET)

        _name = d.pop("name", UNSET)
        name: Union[Unset, ScimUserName]
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = ScimUserName.from_dict(_name)

        display_name = d.pop("displayName", UNSET)

        active = d.pop("active", UNSET)

        emails = []
        _emails = d.pop("emails", UNSET)
        for emails_item_data in _emails or []:
            emails_item = ScimEmail.from_dict(emails_item_data)

            emails.append(emails_item)

        groups = []
        _groups = d.pop("groups", UNSET)
        for groups_item_data in _groups or []:
            groups_item = ScimGroup.from_dict(groups_item_data)

            groups.append(groups_item)

        _meta = d.pop("meta", UNSET)
        meta: Union[Unset, ScimUserMeta]
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = ScimUserMeta.from_dict(_meta)

        scim_user = cls(
            schemas=schemas,
            id=id,
            user_name=user_name,
            name=name,
            display_name=display_name,
            active=active,
            emails=emails,
            groups=groups,
            meta=meta,
        )

        scim_user.additional_properties = d
        return scim_user

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
