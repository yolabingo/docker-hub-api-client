import datetime
from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.get_audit_logs_response import GetAuditLogsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    account: str,
    *,
    client: Client,
    action: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    actor: Union[Unset, None, str] = UNSET,
    from_: Union[Unset, None, datetime.datetime] = UNSET,
    to: Union[Unset, None, datetime.datetime] = UNSET,
    page: Union[Unset, None, int] = 1,
    page_size: Union[Unset, None, int] = 25,
) -> Dict[str, Any]:
    url = "{}/v2/auditlogs/{account}".format(client.base_url, account=account)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["action"] = action

    params["name"] = name

    params["actor"] = actor

    json_from_: Union[Unset, None, str] = UNSET
    if not isinstance(from_, Unset):
        json_from_ = from_.isoformat() if from_ else None

    params["from"] = json_from_

    json_to: Union[Unset, None, str] = UNSET
    if not isinstance(to, Unset):
        json_to = to.isoformat() if to else None

    params["to"] = json_to

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, GetAuditLogsResponse]]:
    if response.status_code == 200:
        response_200 = GetAuditLogsResponse.from_dict(response.json())

        return response_200
    if response.status_code == 429:
        response_429 = cast(Any, response.json())
        return response_429
    if response.status_code == 500:
        response_500 = cast(Any, response.json())
        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, GetAuditLogsResponse]]:
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
    action: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    actor: Union[Unset, None, str] = UNSET,
    from_: Union[Unset, None, datetime.datetime] = UNSET,
    to: Union[Unset, None, datetime.datetime] = UNSET,
    page: Union[Unset, None, int] = 1,
    page_size: Union[Unset, None, int] = 25,
) -> Response[Union[Any, GetAuditLogsResponse]]:
    """Returns list of audit log  events.

     Get audit log events for a given namespace.

    Args:
        account (str):
        action (Union[Unset, None, str]):
        name (Union[Unset, None, str]):
        actor (Union[Unset, None, str]):
        from_ (Union[Unset, None, datetime.datetime]):
        to (Union[Unset, None, datetime.datetime]):
        page (Union[Unset, None, int]):  Default: 1.
        page_size (Union[Unset, None, int]):  Default: 25.

    Returns:
        Response[Union[Any, GetAuditLogsResponse]]
    """

    kwargs = _get_kwargs(
        account=account,
        client=client,
        action=action,
        name=name,
        actor=actor,
        from_=from_,
        to=to,
        page=page,
        page_size=page_size,
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
    action: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    actor: Union[Unset, None, str] = UNSET,
    from_: Union[Unset, None, datetime.datetime] = UNSET,
    to: Union[Unset, None, datetime.datetime] = UNSET,
    page: Union[Unset, None, int] = 1,
    page_size: Union[Unset, None, int] = 25,
) -> Optional[Union[Any, GetAuditLogsResponse]]:
    """Returns list of audit log  events.

     Get audit log events for a given namespace.

    Args:
        account (str):
        action (Union[Unset, None, str]):
        name (Union[Unset, None, str]):
        actor (Union[Unset, None, str]):
        from_ (Union[Unset, None, datetime.datetime]):
        to (Union[Unset, None, datetime.datetime]):
        page (Union[Unset, None, int]):  Default: 1.
        page_size (Union[Unset, None, int]):  Default: 25.

    Returns:
        Response[Union[Any, GetAuditLogsResponse]]
    """

    return sync_detailed(
        account=account,
        client=client,
        action=action,
        name=name,
        actor=actor,
        from_=from_,
        to=to,
        page=page,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    account: str,
    *,
    client: Client,
    action: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    actor: Union[Unset, None, str] = UNSET,
    from_: Union[Unset, None, datetime.datetime] = UNSET,
    to: Union[Unset, None, datetime.datetime] = UNSET,
    page: Union[Unset, None, int] = 1,
    page_size: Union[Unset, None, int] = 25,
) -> Response[Union[Any, GetAuditLogsResponse]]:
    """Returns list of audit log  events.

     Get audit log events for a given namespace.

    Args:
        account (str):
        action (Union[Unset, None, str]):
        name (Union[Unset, None, str]):
        actor (Union[Unset, None, str]):
        from_ (Union[Unset, None, datetime.datetime]):
        to (Union[Unset, None, datetime.datetime]):
        page (Union[Unset, None, int]):  Default: 1.
        page_size (Union[Unset, None, int]):  Default: 25.

    Returns:
        Response[Union[Any, GetAuditLogsResponse]]
    """

    kwargs = _get_kwargs(
        account=account,
        client=client,
        action=action,
        name=name,
        actor=actor,
        from_=from_,
        to=to,
        page=page,
        page_size=page_size,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    account: str,
    *,
    client: Client,
    action: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    actor: Union[Unset, None, str] = UNSET,
    from_: Union[Unset, None, datetime.datetime] = UNSET,
    to: Union[Unset, None, datetime.datetime] = UNSET,
    page: Union[Unset, None, int] = 1,
    page_size: Union[Unset, None, int] = 25,
) -> Optional[Union[Any, GetAuditLogsResponse]]:
    """Returns list of audit log  events.

     Get audit log events for a given namespace.

    Args:
        account (str):
        action (Union[Unset, None, str]):
        name (Union[Unset, None, str]):
        actor (Union[Unset, None, str]):
        from_ (Union[Unset, None, datetime.datetime]):
        to (Union[Unset, None, datetime.datetime]):
        page (Union[Unset, None, int]):  Default: 1.
        page_size (Union[Unset, None, int]):  Default: 25.

    Returns:
        Response[Union[Any, GetAuditLogsResponse]]
    """

    return (
        await asyncio_detailed(
            account=account,
            client=client,
            action=action,
            name=name,
            actor=actor,
            from_=from_,
            to=to,
            page=page,
            page_size=page_size,
        )
    ).parsed
