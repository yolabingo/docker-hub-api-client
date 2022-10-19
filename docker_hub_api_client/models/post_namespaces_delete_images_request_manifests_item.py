from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="PostNamespacesDeleteImagesRequestManifestsItem")


@attr.s(auto_attribs=True)
class PostNamespacesDeleteImagesRequestManifestsItem:
    """
    Attributes:
        repository (str): Name of the repository to delete the image from. Example: myrepo.
        digest (str): Digest of the image to delete. Example:
            sha256:1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqr.
    """

    repository: str
    digest: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        repository = self.repository
        digest = self.digest

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "repository": repository,
                "digest": digest,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        repository = d.pop("repository")

        digest = d.pop("digest")

        post_namespaces_delete_images_request_manifests_item = cls(
            repository=repository,
            digest=digest,
        )

        post_namespaces_delete_images_request_manifests_item.additional_properties = d
        return post_namespaces_delete_images_request_manifests_item

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
