from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.audit_log_action import AuditLogAction
from ..types import UNSET, Unset

T = TypeVar("T", bound="AuditLogActions")


@attr.s(auto_attribs=True)
class AuditLogActions:
    """
    Attributes:
        actions (Union[Unset, List[AuditLogAction]]): List of audit log actions.
        label (Union[Unset, str]): Grouping label for a particular set of audit log actions.
    """

    actions: Union[Unset, List[AuditLogAction]] = UNSET
    label: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        actions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.actions, Unset):
            actions = []
            for actions_item_data in self.actions:
                actions_item = actions_item_data.to_dict()

                actions.append(actions_item)

        label = self.label

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if actions is not UNSET:
            field_dict["actions"] = actions
        if label is not UNSET:
            field_dict["label"] = label

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        actions = []
        _actions = d.pop("actions", UNSET)
        for actions_item_data in _actions or []:
            actions_item = AuditLogAction.from_dict(actions_item_data)

            actions.append(actions_item)

        label = d.pop("label", UNSET)

        audit_log_actions = cls(
            actions=actions,
            label=label,
        )

        audit_log_actions.additional_properties = d
        return audit_log_actions

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
