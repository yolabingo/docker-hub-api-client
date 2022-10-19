from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.scim_schema_parent_attribute import ScimSchemaParentAttribute
from ..types import UNSET, Unset

T = TypeVar("T", bound="ScimSchema")


@attr.s(auto_attribs=True)
class ScimSchema:
    """
    Attributes:
        schemas (Union[Unset, List[str]]):  Example: ['urn:ietf:params:scim:schemas:core:2.0:Schema'].
        id (Union[Unset, str]):  Example: urn:ietf:params:scim:schemas:core:2.0:User.
        name (Union[Unset, str]):  Example: User.
        description (Union[Unset, str]):  Example: User Account.
        attributes (Union[Unset, List[ScimSchemaParentAttribute]]):
    """

    schemas: Union[Unset, List[str]] = UNSET
    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    attributes: Union[Unset, List[ScimSchemaParentAttribute]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        schemas: Union[Unset, List[str]] = UNSET
        if not isinstance(self.schemas, Unset):
            schemas = self.schemas

        id = self.id
        name = self.name
        description = self.description
        attributes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = []
            for attributes_item_data in self.attributes:
                attributes_item = attributes_item_data.to_dict()

                attributes.append(attributes_item)

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
        if attributes is not UNSET:
            field_dict["attributes"] = attributes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        schemas = cast(List[str], d.pop("schemas", UNSET))

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        attributes = []
        _attributes = d.pop("attributes", UNSET)
        for attributes_item_data in _attributes or []:
            attributes_item = ScimSchemaParentAttribute.from_dict(attributes_item_data)

            attributes.append(attributes_item)

        scim_schema = cls(
            schemas=schemas,
            id=id,
            name=name,
            description=description,
            attributes=attributes,
        )

        scim_schema.additional_properties = d
        return scim_schema

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
