from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetNamespaceRepositoryImagesTagsResponseResultsItem")


@attr.s(auto_attribs=True)
class GetNamespaceRepositoryImagesTagsResponseResultsItem:
    """
    Attributes:
        tag (Union[Unset, str]): The tag. Example: latest.
        is_current (Union[Unset, bool]): `true` if the tag currently points to this image.

            `false` if it has been overwritten to point at a different image.
             Example: True.
    """

    tag: Union[Unset, str] = UNSET
    is_current: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tag = self.tag
        is_current = self.is_current

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tag is not UNSET:
            field_dict["tag"] = tag
        if is_current is not UNSET:
            field_dict["is_current"] = is_current

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        tag = d.pop("tag", UNSET)

        is_current = d.pop("is_current", UNSET)

        get_namespace_repository_images_tags_response_results_item = cls(
            tag=tag,
            is_current=is_current,
        )

        get_namespace_repository_images_tags_response_results_item.additional_properties = d
        return get_namespace_repository_images_tags_response_results_item

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
