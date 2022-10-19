from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.audit_log import AuditLog
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetAuditLogsResponse")


@attr.s(auto_attribs=True)
class GetAuditLogsResponse:
    """GetAuditLogs response.

    Attributes:
        logs (Union[Unset, List[AuditLog]]): List of audit log events.
    """

    logs: Union[Unset, List[AuditLog]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        logs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.logs, Unset):
            logs = []
            for logs_item_data in self.logs:
                logs_item = logs_item_data.to_dict()

                logs.append(logs_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if logs is not UNSET:
            field_dict["logs"] = logs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        logs = []
        _logs = d.pop("logs", UNSET)
        for logs_item_data in _logs or []:
            logs_item = AuditLog.from_dict(logs_item_data)

            logs.append(logs_item)

        get_audit_logs_response = cls(
            logs=logs,
        )

        get_audit_logs_response.additional_properties = d
        return get_audit_logs_response

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
