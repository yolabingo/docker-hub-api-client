from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.org_settings import OrgSettings
from ...types import Response


def _get_kwargs(
    name: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/v2/orgs/{name}/settings".format(client.base_url, name=name)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, OrgSettings]]:
    if response.status_code == 200:
        response_200 = OrgSettings.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, OrgSettings]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    name: str,
    *,
    client: Client,
) -> Response[Union[Any, OrgSettings]]:
    """Get organization settings

     Returns organization settings by name.

    Args:
        name (str):

    Returns:
        Response[Union[Any, OrgSettings]]
    """

    kwargs = _get_kwargs(
        name=name,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    name: str,
    *,
    client: Client,
) -> Optional[Union[Any, OrgSettings]]:
    """Get organization settings

     Returns organization settings by name.

    Args:
        name (str):

    Returns:
        Response[Union[Any, OrgSettings]]
    """

    return sync_detailed(
        name=name,
        client=client,
    ).parsed


async def asyncio_detailed(
    name: str,
    *,
    client: Client,
) -> Response[Union[Any, OrgSettings]]:
    """Get organization settings

     Returns organization settings by name.

    Args:
        name (str):

    Returns:
        Response[Union[Any, OrgSettings]]
    """

    kwargs = _get_kwargs(
        name=name,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    name: str,
    *,
    client: Client,
) -> Optional[Union[Any, OrgSettings]]:
    """Get organization settings

     Returns organization settings by name.

    Args:
        name (str):

    Returns:
        Response[Union[Any, OrgSettings]]
    """

    return (
        await asyncio_detailed(
            name=name,
            client=client,
        )
    ).parsed
