from unittest.mock import Mock, patch

import pytest

from homework4.task_2_mock_input import URLReader, count_dots_on_i


@patch('homework4.task_2_mock_input.urlopen')
def test_URLReader_get_url(mock_urlopen):
    """Testing read_url method from URLReader class with valid link"""
    fake_url = 'fake_url'
    url_mock = Mock()
    url_mock.read.side_effect = ['_i_<response_i>'.encode('utf-8')]
    correct_response = '_i_<response_i>'.encode('utf-8')
    mock_urlopen.return_value = url_mock
    client = URLReader()

    response = client.read_url(fake_url)

    assert response == correct_response


def test_URLReader_cant_get_url():
    """Testing read_url method from URLReader class with unreachable link"""
    fake_url = 'fake_url'
    client = URLReader()

    with pytest.raises(ValueError):
        _ = client.read_url(fake_url)


def test_URLReader_decode_url():
    """Testing decode_url method from URLReader class"""
    test_input = '_i_<response_i>'.encode('utf-8')
    correct_text = '_i_<response_i>'
    client = URLReader()

    decoded_text = client.decode_url(test_input)

    assert decoded_text == correct_text


def test_i_in_html_case():
    """Testing program when some "i" characters are presented in html"""

    class FakeReader:
        """Fake URLReader class for unit tests"""

        @staticmethod
        def read_url(url: str) -> bytes:
            fake_answer = '_i_<response_i>'.encode('utf-8')
            return fake_answer

        @staticmethod
        def decode_url(url_response: bytes, encoding: str = 'utf-8') -> str:
            return url_response.decode(encoding)

    fake_url = 'fake_url'
    with patch('homework4.task_2_mock_input.URLReader', FakeReader):
        assert count_dots_on_i(fake_url) == 2


def test_html_without_i_case():
    """Testing program when there are not some "i" characters in html"""

    class FakeReader:
        """Fake URLReader class for unit tests"""

        @staticmethod
        def read_url(url: str) -> bytes:
            fake_answer = '__<response_>'.encode('utf-8')
            return fake_answer

        @staticmethod
        def decode_url(url_response: bytes, encoding: str = 'utf-8') -> str:
            return url_response.decode(encoding)

    fake_url = 'fake_url'
    with patch('homework4.task_2_mock_input.URLReader', FakeReader):
        assert count_dots_on_i(fake_url) == 0
