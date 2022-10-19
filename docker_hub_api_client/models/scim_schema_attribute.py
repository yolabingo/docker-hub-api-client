from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.scim_schema_attribute_type import ScimSchemaAttributeType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ScimSchemaAttribute")


@attr.s(auto_attribs=True)
class ScimSchemaAttribute:
    """
    Attributes:
        name (Union[Unset, str]):  Example: userName.
        type (Union[Unset, ScimSchemaAttributeType]):  Example: string.
        multi_valued (Union[Unset, bool]):
        description (Union[Unset, str]):  Example: Unique identifier for the User, typically used by the user to
            directly authenticate to the service provider. Each User MUST include a non-empty userName value. This
            identifier MUST be unique across the service provider's entire set of Users..
        required (Union[Unset, bool]):  Example: True.
        case_exact (Union[Unset, bool]):
        mutability (Union[Unset, str]):  Example: readWrite.
        returned (Union[Unset, str]):  Example: default.
        uniqueness (Union[Unset, str]):  Example: server.
    """

    name: Union[Unset, str] = UNSET
    type: Union[Unset, ScimSchemaAttributeType] = UNSET
    multi_valued: Union[Unset, bool] = UNSET
    description: Union[Unset, str] = UNSET
    required: Union[Unset, bool] = UNSET
    case_exact: Union[Unset, bool] = UNSET
    mutability: Union[Unset, str] = UNSET
    returned: Union[Unset, str] = UNSET
    uniqueness: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        multi_valued = self.multi_valued
        description = self.description
        required = self.required
        case_exact = self.case_exact
        mutability = self.mutability
        returned = self.returned
        uniqueness = self.uniqueness

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if type is not UNSET:
            field_dict["type"] = type
        if multi_valued is not UNSET:
            field_dict["multiValued"] = multi_valued
        if description is not UNSET:
            field_dict["description"] = description
        if required is not UNSET:
            field_dict["required"] = required
        if case_exact is not UNSET:
            field_dict["caseExact"] = case_exact
        if mutability is not UNSET:
            field_dict["mutability"] = mutability
        if returned is not UNSET:
            field_dict["returned"] = returned
        if uniqueness is not UNSET:
            field_dict["uniqueness"] = uniqueness

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, ScimSchemaAttributeType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = ScimSchemaAttributeType(_type)

        multi_valued = d.pop("multiValued", UNSET)

        description = d.pop("description", UNSET)

        required = d.pop("required", UNSET)

        case_exact = d.pop("caseExact", UNSET)

        mutability = d.pop("mutability", UNSET)

        returned = d.pop("returned", UNSET)

        uniqueness = d.pop("uniqueness", UNSET)

        scim_schema_attribute = cls(
            name=name,
            type=type,
            multi_valued=multi_valued,
            description=description,
            required=required,
            case_exact=case_exact,
            mutability=mutability,
            returned=returned,
            uniqueness=uniqueness,
        )

        scim_schema_attribute.additional_properties = d
        return scim_schema_attribute

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
