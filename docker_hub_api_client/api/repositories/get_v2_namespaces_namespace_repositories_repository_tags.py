from typing import Any, Dict

import httpx

from ...client import Client
from ...types import UNSET, Response


def _get_kwargs(
    namespace: str,
    repository: str,
    *,
    client: Client,
    page: int,
    page_size: int,
) -> Dict[str, Any]:
    url = "{}/v2/namespaces/{namespace}/repositories/{repository}/tags".format(
        client.base_url, namespace=namespace, repository=repository
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


def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    namespace: str,
    repository: str,
    *,
    client: Client,
    page: int,
    page_size: int,
) -> Response[Any]:
    """List repository tags

    Args:
        namespace (str):
        repository (str):
        page (int):
        page_size (int):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        namespace=namespace,
        repository=repository,
        client=client,
        page=page,
        page_size=page_size,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    namespace: str,
    repository: str,
    *,
    client: Client,
    page: int,
    page_size: int,
) -> Response[Any]:
    """List repository tags

    Args:
        namespace (str):
        repository (str):
        page (int):
        page_size (int):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        namespace=namespace,
        repository=repository,
        client=client,
        page=page,
        page_size=page_size,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
