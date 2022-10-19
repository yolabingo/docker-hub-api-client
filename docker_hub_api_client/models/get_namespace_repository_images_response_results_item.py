from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.get_namespace_repository_images_response_results_item_status import (
    GetNamespaceRepositoryImagesResponseResultsItemStatus,
)
from ..models.get_namespace_repository_images_response_results_item_tags_item import (
    GetNamespaceRepositoryImagesResponseResultsItemTagsItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetNamespaceRepositoryImagesResponseResultsItem")


@attr.s(auto_attribs=True)
class GetNamespaceRepositoryImagesResponseResultsItem:
    """
    Attributes:
        namespace (Union[Unset, str]): The repository namespace. Example: mynamespace.
        repository (Union[Unset, str]): The repository name. Example: myrepo.
        digest (Union[Unset, str]): The image's digest. Example:
            sha256:1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqr.
        tags (Union[Unset, List[GetNamespaceRepositoryImagesResponseResultsItemTagsItem]]): The current and historical
            tags for this image.
        last_pushed (Union[Unset, None, str]): Time when this image was last pushed. Example: 2021-02-24
            22:05:27.526308+00:00.
        last_pulled (Union[Unset, None, str]): Time when this image was last pulled. Note this is updated at most once
            per hour. Example: 2021-02-24 23:16:10.200008+00:00.
        status (Union[Unset, GetNamespaceRepositoryImagesResponseResultsItemStatus]): The status of the image based on
            its last activity against the `active_from` time. Example: active.
    """

    namespace: Union[Unset, str] = UNSET
    repository: Union[Unset, str] = UNSET
    digest: Union[Unset, str] = UNSET
    tags: Union[Unset, List[GetNamespaceRepositoryImagesResponseResultsItemTagsItem]] = UNSET
    last_pushed: Union[Unset, None, str] = UNSET
    last_pulled: Union[Unset, None, str] = UNSET
    status: Union[Unset, GetNamespaceRepositoryImagesResponseResultsItemStatus] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        namespace = self.namespace
        repository = self.repository
        digest = self.digest
        tags: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()

                tags.append(tags_item)

        last_pushed = self.last_pushed
        last_pulled = self.last_pulled
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if repository is not UNSET:
            field_dict["repository"] = repository
        if digest is not UNSET:
            field_dict["digest"] = digest
        if tags is not UNSET:
            field_dict["tags"] = tags
        if last_pushed is not UNSET:
            field_dict["last_pushed"] = last_pushed
        if last_pulled is not UNSET:
            field_dict["last_pulled"] = last_pulled
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        namespace = d.pop("namespace", UNSET)

        repository = d.pop("repository", UNSET)

        digest = d.pop("digest", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = GetNamespaceRepositoryImagesResponseResultsItemTagsItem.from_dict(tags_item_data)

            tags.append(tags_item)

        last_pushed = d.pop("last_pushed", UNSET)

        last_pulled = d.pop("last_pulled", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, GetNamespaceRepositoryImagesResponseResultsItemStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = GetNamespaceRepositoryImagesResponseResultsItemStatus(_status)

        get_namespace_repository_images_response_results_item = cls(
            namespace=namespace,
            repository=repository,
            digest=digest,
            tags=tags,
            last_pushed=last_pushed,
            last_pulled=last_pulled,
            status=status,
        )

        get_namespace_repository_images_response_results_item.additional_properties = d
        return get_namespace_repository_images_response_results_item

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
