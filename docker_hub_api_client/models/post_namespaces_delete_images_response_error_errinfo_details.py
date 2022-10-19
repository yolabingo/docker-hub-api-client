from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.post_namespaces_delete_images_response_error_errinfo_details_errors_item import (
    PostNamespacesDeleteImagesResponseErrorErrinfoDetailsErrorsItem,
)
from ..models.post_namespaces_delete_images_response_error_errinfo_details_warnings_item import (
    PostNamespacesDeleteImagesResponseErrorErrinfoDetailsWarningsItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostNamespacesDeleteImagesResponseErrorErrinfoDetails")


@attr.s(auto_attribs=True)
class PostNamespacesDeleteImagesResponseErrorErrinfoDetails:
    """
    Attributes:
        errors (Union[Unset, List[PostNamespacesDeleteImagesResponseErrorErrinfoDetailsErrorsItem]]): Errors from
            validating delete request. These cannot be ignored.
        warnings (Union[Unset, List[PostNamespacesDeleteImagesResponseErrorErrinfoDetailsWarningsItem]]): Warnings that
            can be ignored.

            These warnings include:

            - is_active: warning when attempting to delete an image that is marked as
            active.
            - current_tag: warning when attempting to delete an image that has one or
            more current tags in the repository.

            Warnings can be copied from the response to the request.
    """

    errors: Union[Unset, List[PostNamespacesDeleteImagesResponseErrorErrinfoDetailsErrorsItem]] = UNSET
    warnings: Union[Unset, List[PostNamespacesDeleteImagesResponseErrorErrinfoDetailsWarningsItem]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        errors: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()

                errors.append(errors_item)

        warnings: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = []
            for warnings_item_data in self.warnings:
                warnings_item = warnings_item_data.to_dict()

                warnings.append(warnings_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if errors is not UNSET:
            field_dict["errors"] = errors
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        errors = []
        _errors = d.pop("errors", UNSET)
        for errors_item_data in _errors or []:
            errors_item = PostNamespacesDeleteImagesResponseErrorErrinfoDetailsErrorsItem.from_dict(errors_item_data)

            errors.append(errors_item)

        warnings = []
        _warnings = d.pop("warnings", UNSET)
        for warnings_item_data in _warnings or []:
            warnings_item = PostNamespacesDeleteImagesResponseErrorErrinfoDetailsWarningsItem.from_dict(
                warnings_item_data
            )

            warnings.append(warnings_item)

        post_namespaces_delete_images_response_error_errinfo_details = cls(
            errors=errors,
            warnings=warnings,
        )

        post_namespaces_delete_images_response_error_errinfo_details.additional_properties = d
        return post_namespaces_delete_images_response_error_errinfo_details

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
