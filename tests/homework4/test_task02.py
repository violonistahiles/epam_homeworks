from unittest.mock import Mock, patch

import pytest

from homework4.task_2_mock_input import count_dots_on_i


def test_network_error_case():
    """Testing program when any network errors presented"""
    fake_url = 'fake_url'

    with pytest.raises(ValueError):
        count_dots_on_i(fake_url)


@patch('homework4.task_2_mock_input.urlopen')
def test_i_in_html_case(mock_urlopen):
    """Testing program when some "i" characters are presented in html"""
    fake_url = 'fake_url'
    url_mock = Mock()
    url_mock.read.side_effect = ['_i_<response_i>'.encode('utf-8')]
    mock_urlopen.return_value = url_mock

    test_result = count_dots_on_i(fake_url)

    assert test_result == 2


@patch('homework4.task_2_mock_input.urlopen')
def test_html_without_i_case(mock_urlopen):
    """Testing when there is no "i" in html"""
    fake_url = 'fake_url'
    url_mock = Mock()
    url_mock.read.side_effect = ['response'.encode('utf-8')]
    mock_urlopen.return_value = url_mock

    assert not count_dots_on_i(fake_url)
