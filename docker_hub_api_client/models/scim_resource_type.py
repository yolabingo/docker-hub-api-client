from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ScimResourceType")


@attr.s(auto_attribs=True)
class ScimResourceType:
    """
    Attributes:
        schemas (Union[Unset, List[str]]):  Example: urn:ietf:params:scim:schemas:core:2.0:ResourceType.
        id (Union[Unset, str]):  Example: User.
        name (Union[Unset, str]):  Example: User.
        description (Union[Unset, str]):  Example: User.
        endpoint (Union[Unset, str]):  Example: /Users.
        schema (Union[Unset, str]):  Example: urn:ietf:params:scim:schemas:core:2.0:User.
    """

    schemas: Union[Unset, List[str]] = UNSET
    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    endpoint: Union[Unset, str] = UNSET
    schema: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        schemas: Union[Unset, List[str]] = UNSET
        if not isinstance(self.schemas, Unset):
            schemas = self.schemas

        id = self.id
        name = self.name
        description = self.description
        endpoint = self.endpoint
        schema = self.schema

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if schemas is not UNSET:
            field_dict["schemas"] = schemas
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if endpoint is not UNSET:
            field_dict["endpoint"] = endpoint
        if schema is not UNSET:
            field_dict["schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        schemas = cast(List[str], d.pop("schemas", UNSET))

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        endpoint = d.pop("endpoint", UNSET)

        schema = d.pop("schema", UNSET)

        scim_resource_type = cls(
            schemas=schemas,
            id=id,
            name=name,
            description=description,
            endpoint=endpoint,
            schema=schema,
        )

        scim_resource_type.additional_properties = d
        return scim_resource_type

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
