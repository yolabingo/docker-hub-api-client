from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.post_namespaces_delete_images_response_error_errinfo_details_warnings_item_warning import (
    PostNamespacesDeleteImagesResponseErrorErrinfoDetailsWarningsItemWarning,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostNamespacesDeleteImagesResponseErrorErrinfoDetailsWarningsItem")


@attr.s(auto_attribs=True)
class PostNamespacesDeleteImagesResponseErrorErrinfoDetailsWarningsItem:
    """
    Attributes:
        repository (Union[Unset, str]): Name of the repository of the image that caused the warning. Example: myrepo.
        digest (Union[Unset, str]): Digest of the image that caused the warning. Example:
            sha256:1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqr.
        warning (Union[Unset, PostNamespacesDeleteImagesResponseErrorErrinfoDetailsWarningsItemWarning]): Warning type.
            Example: current_tag.
        tags (Union[Unset, List[str]]): Current tags if warning is `current_tag`.
    """

    repository: Union[Unset, str] = UNSET
    digest: Union[Unset, str] = UNSET
    warning: Union[Unset, PostNamespacesDeleteImagesResponseErrorErrinfoDetailsWarningsItemWarning] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        repository = self.repository
        digest = self.digest
        warning: Union[Unset, str] = UNSET
        if not isinstance(self.warning, Unset):
            warning = self.warning.value

        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if repository is not UNSET:
            field_dict["repository"] = repository
        if digest is not UNSET:
            field_dict["digest"] = digest
        if warning is not UNSET:
            field_dict["warning"] = warning
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        repository = d.pop("repository", UNSET)

        digest = d.pop("digest", UNSET)

        _warning = d.pop("warning", UNSET)
        warning: Union[Unset, PostNamespacesDeleteImagesResponseErrorErrinfoDetailsWarningsItemWarning]
        if isinstance(_warning, Unset):
            warning = UNSET
        else:
            warning = PostNamespacesDeleteImagesResponseErrorErrinfoDetailsWarningsItemWarning(_warning)

        tags = cast(List[str], d.pop("tags", UNSET))

        post_namespaces_delete_images_response_error_errinfo_details_warnings_item = cls(
            repository=repository,
            digest=digest,
            warning=warning,
            tags=tags,
        )

        post_namespaces_delete_images_response_error_errinfo_details_warnings_item.additional_properties = d
        return post_namespaces_delete_images_response_error_errinfo_details_warnings_item

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
