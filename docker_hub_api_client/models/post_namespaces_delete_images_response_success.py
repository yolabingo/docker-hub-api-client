from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.post_namespaces_delete_images_response_success_metrics import (
    PostNamespacesDeleteImagesResponseSuccessMetrics,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostNamespacesDeleteImagesResponseSuccess")


@attr.s(auto_attribs=True)
class PostNamespacesDeleteImagesResponseSuccess:
    """Successful delete images response.

    Attributes:
        dry_run (Union[Unset, bool]): Whether the request was a dry run or not.
        metrics (Union[Unset, PostNamespacesDeleteImagesResponseSuccessMetrics]):
    """

    dry_run: Union[Unset, bool] = UNSET
    metrics: Union[Unset, PostNamespacesDeleteImagesResponseSuccessMetrics] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dry_run = self.dry_run
        metrics: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metrics, Unset):
            metrics = self.metrics.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dry_run is not UNSET:
            field_dict["dry_run"] = dry_run
        if metrics is not UNSET:
            field_dict["metrics"] = metrics

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        dry_run = d.pop("dry_run", UNSET)

        _metrics = d.pop("metrics", UNSET)
        metrics: Union[Unset, PostNamespacesDeleteImagesResponseSuccessMetrics]
        if isinstance(_metrics, Unset):
            metrics = UNSET
        else:
            metrics = PostNamespacesDeleteImagesResponseSuccessMetrics.from_dict(_metrics)

        post_namespaces_delete_images_response_success = cls(
            dry_run=dry_run,
            metrics=metrics,
        )

        post_namespaces_delete_images_response_success.additional_properties = d
        return post_namespaces_delete_images_response_success

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
