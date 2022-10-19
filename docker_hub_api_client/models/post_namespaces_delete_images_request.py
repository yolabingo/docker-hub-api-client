from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.post_namespaces_delete_images_request_ignore_warnings_item import (
    PostNamespacesDeleteImagesRequestIgnoreWarningsItem,
)
from ..models.post_namespaces_delete_images_request_manifests_item import PostNamespacesDeleteImagesRequestManifestsItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostNamespacesDeleteImagesRequest")


@attr.s(auto_attribs=True)
class PostNamespacesDeleteImagesRequest:
    """Delete images request.

    Attributes:
        dry_run (Union[Unset, bool]): If `true` then will check and return errors and unignored warnings for the
            deletion request but will not delete any images.
        active_from (Union[Unset, str]): Sets the time from which an image must have been pushed or pulled to
            be counted as active.

            Defaults to 1 month before the current time.
             Example: 2020-12-01 12:00:00+00:00.
        manifests (Union[Unset, List[PostNamespacesDeleteImagesRequestManifestsItem]]): Image manifests to delete.
        ignore_warnings (Union[Unset, List[PostNamespacesDeleteImagesRequestIgnoreWarningsItem]]): Warnings to ignore.
            If a warning is not ignored then no deletions will happen and the
            warning is returned in the response.

            These warnings include:

            - is_active: warning when attempting to delete an image that is marked as active.
            - current_tag: warning when attempting to delete an image that has one or more current
            tags in the repository.

            Warnings can be copied from the response to the request.
    """

    dry_run: Union[Unset, bool] = UNSET
    active_from: Union[Unset, str] = UNSET
    manifests: Union[Unset, List[PostNamespacesDeleteImagesRequestManifestsItem]] = UNSET
    ignore_warnings: Union[Unset, List[PostNamespacesDeleteImagesRequestIgnoreWarningsItem]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dry_run = self.dry_run
        active_from = self.active_from
        manifests: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.manifests, Unset):
            manifests = []
            for manifests_item_data in self.manifests:
                manifests_item = manifests_item_data.to_dict()

                manifests.append(manifests_item)

        ignore_warnings: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.ignore_warnings, Unset):
            ignore_warnings = []
            for ignore_warnings_item_data in self.ignore_warnings:
                ignore_warnings_item = ignore_warnings_item_data.to_dict()

                ignore_warnings.append(ignore_warnings_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dry_run is not UNSET:
            field_dict["dry_run"] = dry_run
        if active_from is not UNSET:
            field_dict["active_from"] = active_from
        if manifests is not UNSET:
            field_dict["manifests"] = manifests
        if ignore_warnings is not UNSET:
            field_dict["ignore_warnings"] = ignore_warnings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        dry_run = d.pop("dry_run", UNSET)

        active_from = d.pop("active_from", UNSET)

        manifests = []
        _manifests = d.pop("manifests", UNSET)
        for manifests_item_data in _manifests or []:
            manifests_item = PostNamespacesDeleteImagesRequestManifestsItem.from_dict(manifests_item_data)

            manifests.append(manifests_item)

        ignore_warnings = []
        _ignore_warnings = d.pop("ignore_warnings", UNSET)
        for ignore_warnings_item_data in _ignore_warnings or []:
            ignore_warnings_item = PostNamespacesDeleteImagesRequestIgnoreWarningsItem.from_dict(
                ignore_warnings_item_data
            )

            ignore_warnings.append(ignore_warnings_item)

        post_namespaces_delete_images_request = cls(
            dry_run=dry_run,
            active_from=active_from,
            manifests=manifests,
            ignore_warnings=ignore_warnings,
        )

        post_namespaces_delete_images_request.additional_properties = d
        return post_namespaces_delete_images_request

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
