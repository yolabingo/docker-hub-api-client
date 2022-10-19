from typing import Any, Dict, List, Type, TypeVar, cast

import attr

T = TypeVar("T", bound="CreateAccessTokenRequest")


@attr.s(auto_attribs=True)
class CreateAccessTokenRequest:
    """
    Attributes:
        token_label (str): Friendly name for you to identify the token. Example: My read only token.
        scopes (List[str]): Valid scopes: "repo:admin", "repo:write", "repo:read", "repo:public_read"
             Example: ['repo:read'].
    """

    token_label: str
    scopes: List[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        token_label = self.token_label
        scopes = self.scopes

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "token_label": token_label,
                "scopes": scopes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        token_label = d.pop("token_label")

        scopes = cast(List[str], d.pop("scopes"))

        create_access_token_request = cls(
            token_label=token_label,
            scopes=scopes,
        )

        create_access_token_request.additional_properties = d
        return create_access_token_request

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
