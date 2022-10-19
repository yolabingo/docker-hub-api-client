from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AccessToken")


@attr.s(auto_attribs=True)
class AccessToken:
    """
    Attributes:
        uuid (Union[Unset, str]):  Example: b30bbf97-506c-4ecd-aabc-842f3cb484fb.
        client_id (Union[Unset, str]):  Example: HUB.
        creator_ip (Union[Unset, str]):  Example: 127.0.0.1.
        creator_ua (Union[Unset, str]):  Example: some user agent.
        created_at (Union[Unset, str]):  Example: 2021-07-20 12:00:00+00:00.
        last_used (Union[Unset, None, str]):
        generated_by (Union[Unset, str]):  Example: manual.
        is_active (Union[Unset, bool]):  Example: True.
        token (Union[Unset, str]):  Example: a7a5ef25-8889-43a0-8cc7-f2a94268e861.
        token_label (Union[Unset, str]):  Example: My read only token.
        scopes (Union[Unset, List[str]]):  Example: ['repo:read'].
    """

    uuid: Union[Unset, str] = UNSET
    client_id: Union[Unset, str] = UNSET
    creator_ip: Union[Unset, str] = UNSET
    creator_ua: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    last_used: Union[Unset, None, str] = UNSET
    generated_by: Union[Unset, str] = UNSET
    is_active: Union[Unset, bool] = UNSET
    token: Union[Unset, str] = UNSET
    token_label: Union[Unset, str] = UNSET
    scopes: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        uuid = self.uuid
        client_id = self.client_id
        creator_ip = self.creator_ip
        creator_ua = self.creator_ua
        created_at = self.created_at
        last_used = self.last_used
        generated_by = self.generated_by
        is_active = self.is_active
        token = self.token
        token_label = self.token_label
        scopes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.scopes, Unset):
            scopes = self.scopes

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if client_id is not UNSET:
            field_dict["client_id"] = client_id
        if creator_ip is not UNSET:
            field_dict["creator_ip"] = creator_ip
        if creator_ua is not UNSET:
            field_dict["creator_ua"] = creator_ua
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if last_used is not UNSET:
            field_dict["last_used"] = last_used
        if generated_by is not UNSET:
            field_dict["generated_by"] = generated_by
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if token is not UNSET:
            field_dict["token"] = token
        if token_label is not UNSET:
            field_dict["token_label"] = token_label
        if scopes is not UNSET:
            field_dict["scopes"] = scopes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        uuid = d.pop("uuid", UNSET)

        client_id = d.pop("client_id", UNSET)

        creator_ip = d.pop("creator_ip", UNSET)

        creator_ua = d.pop("creator_ua", UNSET)

        created_at = d.pop("created_at", UNSET)

        last_used = d.pop("last_used", UNSET)

        generated_by = d.pop("generated_by", UNSET)

        is_active = d.pop("is_active", UNSET)

        token = d.pop("token", UNSET)

        token_label = d.pop("token_label", UNSET)

        scopes = cast(List[str], d.pop("scopes", UNSET))

        access_token = cls(
            uuid=uuid,
            client_id=client_id,
            creator_ip=creator_ip,
            creator_ua=creator_ua,
            created_at=created_at,
            last_used=last_used,
            generated_by=generated_by,
            is_active=is_active,
            token=token,
            token_label=token_label,
            scopes=scopes,
        )

        access_token.additional_properties = d
        return access_token

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
