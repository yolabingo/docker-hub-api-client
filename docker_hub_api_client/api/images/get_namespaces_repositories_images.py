from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.error_response import ErrorResponse
from ...models.get_namespace_repository_images_response import GetNamespaceRepositoryImagesResponse
from ...models.get_namespaces_repositories_images_ordering import GetNamespacesRepositoriesImagesOrdering
from ...models.get_namespaces_repositories_images_status import GetNamespacesRepositoriesImagesStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    namespace: str,
    repository: str,
    *,
    client: Client,
    status: Union[Unset, None, GetNamespacesRepositoriesImagesStatus] = UNSET,
    currently_tagged: Union[Unset, None, bool] = UNSET,
    ordering: Union[Unset, None, GetNamespacesRepositoriesImagesOrdering] = UNSET,
    active_from: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/v2/namespaces/{namespace}/repositories/{repository}/images".format(
        client.base_url, namespace=namespace, repository=repository
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_status: Union[Unset, None, str] = UNSET
    if not isinstance(status, Unset):
        json_status = status.value if status else None

    params["status"] = json_status

    params["currently_tagged"] = currently_tagged

    json_ordering: Union[Unset, None, str] = UNSET
    if not isinstance(ordering, Unset):
        json_ordering = ordering.value if ordering else None

    params["ordering"] = json_ordering

    params["active_from"] = active_from

    params["page"] = page

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[ErrorResponse, GetNamespaceRepositoryImagesResponse]]:
    if response.status_code == 200:
        response_200 = GetNamespaceRepositoryImagesResponse.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[ErrorResponse, GetNamespaceRepositoryImagesResponse]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    namespace: str,
    repository: str,
    *,
    client: Client,
    status: Union[Unset, None, GetNamespacesRepositoriesImagesStatus] = UNSET,
    currently_tagged: Union[Unset, None, bool] = UNSET,
    ordering: Union[Unset, None, GetNamespacesRepositoriesImagesOrdering] = UNSET,
    active_from: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
) -> Response[Union[ErrorResponse, GetNamespaceRepositoryImagesResponse]]:
    """Get details of repository's images

     Gets details on the images in a repository.

    Args:
        namespace (str):
        repository (str):
        status (Union[Unset, None, GetNamespacesRepositoriesImagesStatus]):
        currently_tagged (Union[Unset, None, bool]):
        ordering (Union[Unset, None, GetNamespacesRepositoriesImagesOrdering]):
        active_from (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):

    Returns:
        Response[Union[ErrorResponse, GetNamespaceRepositoryImagesResponse]]
    """

    kwargs = _get_kwargs(
        namespace=namespace,
        repository=repository,
        client=client,
        status=status,
        currently_tagged=currently_tagged,
        ordering=ordering,
        active_from=active_from,
        page=page,
        page_size=page_size,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    namespace: str,
    repository: str,
    *,
    client: Client,
    status: Union[Unset, None, GetNamespacesRepositoriesImagesStatus] = UNSET,
    currently_tagged: Union[Unset, None, bool] = UNSET,
    ordering: Union[Unset, None, GetNamespacesRepositoriesImagesOrdering] = UNSET,
    active_from: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
) -> Optional[Union[ErrorResponse, GetNamespaceRepositoryImagesResponse]]:
    """Get details of repository's images

     Gets details on the images in a repository.

    Args:
        namespace (str):
        repository (str):
        status (Union[Unset, None, GetNamespacesRepositoriesImagesStatus]):
        currently_tagged (Union[Unset, None, bool]):
        ordering (Union[Unset, None, GetNamespacesRepositoriesImagesOrdering]):
        active_from (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):

    Returns:
        Response[Union[ErrorResponse, GetNamespaceRepositoryImagesResponse]]
    """

    return sync_detailed(
        namespace=namespace,
        repository=repository,
        client=client,
        status=status,
        currently_tagged=currently_tagged,
        ordering=ordering,
        active_from=active_from,
        page=page,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    namespace: str,
    repository: str,
    *,
    client: Client,
    status: Union[Unset, None, GetNamespacesRepositoriesImagesStatus] = UNSET,
    currently_tagged: Union[Unset, None, bool] = UNSET,
    ordering: Union[Unset, None, GetNamespacesRepositoriesImagesOrdering] = UNSET,
    active_from: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
) -> Response[Union[ErrorResponse, GetNamespaceRepositoryImagesResponse]]:
    """Get details of repository's images

     Gets details on the images in a repository.

    Args:
        namespace (str):
        repository (str):
        status (Union[Unset, None, GetNamespacesRepositoriesImagesStatus]):
        currently_tagged (Union[Unset, None, bool]):
        ordering (Union[Unset, None, GetNamespacesRepositoriesImagesOrdering]):
        active_from (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):

    Returns:
        Response[Union[ErrorResponse, GetNamespaceRepositoryImagesResponse]]
    """

    kwargs = _get_kwargs(
        namespace=namespace,
        repository=repository,
        client=client,
        status=status,
        currently_tagged=currently_tagged,
        ordering=ordering,
        active_from=active_from,
        page=page,
        page_size=page_size,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    namespace: str,
    repository: str,
    *,
    client: Client,
    status: Union[Unset, None, GetNamespacesRepositoriesImagesStatus] = UNSET,
    currently_tagged: Union[Unset, None, bool] = UNSET,
    ordering: Union[Unset, None, GetNamespacesRepositoriesImagesOrdering] = UNSET,
    active_from: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
) -> Optional[Union[ErrorResponse, GetNamespaceRepositoryImagesResponse]]:
    """Get details of repository's images

     Gets details on the images in a repository.

    Args:
        namespace (str):
        repository (str):
        status (Union[Unset, None, GetNamespacesRepositoriesImagesStatus]):
        currently_tagged (Union[Unset, None, bool]):
        ordering (Union[Unset, None, GetNamespacesRepositoriesImagesOrdering]):
        active_from (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):

    Returns:
        Response[Union[ErrorResponse, GetNamespaceRepositoryImagesResponse]]
    """

    return (
        await asyncio_detailed(
            namespace=namespace,
            repository=repository,
            client=client,
            status=status,
            currently_tagged=currently_tagged,
            ordering=ordering,
            active_from=active_from,
            page=page,
            page_size=page_size,
        )
    ).parsed
