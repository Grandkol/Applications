from http import HTTPStatus

import pytest
import requests

@pytest.mark.parametrize(
    "query_data, expected_answer",
    [
        (
            {"user_name": "Тимофей", "description": "Я хочу купить рюкзак"},
            {"status": HTTPStatus.CREATED, "length": 4},
        ),
        (
            {"user_family_name": "Jordan", "s": ""},
            {"status": HTTPStatus.EXPECTATION_FAILED, "length": 1},
        ),
    ],
)
@pytest.mark.asyncio
async def test_post_applications(query_data, expected_answer):
    url = "http://application:8000/app/v1/applications"
    response = requests.post(url, json=query_data)
    assert response.status_code == expected_answer["status"]
    assert len(response.json()) == expected_answer["length"]


@pytest.mark.parametrize(
    "query_data, expected_answer",
    [
        (
            {"user_name": "Тимофей"},
            {"status": HTTPStatus.OK},
        ),
        (
            {"user_name": "Jordan"},
            {"status": HTTPStatus.OK},
        ),
        (
            {"user_name": ""},
            {"status": HTTPStatus.OK},
        ),
    ],
)
@pytest.mark.asyncio
async def test_get_applications(query_data, expected_answer):
    url = "http://application:8000/app/v1/applications"
    response = requests.get(url, json=query_data)
    assert response.status_code == expected_answer["status"]




