from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.post_namespaces_delete_images_response_error_errinfo_details_errors_item_error import (
    PostNamespacesDeleteImagesResponseErrorErrinfoDetailsErrorsItemError,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostNamespacesDeleteImagesResponseErrorErrinfoDetailsErrorsItem")


@attr.s(auto_attribs=True)
class PostNamespacesDeleteImagesResponseErrorErrinfoDetailsErrorsItem:
    """
    Attributes:
        repository (Union[Unset, str]): Name of the repository of the image that caused the error. Example: myrepo.
        digest (Union[Unset, str]): Digest of the image that caused the error. Example:
            sha256:1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqr.
        error (Union[Unset, PostNamespacesDeleteImagesResponseErrorErrinfoDetailsErrorsItemError]): Error type. Example:
            not_found.
    """

    repository: Union[Unset, str] = UNSET
    digest: Union[Unset, str] = UNSET
    error: Union[Unset, PostNamespacesDeleteImagesResponseErrorErrinfoDetailsErrorsItemError] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        repository = self.repository
        digest = self.digest
        error: Union[Unset, str] = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if repository is not UNSET:
            field_dict["repository"] = repository
        if digest is not UNSET:
            field_dict["digest"] = digest
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        repository = d.pop("repository", UNSET)

        digest = d.pop("digest", UNSET)

        _error = d.pop("error", UNSET)
        error: Union[Unset, PostNamespacesDeleteImagesResponseErrorErrinfoDetailsErrorsItemError]
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = PostNamespacesDeleteImagesResponseErrorErrinfoDetailsErrorsItemError(_error)

        post_namespaces_delete_images_response_error_errinfo_details_errors_item = cls(
            repository=repository,
            digest=digest,
            error=error,
        )

        post_namespaces_delete_images_response_error_errinfo_details_errors_item.additional_properties = d
        return post_namespaces_delete_images_response_error_errinfo_details_errors_item

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
