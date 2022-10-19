from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.error_response import ErrorResponse
from ...models.get_namespace_repository_images_tags_response import GetNamespaceRepositoryImagesTagsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    namespace: str,
    repository: str,
    digest: str,
    *,
    client: Client,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/v2/namespaces/{namespace}/repositories/{repository}/images/{digest}/tags".format(
        client.base_url, namespace=namespace, repository=repository, digest=digest
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
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
) -> Optional[Union[ErrorResponse, GetNamespaceRepositoryImagesTagsResponse]]:
    if response.status_code == 200:
        response_200 = GetNamespaceRepositoryImagesTagsResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, GetNamespaceRepositoryImagesTagsResponse]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    namespace: str,
    repository: str,
    digest: str,
    *,
    client: Client,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
) -> Response[Union[ErrorResponse, GetNamespaceRepositoryImagesTagsResponse]]:
    """Get image's tags

     Gets current and historical tags for an image.

    Args:
        namespace (str):
        repository (str):
        digest (str):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):

    Returns:
        Response[Union[ErrorResponse, GetNamespaceRepositoryImagesTagsResponse]]
    """

    kwargs = _get_kwargs(
        namespace=namespace,
        repository=repository,
        digest=digest,
        client=client,
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
    digest: str,
    *,
    client: Client,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
) -> Optional[Union[ErrorResponse, GetNamespaceRepositoryImagesTagsResponse]]:
    """Get image's tags

     Gets current and historical tags for an image.

    Args:
        namespace (str):
        repository (str):
        digest (str):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):

    Returns:
        Response[Union[ErrorResponse, GetNamespaceRepositoryImagesTagsResponse]]
    """

    return sync_detailed(
        namespace=namespace,
        repository=repository,
        digest=digest,
        client=client,
        page=page,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    namespace: str,
    repository: str,
    digest: str,
    *,
    client: Client,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
) -> Response[Union[ErrorResponse, GetNamespaceRepositoryImagesTagsResponse]]:
    """Get image's tags

     Gets current and historical tags for an image.

    Args:
        namespace (str):
        repository (str):
        digest (str):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):

    Returns:
        Response[Union[ErrorResponse, GetNamespaceRepositoryImagesTagsResponse]]
    """

    kwargs = _get_kwargs(
        namespace=namespace,
        repository=repository,
        digest=digest,
        client=client,
        page=page,
        page_size=page_size,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    namespace: str,
    repository: str,
    digest: str,
    *,
    client: Client,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
) -> Optional[Union[ErrorResponse, GetNamespaceRepositoryImagesTagsResponse]]:
    """Get image's tags

     Gets current and historical tags for an image.

    Args:
        namespace (str):
        repository (str):
        digest (str):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):

    Returns:
        Response[Union[ErrorResponse, GetNamespaceRepositoryImagesTagsResponse]]
    """

    return (
        await asyncio_detailed(
            namespace=namespace,
            repository=repository,
            digest=digest,
            client=client,
            page=page,
            page_size=page_size,
        )
    ).parsed
