from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.post_users_login_error_response import PostUsersLoginErrorResponse
from ...models.post_users_login_success_response import PostUsersLoginSuccessResponse
from ...models.users_login_request import UsersLoginRequest
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: UsersLoginRequest,
) -> Dict[str, Any]:
    url = "{}/v2/users/login".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[PostUsersLoginErrorResponse, PostUsersLoginSuccessResponse]]:
    if response.status_code == 200:
        response_200 = PostUsersLoginSuccessResponse.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = PostUsersLoginErrorResponse.from_dict(response.json())

        return response_401
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[PostUsersLoginErrorResponse, PostUsersLoginSuccessResponse]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: UsersLoginRequest,
) -> Response[Union[PostUsersLoginErrorResponse, PostUsersLoginSuccessResponse]]:
    """Create an authentication token

     Creates and returns a bearer token in JWT format that you can use to
    authenticate with Docker Hub APIs.

    The returned token is used in the HTTP Authorization header like `Authorization: Bearer {TOKEN}`.

    Most Docker Hub APIs require this token either to consume or to get detailed information. For
    example, to list images in a private repository.

    Args:
        json_body (UsersLoginRequest): User login details

    Returns:
        Response[Union[PostUsersLoginErrorResponse, PostUsersLoginSuccessResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    json_body: UsersLoginRequest,
) -> Optional[Union[PostUsersLoginErrorResponse, PostUsersLoginSuccessResponse]]:
    """Create an authentication token

     Creates and returns a bearer token in JWT format that you can use to
    authenticate with Docker Hub APIs.

    The returned token is used in the HTTP Authorization header like `Authorization: Bearer {TOKEN}`.

    Most Docker Hub APIs require this token either to consume or to get detailed information. For
    example, to list images in a private repository.

    Args:
        json_body (UsersLoginRequest): User login details

    Returns:
        Response[Union[PostUsersLoginErrorResponse, PostUsersLoginSuccessResponse]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: UsersLoginRequest,
) -> Response[Union[PostUsersLoginErrorResponse, PostUsersLoginSuccessResponse]]:
    """Create an authentication token

     Creates and returns a bearer token in JWT format that you can use to
    authenticate with Docker Hub APIs.

    The returned token is used in the HTTP Authorization header like `Authorization: Bearer {TOKEN}`.

    Most Docker Hub APIs require this token either to consume or to get detailed information. For
    example, to list images in a private repository.

    Args:
        json_body (UsersLoginRequest): User login details

    Returns:
        Response[Union[PostUsersLoginErrorResponse, PostUsersLoginSuccessResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: UsersLoginRequest,
) -> Optional[Union[PostUsersLoginErrorResponse, PostUsersLoginSuccessResponse]]:
    """Create an authentication token

     Creates and returns a bearer token in JWT format that you can use to
    authenticate with Docker Hub APIs.

    The returned token is used in the HTTP Authorization header like `Authorization: Bearer {TOKEN}`.

    Most Docker Hub APIs require this token either to consume or to get detailed information. For
    example, to list images in a private repository.

    Args:
        json_body (UsersLoginRequest): User login details

    Returns:
        Response[Union[PostUsersLoginErrorResponse, PostUsersLoginSuccessResponse]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
