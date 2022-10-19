from typing import Any, Dict

import httpx

from ...client import Client
from ...models.patch_access_token_request import PatchAccessTokenRequest
from ...types import Response


def _get_kwargs(
    uuid: str,
    *,
    client: Client,
    json_body: PatchAccessTokenRequest,
) -> Dict[str, Any]:
    url = "{}/v2/access-tokens/{uuid}".format(client.base_url, uuid=uuid)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "patch",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    uuid: str,
    *,
    client: Client,
    json_body: PatchAccessTokenRequest,
) -> Response[Any]:
    """Update a personal access token

     Updates a personal access token partially. You can either update the
    token's label or enable/disable it.

    Args:
        uuid (str):
        json_body (PatchAccessTokenRequest):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    uuid: str,
    *,
    client: Client,
    json_body: PatchAccessTokenRequest,
) -> Response[Any]:
    """Update a personal access token

     Updates a personal access token partially. You can either update the
    token's label or enable/disable it.

    Args:
        uuid (str):
        json_body (PatchAccessTokenRequest):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
