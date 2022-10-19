from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.error_response import ErrorResponse
from ...models.post_namespaces_delete_images_request import PostNamespacesDeleteImagesRequest
from ...models.post_namespaces_delete_images_response_error import PostNamespacesDeleteImagesResponseError
from ...models.post_namespaces_delete_images_response_success import PostNamespacesDeleteImagesResponseSuccess
from ...types import Response


def _get_kwargs(
    namespace: str,
    *,
    client: Client,
    json_body: PostNamespacesDeleteImagesRequest,
) -> Dict[str, Any]:
    url = "{}/v2/namespaces/{namespace}/delete-images".format(client.base_url, namespace=namespace)

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
) -> Optional[Union[ErrorResponse, PostNamespacesDeleteImagesResponseError, PostNamespacesDeleteImagesResponseSuccess]]:
    if response.status_code == 200:
        response_200 = PostNamespacesDeleteImagesResponseSuccess.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = PostNamespacesDeleteImagesResponseError.from_dict(response.json())

        return response_400
    if response.status_code == 403:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[ErrorResponse, PostNamespacesDeleteImagesResponseError, PostNamespacesDeleteImagesResponseSuccess]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    namespace: str,
    *,
    client: Client,
    json_body: PostNamespacesDeleteImagesRequest,
) -> Response[Union[ErrorResponse, PostNamespacesDeleteImagesResponseError, PostNamespacesDeleteImagesResponseSuccess]]:
    """Delete images

     Deletes one or more images within a namespace. This is currently limited to a single
    repository.

    If you attempt to delete images that are marked as active or are currently tagged, the deletion does
    not happen and it displays the warnings.
    To continue with the deletion, you must ignore these warnings by putting them in the
    `ignore_warnings` property.

    Deleting a currently tagged image deletes the tag from the repository.

    You cannot ignore errors. It is not possible to directly delete children of multi-arch images.

    Args:
        namespace (str):
        json_body (PostNamespacesDeleteImagesRequest): Delete images request.

    Returns:
        Response[Union[ErrorResponse, PostNamespacesDeleteImagesResponseError, PostNamespacesDeleteImagesResponseSuccess]]
    """

    kwargs = _get_kwargs(
        namespace=namespace,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    namespace: str,
    *,
    client: Client,
    json_body: PostNamespacesDeleteImagesRequest,
) -> Optional[Union[ErrorResponse, PostNamespacesDeleteImagesResponseError, PostNamespacesDeleteImagesResponseSuccess]]:
    """Delete images

     Deletes one or more images within a namespace. This is currently limited to a single
    repository.

    If you attempt to delete images that are marked as active or are currently tagged, the deletion does
    not happen and it displays the warnings.
    To continue with the deletion, you must ignore these warnings by putting them in the
    `ignore_warnings` property.

    Deleting a currently tagged image deletes the tag from the repository.

    You cannot ignore errors. It is not possible to directly delete children of multi-arch images.

    Args:
        namespace (str):
        json_body (PostNamespacesDeleteImagesRequest): Delete images request.

    Returns:
        Response[Union[ErrorResponse, PostNamespacesDeleteImagesResponseError, PostNamespacesDeleteImagesResponseSuccess]]
    """

    return sync_detailed(
        namespace=namespace,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    namespace: str,
    *,
    client: Client,
    json_body: PostNamespacesDeleteImagesRequest,
) -> Response[Union[ErrorResponse, PostNamespacesDeleteImagesResponseError, PostNamespacesDeleteImagesResponseSuccess]]:
    """Delete images

     Deletes one or more images within a namespace. This is currently limited to a single
    repository.

    If you attempt to delete images that are marked as active or are currently tagged, the deletion does
    not happen and it displays the warnings.
    To continue with the deletion, you must ignore these warnings by putting them in the
    `ignore_warnings` property.

    Deleting a currently tagged image deletes the tag from the repository.

    You cannot ignore errors. It is not possible to directly delete children of multi-arch images.

    Args:
        namespace (str):
        json_body (PostNamespacesDeleteImagesRequest): Delete images request.

    Returns:
        Response[Union[ErrorResponse, PostNamespacesDeleteImagesResponseError, PostNamespacesDeleteImagesResponseSuccess]]
    """

    kwargs = _get_kwargs(
        namespace=namespace,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    namespace: str,
    *,
    client: Client,
    json_body: PostNamespacesDeleteImagesRequest,
) -> Optional[Union[ErrorResponse, PostNamespacesDeleteImagesResponseError, PostNamespacesDeleteImagesResponseSuccess]]:
    """Delete images

     Deletes one or more images within a namespace. This is currently limited to a single
    repository.

    If you attempt to delete images that are marked as active or are currently tagged, the deletion does
    not happen and it displays the warnings.
    To continue with the deletion, you must ignore these warnings by putting them in the
    `ignore_warnings` property.

    Deleting a currently tagged image deletes the tag from the repository.

    You cannot ignore errors. It is not possible to directly delete children of multi-arch images.

    Args:
        namespace (str):
        json_body (PostNamespacesDeleteImagesRequest): Delete images request.

    Returns:
        Response[Union[ErrorResponse, PostNamespacesDeleteImagesResponseError, PostNamespacesDeleteImagesResponseSuccess]]
    """

    return (
        await asyncio_detailed(
            namespace=namespace,
            client=client,
            json_body=json_body,
        )
    ).parsed
