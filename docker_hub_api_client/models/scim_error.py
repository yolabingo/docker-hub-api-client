from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ScimError")


@attr.s(auto_attribs=True)
class ScimError:
    """
    Attributes:
        status (Union[Unset, str]): The status code for the response in string format.
        schemas (Union[Unset, List[str]]):
        detail (Union[Unset, str]): Details about why the request failed.
    """

    status: Union[Unset, str] = UNSET
    schemas: Union[Unset, List[str]] = UNSET
    detail: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status = self.status
        schemas: Union[Unset, List[str]] = UNSET
        if not isinstance(self.schemas, Unset):
            schemas = self.schemas

        detail = self.detail

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if schemas is not UNSET:
            field_dict["schemas"] = schemas
        if detail is not UNSET:
            field_dict["detail"] = detail

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        status = d.pop("status", UNSET)

        schemas = cast(List[str], d.pop("schemas", UNSET))

        detail = d.pop("detail", UNSET)

        scim_error = cls(
            status=status,
            schemas=schemas,
            detail=detail,
        )

        scim_error.additional_properties = d
        return scim_error

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
