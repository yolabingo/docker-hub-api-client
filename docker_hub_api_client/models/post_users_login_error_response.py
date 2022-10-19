from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostUsersLoginErrorResponse")


@attr.s(auto_attribs=True)
class PostUsersLoginErrorResponse:
    """failed user login response or second factor required

    Attributes:
        detail (str): Description of the error. Example: Incorrect authentication credentials.
        login_2fa_token (Union[Unset, None, str]): Short time lived token to be used on `/v2/users/2fa-login` to
            complete the authentication. This field is present only if 2FA is enabled. Example: eyJhbGciOiJIUzI1NiIsInR5cCI6
            IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36P
            Ok6yJV_adQssw5c.
    """

    detail: str
    login_2fa_token: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        detail = self.detail
        login_2fa_token = self.login_2fa_token

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "detail": detail,
            }
        )
        if login_2fa_token is not UNSET:
            field_dict["login_2fa_token"] = login_2fa_token

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        detail = d.pop("detail")

        login_2fa_token = d.pop("login_2fa_token", UNSET)

        post_users_login_error_response = cls(
            detail=detail,
            login_2fa_token=login_2fa_token,
        )

        post_users_login_error_response.additional_properties = d
        return post_users_login_error_response

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
