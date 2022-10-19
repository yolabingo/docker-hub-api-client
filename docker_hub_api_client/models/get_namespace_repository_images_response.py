from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.get_namespace_repository_images_response_results_item import (
    GetNamespaceRepositoryImagesResponseResultsItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetNamespaceRepositoryImagesResponse")


@attr.s(auto_attribs=True)
class GetNamespaceRepositoryImagesResponse:
    """Paginated list of images in a repository.

    Attributes:
        count (Union[Unset, int]): Total count of images in the repository. Example: 100.
        next_ (Union[Unset, None, str]): Link to the next page with the same query parameters if there are more images.
            Example: https://hub.docker.com/v2/namespaces/mynamespace/repositories/myrepo/images?&page=4&page_size=20.
        previous (Union[Unset, None, str]): Link to the previous page with the same query parameters if not on first
            page. Example: https://hub.docker.com/v2/namespaces/mynamespace/repositories/myrepo/images?&page=2&page_size=20.
        results (Union[Unset, List[GetNamespaceRepositoryImagesResponseResultsItem]]): Image details.
    """

    count: Union[Unset, int] = UNSET
    next_: Union[Unset, None, str] = UNSET
    previous: Union[Unset, None, str] = UNSET
    results: Union[Unset, List[GetNamespaceRepositoryImagesResponseResultsItem]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        count = self.count
        next_ = self.next_
        previous = self.previous
        results: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.results, Unset):
            results = []
            for results_item_data in self.results:
                results_item = results_item_data.to_dict()

                results.append(results_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if next_ is not UNSET:
            field_dict["next"] = next_
        if previous is not UNSET:
            field_dict["previous"] = previous
        if results is not UNSET:
            field_dict["results"] = results

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        count = d.pop("count", UNSET)

        next_ = d.pop("next", UNSET)

        previous = d.pop("previous", UNSET)

        results = []
        _results = d.pop("results", UNSET)
        for results_item_data in _results or []:
            results_item = GetNamespaceRepositoryImagesResponseResultsItem.from_dict(results_item_data)

            results.append(results_item)

        get_namespace_repository_images_response = cls(
            count=count,
            next_=next_,
            previous=previous,
            results=results,
        )

        get_namespace_repository_images_response.additional_properties = d
        return get_namespace_repository_images_response

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
