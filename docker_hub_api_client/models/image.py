from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.image_status import ImageStatus
from ..models.layer import Layer
from ..types import UNSET, Unset

T = TypeVar("T", bound="Image")


@attr.s(auto_attribs=True)
class Image:
    """
    Attributes:
        architecture (Union[Unset, str]): CPU architecture
        features (Union[Unset, str]): CPU features
        variant (Union[Unset, str]): CPU variant
        digest (Union[Unset, None, str]): image digest
        layers (Union[Unset, List[Layer]]):
        os (Union[Unset, str]): operating system
        os_features (Union[Unset, str]): OS features
        os_version (Union[Unset, str]): OS version
        size (Union[Unset, int]): size of the image
        status (Union[Unset, ImageStatus]): Status of the image
        last_pulled (Union[Unset, None, str]): datetime of last pull Example: 2021-01-05T21:06:53.506400Z.
        last_pushed (Union[Unset, None, str]): datetime of last push Example: 2021-01-05T21:06:53.506400Z.
    """

    architecture: Union[Unset, str] = UNSET
    features: Union[Unset, str] = UNSET
    variant: Union[Unset, str] = UNSET
    digest: Union[Unset, None, str] = UNSET
    layers: Union[Unset, List[Layer]] = UNSET
    os: Union[Unset, str] = UNSET
    os_features: Union[Unset, str] = UNSET
    os_version: Union[Unset, str] = UNSET
    size: Union[Unset, int] = UNSET
    status: Union[Unset, ImageStatus] = UNSET
    last_pulled: Union[Unset, None, str] = UNSET
    last_pushed: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        architecture = self.architecture
        features = self.features
        variant = self.variant
        digest = self.digest
        layers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.layers, Unset):
            layers = []
            for layers_item_data in self.layers:
                layers_item = layers_item_data.to_dict()

                layers.append(layers_item)

        os = self.os
        os_features = self.os_features
        os_version = self.os_version
        size = self.size
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        last_pulled = self.last_pulled
        last_pushed = self.last_pushed

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if architecture is not UNSET:
            field_dict["architecture"] = architecture
        if features is not UNSET:
            field_dict["features"] = features
        if variant is not UNSET:
            field_dict["variant"] = variant
        if digest is not UNSET:
            field_dict["digest"] = digest
        if layers is not UNSET:
            field_dict["layers"] = layers
        if os is not UNSET:
            field_dict["os"] = os
        if os_features is not UNSET:
            field_dict["os_features"] = os_features
        if os_version is not UNSET:
            field_dict["os_version"] = os_version
        if size is not UNSET:
            field_dict["size"] = size
        if status is not UNSET:
            field_dict["status"] = status
        if last_pulled is not UNSET:
            field_dict["last_pulled"] = last_pulled
        if last_pushed is not UNSET:
            field_dict["last_pushed"] = last_pushed

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        architecture = d.pop("architecture", UNSET)

        features = d.pop("features", UNSET)

        variant = d.pop("variant", UNSET)

        digest = d.pop("digest", UNSET)

        layers = []
        _layers = d.pop("layers", UNSET)
        for layers_item_data in _layers or []:
            layers_item = Layer.from_dict(layers_item_data)

            layers.append(layers_item)

        os = d.pop("os", UNSET)

        os_features = d.pop("os_features", UNSET)

        os_version = d.pop("os_version", UNSET)

        size = d.pop("size", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, ImageStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ImageStatus(_status)

        last_pulled = d.pop("last_pulled", UNSET)

        last_pushed = d.pop("last_pushed", UNSET)

        image = cls(
            architecture=architecture,
            features=features,
            variant=variant,
            digest=digest,
            layers=layers,
            os=os,
            os_features=os_features,
            os_version=os_version,
            size=size,
            status=status,
            last_pulled=last_pulled,
            last_pushed=last_pushed,
        )

        image.additional_properties = d
        return image

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
