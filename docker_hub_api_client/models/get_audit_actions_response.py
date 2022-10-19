from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.get_audit_actions_response_actions import GetAuditActionsResponseActions
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetAuditActionsResponse")


@attr.s(auto_attribs=True)
class GetAuditActionsResponse:
    """GetAuditActions response.

    Attributes:
        actions (Union[Unset, GetAuditActionsResponseActions]): Map of audit log actions.
    """

    actions: Union[Unset, GetAuditActionsResponseActions] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        actions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.actions, Unset):
            actions = self.actions.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if actions is not UNSET:
            field_dict["actions"] = actions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _actions = d.pop("actions", UNSET)
        actions: Union[Unset, GetAuditActionsResponseActions]
        if isinstance(_actions, Unset):
            actions = UNSET
        else:
            actions = GetAuditActionsResponseActions.from_dict(_actions)

        get_audit_actions_response = cls(
            actions=actions,
        )

        get_audit_actions_response.additional_properties = d
        return get_audit_actions_response

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
