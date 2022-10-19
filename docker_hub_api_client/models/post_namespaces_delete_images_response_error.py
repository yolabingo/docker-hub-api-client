from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.post_namespaces_delete_images_response_error_errinfo import PostNamespacesDeleteImagesResponseErrorErrinfo
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostNamespacesDeleteImagesResponseError")


@attr.s(auto_attribs=True)
class PostNamespacesDeleteImagesResponseError:
    """Deletion not possible.

    Attributes:
        txnid (Union[Unset, str]): Unique ID for this call.
        message (Union[Unset, str]): The error message.
        errinfo (Union[Unset, PostNamespacesDeleteImagesResponseErrorErrinfo]):
    """

    txnid: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    errinfo: Union[Unset, PostNamespacesDeleteImagesResponseErrorErrinfo] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        txnid = self.txnid
        message = self.message
        errinfo: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.errinfo, Unset):
            errinfo = self.errinfo.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if txnid is not UNSET:
            field_dict["txnid"] = txnid
        if message is not UNSET:
            field_dict["message"] = message
        if errinfo is not UNSET:
            field_dict["errinfo"] = errinfo

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        txnid = d.pop("txnid", UNSET)

        message = d.pop("message", UNSET)

        _errinfo = d.pop("errinfo", UNSET)
        errinfo: Union[Unset, PostNamespacesDeleteImagesResponseErrorErrinfo]
        if isinstance(_errinfo, Unset):
            errinfo = UNSET
        else:
            errinfo = PostNamespacesDeleteImagesResponseErrorErrinfo.from_dict(_errinfo)

        post_namespaces_delete_images_response_error = cls(
            txnid=txnid,
            message=message,
            errinfo=errinfo,
        )

        post_namespaces_delete_images_response_error.additional_properties = d
        return post_namespaces_delete_images_response_error

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
