from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.error_response import ErrorResponse
from ...models.get_namespace_repository_images_summary_response import GetNamespaceRepositoryImagesSummaryResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    namespace: str,
    repository: str,
    *,
    client: Client,
    active_from: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/v2/namespaces/{namespace}/repositories/{repository}/images-summary".format(
        client.base_url, namespace=namespace, repository=repository
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["active_from"] = active_from

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
) -> Optional[Union[ErrorResponse, GetNamespaceRepositoryImagesSummaryResponse]]:
    if response.status_code == 200:
        response_200 = GetNamespaceRepositoryImagesSummaryResponse.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[ErrorResponse, GetNamespaceRepositoryImagesSummaryResponse]]:
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
    active_from: Union[Unset, None, str] = UNSET,
) -> Response[Union[ErrorResponse, GetNamespaceRepositoryImagesSummaryResponse]]:
    """Get summary of repository's images

     Gets the number of images in a repository and the number of images
    counted as active and inactive.

    Args:
        namespace (str):
        repository (str):
        active_from (Union[Unset, None, str]):

    Returns:
        Response[Union[ErrorResponse, GetNamespaceRepositoryImagesSummaryResponse]]
    """

    kwargs = _get_kwargs(
        namespace=namespace,
        repository=repository,
        client=client,
        active_from=active_from,
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
    active_from: Union[Unset, None, str] = UNSET,
) -> Optional[Union[ErrorResponse, GetNamespaceRepositoryImagesSummaryResponse]]:
    """Get summary of repository's images

     Gets the number of images in a repository and the number of images
    counted as active and inactive.

    Args:
        namespace (str):
        repository (str):
        active_from (Union[Unset, None, str]):

    Returns:
        Response[Union[ErrorResponse, GetNamespaceRepositoryImagesSummaryResponse]]
    """

    return sync_detailed(
        namespace=namespace,
        repository=repository,
        client=client,
        active_from=active_from,
    ).parsed


async def asyncio_detailed(
    namespace: str,
    repository: str,
    *,
    client: Client,
    active_from: Union[Unset, None, str] = UNSET,
) -> Response[Union[ErrorResponse, GetNamespaceRepositoryImagesSummaryResponse]]:
    """Get summary of repository's images

     Gets the number of images in a repository and the number of images
    counted as active and inactive.

    Args:
        namespace (str):
        repository (str):
        active_from (Union[Unset, None, str]):

    Returns:
        Response[Union[ErrorResponse, GetNamespaceRepositoryImagesSummaryResponse]]
    """

    kwargs = _get_kwargs(
        namespace=namespace,
        repository=repository,
        client=client,
        active_from=active_from,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    namespace: str,
    repository: str,
    *,
    client: Client,
    active_from: Union[Unset, None, str] = UNSET,
) -> Optional[Union[ErrorResponse, GetNamespaceRepositoryImagesSummaryResponse]]:
    """Get summary of repository's images

     Gets the number of images in a repository and the number of images
    counted as active and inactive.

    Args:
        namespace (str):
        repository (str):
        active_from (Union[Unset, None, str]):

    Returns:
        Response[Union[ErrorResponse, GetNamespaceRepositoryImagesSummaryResponse]]
    """

    return (
        await asyncio_detailed(
            namespace=namespace,
            repository=repository,
            client=client,
            active_from=active_from,
        )
    ).parsed
