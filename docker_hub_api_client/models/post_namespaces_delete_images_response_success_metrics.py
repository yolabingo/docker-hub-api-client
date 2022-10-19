from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostNamespacesDeleteImagesResponseSuccessMetrics")


@attr.s(auto_attribs=True)
class PostNamespacesDeleteImagesResponseSuccessMetrics:
    """
    Attributes:
        manifest_deletes (Union[Unset, int]): Number of manifests deleted. Example: 3.
        manifest_errors (Union[Unset, int]): Number of manifests that failed to delete.
        tag_deletes (Union[Unset, int]): Number of tags deleted. Example: 1.
        tag_errors (Union[Unset, int]): Number of tags that failed to delete.
    """

    manifest_deletes: Union[Unset, int] = UNSET
    manifest_errors: Union[Unset, int] = UNSET
    tag_deletes: Union[Unset, int] = UNSET
    tag_errors: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        manifest_deletes = self.manifest_deletes
        manifest_errors = self.manifest_errors
        tag_deletes = self.tag_deletes
        tag_errors = self.tag_errors

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if manifest_deletes is not UNSET:
            field_dict["manifest_deletes"] = manifest_deletes
        if manifest_errors is not UNSET:
            field_dict["manifest_errors"] = manifest_errors
        if tag_deletes is not UNSET:
            field_dict["tag_deletes"] = tag_deletes
        if tag_errors is not UNSET:
            field_dict["tag_errors"] = tag_errors

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        manifest_deletes = d.pop("manifest_deletes", UNSET)

        manifest_errors = d.pop("manifest_errors", UNSET)

        tag_deletes = d.pop("tag_deletes", UNSET)

        tag_errors = d.pop("tag_errors", UNSET)

        post_namespaces_delete_images_response_success_metrics = cls(
            manifest_deletes=manifest_deletes,
            manifest_errors=manifest_errors,
            tag_deletes=tag_deletes,
            tag_errors=tag_errors,
        )

        post_namespaces_delete_images_response_success_metrics.additional_properties = d
        return post_namespaces_delete_images_response_success_metrics

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
