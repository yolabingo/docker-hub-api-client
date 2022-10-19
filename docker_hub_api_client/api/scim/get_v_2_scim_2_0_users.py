from typing import Any, Dict, Union

import httpx

from ...client import AuthenticatedClient
from ...models.get_v2_scim_20_users_sort_order import GetV2Scim20UsersSortOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    start_index: Union[Unset, None, int] = UNSET,
    count: Union[Unset, None, int] = UNSET,
    filter_: Union[Unset, None, str] = UNSET,
    attributes: str,
    sort_order: Union[Unset, None, GetV2Scim20UsersSortOrder] = UNSET,
    sort_by: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/v2/scim/2.0/Users".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["startIndex"] = start_index

    params["count"] = count

    params["filter"] = filter_

    params["attributes"] = attributes

    json_sort_order: Union[Unset, None, str] = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value if sort_order else None

    params["sortOrder"] = json_sort_order

    params["sortBy"] = sort_by

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
    *,
    client: AuthenticatedClient,
    start_index: Union[Unset, None, int] = UNSET,
    count: Union[Unset, None, int] = UNSET,
    filter_: Union[Unset, None, str] = UNSET,
    attributes: str,
    sort_order: Union[Unset, None, GetV2Scim20UsersSortOrder] = UNSET,
    sort_by: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """List users

     List users, returns paginated users for an organization. Use `startIndex`
    and `count` query parameters to receive paginated results.

    **Sorting:**<br>
    Sorting lets you to specify the order of returned resources by specifying
    a combination of `sortBy` and `sortOrder` query parameters.

    The `sortBy` parameter specifies the attribute whose value will be used
    to order the returned responses. The `sortOrder` parameter defines the
    order in which the `sortBy` parameter is applied. Allowed values are
    \"ascending\" and \"descending\".

    **Filtering:**<br>
    You can request a subset of resources by specifying the `filter` query
    parameter containing a filter expression. Attribute names and attribute
    operators used in filters are case insensitive. The filter parameter
    must contain at least one valid expression. Each expression must contain
    an attribute name followed by an attribute operator and an optional
    value.

    Supported operators are listed below.

    - `eq` equal
    - `ne` not equal
    - `co` contains
    - `sw` starts with
    - `and` Logical \"and\"
    - `or` Logical \"or\"
    - `not` \"Not\" function
    - `()` Precedence grouping

    Args:
        start_index (Union[Unset, None, int]):
        count (Union[Unset, None, int]):
        filter_ (Union[Unset, None, str]):
        attributes (str):
        sort_order (Union[Unset, None, GetV2Scim20UsersSortOrder]):
        sort_by (Union[Unset, None, str]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        start_index=start_index,
        count=count,
        filter_=filter_,
        attributes=attributes,
        sort_order=sort_order,
        sort_by=sort_by,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    start_index: Union[Unset, None, int] = UNSET,
    count: Union[Unset, None, int] = UNSET,
    filter_: Union[Unset, None, str] = UNSET,
    attributes: str,
    sort_order: Union[Unset, None, GetV2Scim20UsersSortOrder] = UNSET,
    sort_by: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """List users

     List users, returns paginated users for an organization. Use `startIndex`
    and `count` query parameters to receive paginated results.

    **Sorting:**<br>
    Sorting lets you to specify the order of returned resources by specifying
    a combination of `sortBy` and `sortOrder` query parameters.

    The `sortBy` parameter specifies the attribute whose value will be used
    to order the returned responses. The `sortOrder` parameter defines the
    order in which the `sortBy` parameter is applied. Allowed values are
    \"ascending\" and \"descending\".

    **Filtering:**<br>
    You can request a subset of resources by specifying the `filter` query
    parameter containing a filter expression. Attribute names and attribute
    operators used in filters are case insensitive. The filter parameter
    must contain at least one valid expression. Each expression must contain
    an attribute name followed by an attribute operator and an optional
    value.

    Supported operators are listed below.

    - `eq` equal
    - `ne` not equal
    - `co` contains
    - `sw` starts with
    - `and` Logical \"and\"
    - `or` Logical \"or\"
    - `not` \"Not\" function
    - `()` Precedence grouping

    Args:
        start_index (Union[Unset, None, int]):
        count (Union[Unset, None, int]):
        filter_ (Union[Unset, None, str]):
        attributes (str):
        sort_order (Union[Unset, None, GetV2Scim20UsersSortOrder]):
        sort_by (Union[Unset, None, str]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        start_index=start_index,
        count=count,
        filter_=filter_,
        attributes=attributes,
        sort_order=sort_order,
        sort_by=sort_by,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
