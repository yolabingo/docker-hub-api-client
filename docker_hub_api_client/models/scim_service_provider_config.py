from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.scim_service_provider_config_authentication_schemes import ScimServiceProviderConfigAuthenticationSchemes
from ..models.scim_service_provider_config_bulk import ScimServiceProviderConfigBulk
from ..models.scim_service_provider_config_change_password import ScimServiceProviderConfigChangePassword
from ..models.scim_service_provider_config_etag import ScimServiceProviderConfigEtag
from ..models.scim_service_provider_config_filter import ScimServiceProviderConfigFilter
from ..models.scim_service_provider_config_sort import ScimServiceProviderConfigSort
from ..types import UNSET, Unset

T = TypeVar("T", bound="ScimServiceProviderConfig")


@attr.s(auto_attribs=True)
class ScimServiceProviderConfig:
    """
    Attributes:
        schemas (Union[Unset, List[str]]):  Example: ['urn:ietf:params:scim:schemas:core:2.0:ServiceProviderConfig'].
        documentation_uri (Union[Unset, str]):
        patch (Union[Unset, Any]):
        bulk (Union[Unset, ScimServiceProviderConfigBulk]):
        filter_ (Union[Unset, ScimServiceProviderConfigFilter]):
        change_password (Union[Unset, ScimServiceProviderConfigChangePassword]):
        sort (Union[Unset, ScimServiceProviderConfigSort]):
        etag (Union[Unset, ScimServiceProviderConfigEtag]):
        authentication_schemes (Union[Unset, ScimServiceProviderConfigAuthenticationSchemes]):
    """

    schemas: Union[Unset, List[str]] = UNSET
    documentation_uri: Union[Unset, str] = UNSET
    patch: Union[Unset, Any] = UNSET
    bulk: Union[Unset, ScimServiceProviderConfigBulk] = UNSET
    filter_: Union[Unset, ScimServiceProviderConfigFilter] = UNSET
    change_password: Union[Unset, ScimServiceProviderConfigChangePassword] = UNSET
    sort: Union[Unset, ScimServiceProviderConfigSort] = UNSET
    etag: Union[Unset, ScimServiceProviderConfigEtag] = UNSET
    authentication_schemes: Union[Unset, ScimServiceProviderConfigAuthenticationSchemes] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        schemas: Union[Unset, List[str]] = UNSET
        if not isinstance(self.schemas, Unset):
            schemas = self.schemas

        documentation_uri = self.documentation_uri
        patch = self.patch
        bulk: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.bulk, Unset):
            bulk = self.bulk.to_dict()

        filter_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.to_dict()

        change_password: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.change_password, Unset):
            change_password = self.change_password.to_dict()

        sort: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sort, Unset):
            sort = self.sort.to_dict()

        etag: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.etag, Unset):
            etag = self.etag.to_dict()

        authentication_schemes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.authentication_schemes, Unset):
            authentication_schemes = self.authentication_schemes.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if schemas is not UNSET:
            field_dict["schemas"] = schemas
        if documentation_uri is not UNSET:
            field_dict["documentationUri"] = documentation_uri
        if patch is not UNSET:
            field_dict["patch"] = patch
        if bulk is not UNSET:
            field_dict["bulk"] = bulk
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if change_password is not UNSET:
            field_dict["changePassword"] = change_password
        if sort is not UNSET:
            field_dict["sort"] = sort
        if etag is not UNSET:
            field_dict["etag"] = etag
        if authentication_schemes is not UNSET:
            field_dict["authenticationSchemes"] = authentication_schemes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        schemas = cast(List[str], d.pop("schemas", UNSET))

        documentation_uri = d.pop("documentationUri", UNSET)

        patch = d.pop("patch", UNSET)

        _bulk = d.pop("bulk", UNSET)
        bulk: Union[Unset, ScimServiceProviderConfigBulk]
        if isinstance(_bulk, Unset):
            bulk = UNSET
        else:
            bulk = ScimServiceProviderConfigBulk.from_dict(_bulk)

        _filter_ = d.pop("filter", UNSET)
        filter_: Union[Unset, ScimServiceProviderConfigFilter]
        if isinstance(_filter_, Unset):
            filter_ = UNSET
        else:
            filter_ = ScimServiceProviderConfigFilter.from_dict(_filter_)

        _change_password = d.pop("changePassword", UNSET)
        change_password: Union[Unset, ScimServiceProviderConfigChangePassword]
        if isinstance(_change_password, Unset):
            change_password = UNSET
        else:
            change_password = ScimServiceProviderConfigChangePassword.from_dict(_change_password)

        _sort = d.pop("sort", UNSET)
        sort: Union[Unset, ScimServiceProviderConfigSort]
        if isinstance(_sort, Unset):
            sort = UNSET
        else:
            sort = ScimServiceProviderConfigSort.from_dict(_sort)

        _etag = d.pop("etag", UNSET)
        etag: Union[Unset, ScimServiceProviderConfigEtag]
        if isinstance(_etag, Unset):
            etag = UNSET
        else:
            etag = ScimServiceProviderConfigEtag.from_dict(_etag)

        _authentication_schemes = d.pop("authenticationSchemes", UNSET)
        authentication_schemes: Union[Unset, ScimServiceProviderConfigAuthenticationSchemes]
        if isinstance(_authentication_schemes, Unset):
            authentication_schemes = UNSET
        else:
            authentication_schemes = ScimServiceProviderConfigAuthenticationSchemes.from_dict(_authentication_schemes)

        scim_service_provider_config = cls(
            schemas=schemas,
            documentation_uri=documentation_uri,
            patch=patch,
            bulk=bulk,
            filter_=filter_,
            change_password=change_password,
            sort=sort,
            etag=etag,
            authentication_schemes=authentication_schemes,
        )

        scim_service_provider_config.additional_properties = d
        return scim_service_provider_config

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
