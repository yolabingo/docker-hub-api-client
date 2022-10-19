from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.value_error_fields import ValueErrorFields
from ..types import UNSET, Unset

T = TypeVar("T", bound="ValueError_")


@attr.s(auto_attribs=True)
class ValueError_:
    """Used to error if input validation fails.

    Attributes:
        fields (Union[Unset, ValueErrorFields]):
        text (Union[Unset, str]):
    """

    fields: Union[Unset, ValueErrorFields] = UNSET
    text: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        fields: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.fields, Unset):
            fields = self.fields.to_dict()

        text = self.text

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fields is not UNSET:
            field_dict["fields"] = fields
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _fields = d.pop("fields", UNSET)
        fields: Union[Unset, ValueErrorFields]
        if isinstance(_fields, Unset):
            fields = UNSET
        else:
            fields = ValueErrorFields.from_dict(_fields)

        text = d.pop("text", UNSET)

        value_error = cls(
            fields=fields,
            text=text,
        )

        value_error.additional_properties = d
        return value_error

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
