from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.post_namespaces_delete_images_response_error_errinfo_details import (
    PostNamespacesDeleteImagesResponseErrorErrinfoDetails,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostNamespacesDeleteImagesResponseErrorErrinfo")


@attr.s(auto_attribs=True)
class PostNamespacesDeleteImagesResponseErrorErrinfo:
    """
    Attributes:
        api_call_docker_id (Union[Unset, str]): ID of docker user.
        api_call_name (Union[Unset, str]): Name of the API operation called.
        api_call_start (Union[Unset, str]): Date/time of call start.
        api_call_txnid (Union[Unset, str]): Unique ID for this call.
        type (Union[Unset, str]): Type of error. Example: validation.
        details (Union[Unset, PostNamespacesDeleteImagesResponseErrorErrinfoDetails]):
    """

    api_call_docker_id: Union[Unset, str] = UNSET
    api_call_name: Union[Unset, str] = UNSET
    api_call_start: Union[Unset, str] = UNSET
    api_call_txnid: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    details: Union[Unset, PostNamespacesDeleteImagesResponseErrorErrinfoDetails] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        api_call_docker_id = self.api_call_docker_id
        api_call_name = self.api_call_name
        api_call_start = self.api_call_start
        api_call_txnid = self.api_call_txnid
        type = self.type
        details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if api_call_docker_id is not UNSET:
            field_dict["api_call_docker_id"] = api_call_docker_id
        if api_call_name is not UNSET:
            field_dict["api_call_name"] = api_call_name
        if api_call_start is not UNSET:
            field_dict["api_call_start"] = api_call_start
        if api_call_txnid is not UNSET:
            field_dict["api_call_txnid"] = api_call_txnid
        if type is not UNSET:
            field_dict["type"] = type
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        api_call_docker_id = d.pop("api_call_docker_id", UNSET)

        api_call_name = d.pop("api_call_name", UNSET)

        api_call_start = d.pop("api_call_start", UNSET)

        api_call_txnid = d.pop("api_call_txnid", UNSET)

        type = d.pop("type", UNSET)

        _details = d.pop("details", UNSET)
        details: Union[Unset, PostNamespacesDeleteImagesResponseErrorErrinfoDetails]
        if isinstance(_details, Unset):
            details = UNSET
        else:
            details = PostNamespacesDeleteImagesResponseErrorErrinfoDetails.from_dict(_details)

        post_namespaces_delete_images_response_error_errinfo = cls(
            api_call_docker_id=api_call_docker_id,
            api_call_name=api_call_name,
            api_call_start=api_call_start,
            api_call_txnid=api_call_txnid,
            type=type,
            details=details,
        )

        post_namespaces_delete_images_response_error_errinfo.additional_properties = d
        return post_namespaces_delete_images_response_error_errinfo

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
