from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="UsersLoginRequest")


@attr.s(auto_attribs=True)
class UsersLoginRequest:
    """User login details

    Attributes:
        username (str): The username of the Docker Hub account to authenticate with. Example: myusername.
        password (str): The password or personal access token (PAT) of the Docker Hub account to authenticate with.
            Example: hunter2.
    """

    username: str
    password: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        username = self.username
        password = self.password

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "username": username,
                "password": password,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        username = d.pop("username")

        password = d.pop("password")

        users_login_request = cls(
            username=username,
            password=password,
        )

        users_login_request.additional_properties = d
        return users_login_request

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
