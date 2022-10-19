import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.audit_log_data import AuditLogData
from ..types import UNSET, Unset

T = TypeVar("T", bound="AuditLog")


@attr.s(auto_attribs=True)
class AuditLog:
    """Audit log event.

    Attributes:
        account (Union[Unset, str]):
        action (Union[Unset, str]):
        name (Union[Unset, str]):
        actor (Union[Unset, str]):
        data (Union[Unset, AuditLogData]):
        timestamp (Union[Unset, datetime.datetime]):
        action_description (Union[Unset, str]):
    """

    account: Union[Unset, str] = UNSET
    action: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    actor: Union[Unset, str] = UNSET
    data: Union[Unset, AuditLogData] = UNSET
    timestamp: Union[Unset, datetime.datetime] = UNSET
    action_description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account = self.account
        action = self.action
        name = self.name
        actor = self.actor
        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        action_description = self.action_description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account is not UNSET:
            field_dict["account"] = account
        if action is not UNSET:
            field_dict["action"] = action
        if name is not UNSET:
            field_dict["name"] = name
        if actor is not UNSET:
            field_dict["actor"] = actor
        if data is not UNSET:
            field_dict["data"] = data
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if action_description is not UNSET:
            field_dict["action_description"] = action_description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        account = d.pop("account", UNSET)

        action = d.pop("action", UNSET)

        name = d.pop("name", UNSET)

        actor = d.pop("actor", UNSET)

        _data = d.pop("data", UNSET)
        data: Union[Unset, AuditLogData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = AuditLogData.from_dict(_data)

        _timestamp = d.pop("timestamp", UNSET)
        timestamp: Union[Unset, datetime.datetime]
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = isoparse(_timestamp)

        action_description = d.pop("action_description", UNSET)

        audit_log = cls(
            account=account,
            action=action,
            name=name,
            actor=actor,
            data=data,
            timestamp=timestamp,
            action_description=action_description,
        )

        audit_log.additional_properties = d
        return audit_log

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
