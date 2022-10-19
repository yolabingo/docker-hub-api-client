from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Layer")


@attr.s(auto_attribs=True)
class Layer:
    """
    Attributes:
        digest (Union[Unset, None, str]): image layer digest
        size (Union[Unset, int]): size of the layer
        instruction (Union[Unset, str]): Dockerfile instruction
    """

    digest: Union[Unset, None, str] = UNSET
    size: Union[Unset, int] = UNSET
    instruction: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        digest = self.digest
        size = self.size
        instruction = self.instruction

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if digest is not UNSET:
            field_dict["digest"] = digest
        if size is not UNSET:
            field_dict["size"] = size
        if instruction is not UNSET:
            field_dict["instruction"] = instruction

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        digest = d.pop("digest", UNSET)

        size = d.pop("size", UNSET)

        instruction = d.pop("instruction", UNSET)

        layer = cls(
            digest=digest,
            size=size,
            instruction=instruction,
        )

        layer.additional_properties = d
        return layer

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
