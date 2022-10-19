from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ScimServiceProviderConfigAuthenticationSchemes")


@attr.s(auto_attribs=True)
class ScimServiceProviderConfigAuthenticationSchemes:
    """
    Attributes:
        name (Union[Unset, str]):  Example: OAuth 2.0 Bearer Token.
        description (Union[Unset, str]):  Example: The OAuth 2.0 Bearer Token Authentication scheme. OAuth enables
            clients to access protected resources by obtaining an access token, which is defined in RFC 6750 as "a string
            representing an access authorization issued to the client", rather than using the resource owner's credentials
            directly..
        spec_uri (Union[Unset, str]):  Example: http://tools.ietf.org/html/rfc6750.
        type (Union[Unset, str]):  Example: oauthbearertoken.
    """

    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    spec_uri: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        description = self.description
        spec_uri = self.spec_uri
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if spec_uri is not UNSET:
            field_dict["specUri"] = spec_uri
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        spec_uri = d.pop("specUri", UNSET)

        type = d.pop("type", UNSET)

        scim_service_provider_config_authentication_schemes = cls(
            name=name,
            description=description,
            spec_uri=spec_uri,
            type=type,
        )

        scim_service_provider_config_authentication_schemes.additional_properties = d
        return scim_service_provider_config_authentication_schemes

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
