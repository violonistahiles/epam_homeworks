from unittest.mock import patch

import pytest

from homework10.connection import URLReader


class FakeSession:
    """Class for imitating aiohttp.ClientSession"""
    def __init__(self,  status, text):
        self.status = status
        self.text_response = text

    def get(self, url):
        return self

    async def __aenter__(self):
        await self
        return self

    async def __aexit__(self, *args):
        await self
        return self

    def __await__(self):
        return (yield)

    async def text(self, *args, **kwargs):
        await self
        return self.text_response


@pytest.mark.asyncio
@patch('homework10.connection.aiohttp.ClientSession')
async def test_get_page_with_status_200(mock_session):
    """Testing when get response code is 200 function returns HTML"""
    fake_url = 'fake_url'
    session = FakeSession(200, 'fake_text')
    mock_session.return_value = session
    correct_response = 'fake_text'

    client = URLReader()

    response = await client.get_page(fake_url)

    assert response == correct_response


@pytest.mark.asyncio
@patch('homework10.connection.aiohttp.ClientSession')
async def test_get_page_with_status_not_200(mock_session):
    """Testing when get response code is 200 function returns HTML"""
    fake_url = 'fake_url'
    session = FakeSession(400, 'fake_text')
    mock_session.return_value = session

    client = URLReader()

    with pytest.raises(ValueError):
        _ = await client.get_page(fake_url)
