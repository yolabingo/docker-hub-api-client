from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.get_audit_actions_response import GetAuditActionsResponse
from ...types import Response


def _get_kwargs(
    account: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/v2/auditlogs/{account}/actions".format(client.base_url, account=account)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, GetAuditActionsResponse]]:
    if response.status_code == 200:
        response_200 = GetAuditActionsResponse.from_dict(response.json())

        return response_200
    if response.status_code == 429:
        response_429 = cast(Any, response.json())
        return response_429
    if response.status_code == 500:
        response_500 = cast(Any, response.json())
        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, GetAuditActionsResponse]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    account: str,
    *,
    client: Client,
) -> Response[Union[Any, GetAuditActionsResponse]]:
    """Returns list of audit log actions.

     Get audit log actions for a namespace to be used as a filter for querying audit events.

    Args:
        account (str):

    Returns:
        Response[Union[Any, GetAuditActionsResponse]]
    """

    kwargs = _get_kwargs(
        account=account,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    account: str,
    *,
    client: Client,
) -> Optional[Union[Any, GetAuditActionsResponse]]:
    """Returns list of audit log actions.

     Get audit log actions for a namespace to be used as a filter for querying audit events.

    Args:
        account (str):

    Returns:
        Response[Union[Any, GetAuditActionsResponse]]
    """

    return sync_detailed(
        account=account,
        client=client,
    ).parsed


async def asyncio_detailed(
    account: str,
    *,
    client: Client,
) -> Response[Union[Any, GetAuditActionsResponse]]:
    """Returns list of audit log actions.

     Get audit log actions for a namespace to be used as a filter for querying audit events.

    Args:
        account (str):

    Returns:
        Response[Union[Any, GetAuditActionsResponse]]
    """

    kwargs = _get_kwargs(
        account=account,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    account: str,
    *,
    client: Client,
) -> Optional[Union[Any, GetAuditActionsResponse]]:
    """Returns list of audit log actions.

     Get audit log actions for a namespace to be used as a filter for querying audit events.

    Args:
        account (str):

    Returns:
        Response[Union[Any, GetAuditActionsResponse]]
    """

    return (
        await asyncio_detailed(
            account=account,
            client=client,
        )
    ).parsed
