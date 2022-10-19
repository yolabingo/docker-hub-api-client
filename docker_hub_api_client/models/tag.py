from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.image import Image
from ..models.tag_status import TagStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="Tag")


@attr.s(auto_attribs=True)
class Tag:
    """
    Attributes:
        id (Union[Unset, int]): tag ID
        images (Union[Unset, Image]):
        creator (Union[Unset, int]): ID of the user that pushed the tag
        last_updated (Union[Unset, None, str]): datetime of last update Example: 2021-01-05T21:06:53.506400Z.
        last_updater (Union[Unset, int]): ID of the last user that updated the tag
        last_updater_username (Union[Unset, str]): Hub username of the user that updated the tag
        name (Union[Unset, str]): name of the tag
        repository (Union[Unset, int]): repository ID
        full_size (Union[Unset, int]): compressed size (sum of all layers) of the tagged image
        v2 (Union[Unset, str]): repository API version
        status (Union[Unset, TagStatus]): whether a tag has been pushed to or pulled in the past month
        tag_last_pulled (Union[Unset, None, str]): datetime of last pull Example: 2021-01-05T21:06:53.506400Z.
        tag_last_pushed (Union[Unset, None, str]): datetime of last push Example: 2021-01-05T21:06:53.506400Z.
    """

    id: Union[Unset, int] = UNSET
    images: Union[Unset, Image] = UNSET
    creator: Union[Unset, int] = UNSET
    last_updated: Union[Unset, None, str] = UNSET
    last_updater: Union[Unset, int] = UNSET
    last_updater_username: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    repository: Union[Unset, int] = UNSET
    full_size: Union[Unset, int] = UNSET
    v2: Union[Unset, str] = UNSET
    status: Union[Unset, TagStatus] = UNSET
    tag_last_pulled: Union[Unset, None, str] = UNSET
    tag_last_pushed: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        images: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.images, Unset):
            images = self.images.to_dict()

        creator = self.creator
        last_updated = self.last_updated
        last_updater = self.last_updater
        last_updater_username = self.last_updater_username
        name = self.name
        repository = self.repository
        full_size = self.full_size
        v2 = self.v2
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        tag_last_pulled = self.tag_last_pulled
        tag_last_pushed = self.tag_last_pushed

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if images is not UNSET:
            field_dict["images"] = images
        if creator is not UNSET:
            field_dict["creator"] = creator
        if last_updated is not UNSET:
            field_dict["last_updated"] = last_updated
        if last_updater is not UNSET:
            field_dict["last_updater"] = last_updater
        if last_updater_username is not UNSET:
            field_dict["last_updater_username"] = last_updater_username
        if name is not UNSET:
            field_dict["name"] = name
        if repository is not UNSET:
            field_dict["repository"] = repository
        if full_size is not UNSET:
            field_dict["full_size"] = full_size
        if v2 is not UNSET:
            field_dict["v2"] = v2
        if status is not UNSET:
            field_dict["status"] = status
        if tag_last_pulled is not UNSET:
            field_dict["tag_last_pulled"] = tag_last_pulled
        if tag_last_pushed is not UNSET:
            field_dict["tag_last_pushed"] = tag_last_pushed

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _images = d.pop("images", UNSET)
        images: Union[Unset, Image]
        if isinstance(_images, Unset):
            images = UNSET
        else:
            images = Image.from_dict(_images)

        creator = d.pop("creator", UNSET)

        last_updated = d.pop("last_updated", UNSET)

        last_updater = d.pop("last_updater", UNSET)

        last_updater_username = d.pop("last_updater_username", UNSET)

        name = d.pop("name", UNSET)

        repository = d.pop("repository", UNSET)

        full_size = d.pop("full_size", UNSET)

        v2 = d.pop("v2", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, TagStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = TagStatus(_status)

        tag_last_pulled = d.pop("tag_last_pulled", UNSET)

        tag_last_pushed = d.pop("tag_last_pushed", UNSET)

        tag = cls(
            id=id,
            images=images,
            creator=creator,
            last_updated=last_updated,
            last_updater=last_updater,
            last_updater_username=last_updater_username,
            name=name,
            repository=repository,
            full_size=full_size,
            v2=v2,
            status=status,
            tag_last_pulled=tag_last_pulled,
            tag_last_pushed=tag_last_pushed,
        )

        tag.additional_properties = d
        return tag

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
