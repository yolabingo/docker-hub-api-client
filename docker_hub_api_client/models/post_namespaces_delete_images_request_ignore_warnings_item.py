from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.post_namespaces_delete_images_request_ignore_warnings_item_warning import (
    PostNamespacesDeleteImagesRequestIgnoreWarningsItemWarning,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostNamespacesDeleteImagesRequestIgnoreWarningsItem")


@attr.s(auto_attribs=True)
class PostNamespacesDeleteImagesRequestIgnoreWarningsItem:
    """
    Attributes:
        repository (str): Name of the repository of the image to ignore the warning for. Example: myrepo.
        digest (str): Digest of the image to ignore the warning for. Example:
            sha256:1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqr.
        warning (PostNamespacesDeleteImagesRequestIgnoreWarningsItemWarning): Warning to ignore. Example: current_tag.
        tags (Union[Unset, List[str]]): Current tags to ignore.
    """

    repository: str
    digest: str
    warning: PostNamespacesDeleteImagesRequestIgnoreWarningsItemWarning
    tags: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        repository = self.repository
        digest = self.digest
        warning = self.warning.value

        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "repository": repository,
                "digest": digest,
                "warning": warning,
            }
        )
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        repository = d.pop("repository")

        digest = d.pop("digest")

        warning = PostNamespacesDeleteImagesRequestIgnoreWarningsItemWarning(d.pop("warning"))

        tags = cast(List[str], d.pop("tags", UNSET))

        post_namespaces_delete_images_request_ignore_warnings_item = cls(
            repository=repository,
            digest=digest,
            warning=warning,
            tags=tags,
        )

        post_namespaces_delete_images_request_ignore_warnings_item.additional_properties = d
        return post_namespaces_delete_images_request_ignore_warnings_item

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
