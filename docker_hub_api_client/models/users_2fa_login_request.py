from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="Users2FALoginRequest")


@attr.s(auto_attribs=True)
class Users2FALoginRequest:
    """Second factor user login details

    Attributes:
        login_2fa_token (str): The intermediate 2FA token returned from `/v2/users/login` API. Example: eyJhbGciOiJIUzI1
            NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2Q
            T4fwpMeJf36POk6yJV_adQssw5c.
        code (str): The Time-based One-Time Password of the Docker Hub account to authenticate with. Example: 123456.
    """

    login_2fa_token: str
    code: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        login_2fa_token = self.login_2fa_token
        code = self.code

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "login_2fa_token": login_2fa_token,
                "code": code,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        login_2fa_token = d.pop("login_2fa_token")

        code = d.pop("code")

        users_2fa_login_request = cls(
            login_2fa_token=login_2fa_token,
            code=code,
        )

        users_2fa_login_request.additional_properties = d
        return users_2fa_login_request

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
