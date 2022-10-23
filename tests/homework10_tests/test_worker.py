from unittest.mock import patch

import pytest

from homework10.worker import Worker


class FakeScalper:
    def __init__(self, companies, course):
        self.companies = companies
        self.course = course

    async def scalp_usd_course(self, *args, **kwargs):
        await self
        return self.course

    async def scalp(self, *args, **kwargs):
        await self
        return self.companies

    async def close_session(self, *args, **kwargs):
        await self

    def __await__(self):
        return (yield)


@patch('homework10.worker.Scalper')
def test_sort_elements_without_coef(mock_scalper):
    """
    Testing sort_elements works correctly when it is invoking
    without coef parameter
    """
    test_companies_list = [{'code': 'code1', 'name': 'name1', 'data': 2},
                           {'code': 'code2', 'name': 'name2', 'data': 1},
                           {'code': 'code3', 'name': 'name3', 'data': 4}]
    worker = Worker(2)
    correct_result = [{'code': 'code2', 'name': 'name2', 'data': 1},
                      {'code': 'code1', 'name': 'name1', 'data': 2}]

    result = worker._sort_elements(test_companies_list, 'data')

    assert result == correct_result


@patch('homework10.worker.Scalper')
def test_sort_elements_with_coef_and_reversed(mock_scalper):
    """
    Testing sort_elements works correctly when it is invoking
    without coef parameter
    """
    test_companies_list = [{'code': 'code1', 'name': 'name1', 'data': 2},
                           {'code': 'code2', 'name': 'name2', 'data': 1},
                           {'code': 'code3', 'name': 'name3', 'data': 4}]
    worker = Worker(2)
    correct_result = [{'code': 'code3', 'name': 'name3', 'data': 8},
                      {'code': 'code1', 'name': 'name1', 'data': 4}]

    result = worker._sort_elements(test_companies_list, 'data', 2, True)

    assert result == correct_result


@pytest.mark.asyncio
@patch('homework10.worker.Scalper')
async def test_get_companies_info(mock_scalper):
    """Testing get_companies_info method works correctly"""

    test_companies_list = [{'code': 'code1', 'name': 'name1', 'data': 2},
                           {'code': 'code2', 'name': 'name2', 'data': 1},
                           {'code': 'code3', 'name': 'name3', 'data': 4}]
    test_usd_course = 42.24
    fake_scalper = FakeScalper(test_companies_list, test_usd_course)
    worker = Worker(2)
    worker._scalper = fake_scalper

    usd_course, companies_info = await worker._get_info()

    assert usd_course == test_usd_course
    assert companies_info == test_companies_list
