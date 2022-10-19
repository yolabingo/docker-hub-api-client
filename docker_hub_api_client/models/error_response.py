from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.error_info import ErrorInfo
from ..types import UNSET, Unset

T = TypeVar("T", bound="ErrorResponse")


@attr.s(auto_attribs=True)
class ErrorResponse:
    """Represents an error.

    Attributes:
        txnid (Union[Unset, str]): Unique ID for this call.
        message (Union[Unset, str]): The error message.
        errinfo (Union[Unset, ErrorInfo]): Context information for an error used for diagnostics.
    """

    txnid: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    errinfo: Union[Unset, ErrorInfo] = UNSET
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
        errinfo: Union[Unset, ErrorInfo]
        if isinstance(_errinfo, Unset):
            errinfo = UNSET
        else:
            errinfo = ErrorInfo.from_dict(_errinfo)

        error_response = cls(
            txnid=txnid,
            message=message,
            errinfo=errinfo,
        )

        error_response.additional_properties = d
        return error_response

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
