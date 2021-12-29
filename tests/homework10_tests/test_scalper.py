import os
from unittest.mock import patch

import pytest

from homework10.scalper import Scalper


class FakeClient:
    def __init__(self, text):
        self.text = text

    async def get_page(self, *args, **kwargs):
        await self
        return self.text

    def __await__(self):
        return (yield)


@pytest.fixture
def usd_data():
    current_path = os.path.abspath(os.getcwd())
    current_path = os.path.join(current_path, 'tests', 'homework10_tests')
    with open(os.path.join(current_path, 'usd_parse.txt'), 'r') as fi:
        data = fi.read()
    return data


@pytest.mark.asyncio
@patch('homework10.scalper.URLReader')
async def test_scalp_usd_course(mock_reader, usd_data):
    """Testing scalp_usd_course collect usd course correctly"""
    fake_client = FakeClient(usd_data)
    fake_info = {'BANK_LINK': '{}'}
    scalper = Scalper(fake_info)
    scalper.client = fake_client
    correct_result = 30.9436

    result = await scalper.scalp_usd_course()

    assert result == correct_result


@pytest.mark.asyncio
@patch('homework10.scalper.URLReader')
@patch('homework10.scalper.TableParser')
async def test_scalp_first_page(mock_reader, mock_table):
    """Testing scalp_first_page calls methods correctly"""
    mock_table.parse_pages_number.return_value = ['1', '2']
    mock_table.parse_companies.return_value = ['link1', 'link2']

    fake_client = FakeClient('fake_data')
    fake_info = {'FIRST_PAGE_LINK': 'page',
                 'SITE_LINK': 'site'}
    scalper = Scalper(fake_info)
    scalper.client = fake_client
    scalper._table_parser = mock_table
    correct_pages_links = ['page1', 'page2']
    correct_companies_links = ['link1', 'link2']

    _ = await scalper._scalp_first_page()

    assert scalper._pages_links == correct_pages_links
    assert scalper._companies_links == correct_companies_links


@pytest.mark.asyncio
@patch('homework10.scalper.URLReader')
@patch('homework10.scalper.TableParser')
async def test_scalp_table(mock_reader, mock_table):
    """Testing scalp_table calls methods correctly"""
    mock_table.parse_companies.return_value = ['link1', 'link2']

    fake_link = 'fake_link'
    fake_client = FakeClient('fake_data')
    fake_info = {'SITE_LINK': 'site'}
    scalper = Scalper(fake_info)
    scalper.client = fake_client
    scalper._table_parser = mock_table
    correct_companies_links = ['link1', 'link2']

    _ = await scalper._scalp_table(fake_link)

    assert scalper._companies_links == correct_companies_links


@pytest.mark.asyncio
@patch('homework10.scalper.URLReader')
@patch('homework10.scalper.CompanyParser')
async def test_scalp_company_page(mock_reader, mock_company):
    """Testing scalp_company_page calls methods correctly"""
    mock_company.parse_company.return_value = {'code': 'test_code'}

    fake_link = 'fake_link'
    fake_client = FakeClient('fake_data')
    fake_info = {'DATA_LINK': 'link'}
    scalper = Scalper(fake_info)
    scalper.client = fake_client
    scalper._company_parser = mock_company
    correct_companies = {'test_code': {'code': 'test_code'}}

    _ = await scalper._scalp_company_page(fake_link)

    assert scalper._companies == correct_companies


@pytest.mark.asyncio
@patch('homework10.scalper.URLReader')
@patch('homework10.scalper.CompanyParser')
async def test_scalp_company_growth_with_link(mock_reader, mock_company):
    """Testing scalp_company_growth works correctly when link is not None"""
    mock_company.parse_company_year_growth.return_value = 5.3

    start_dict = {'test_code': {'code': 'test_code', 'link': 'test_link'}}
    test_data = {'code': 'test_code', 'link': 'test_link'}
    fake_client = FakeClient('fake_data')
    fake_info = {'fake_key': 'fake_value'}
    scalper = Scalper(fake_info)
    scalper.client = fake_client
    scalper._company_parser = mock_company
    scalper._companies = start_dict
    correct_companies = {'test_code': {'code': 'test_code', 'growth': 5.3}}

    _ = await scalper._scalp_company_growth(test_data)

    assert scalper._companies == correct_companies


@pytest.mark.asyncio
@patch('homework10.scalper.URLReader')
@patch('homework10.scalper.CompanyParser')
async def test_scalp_company_growth_without_link(mock_reader, mock_company):
    """Testing scalp_company_growth works correctly when link is None"""

    start_dict = {'test_code': {'code': 'test_code', 'link': None}}
    test_data = {'code': 'test_code', 'link': None}
    fake_client = FakeClient('fake_data')
    fake_info = {'fake_key': 'fake_value'}
    scalper = Scalper(fake_info)
    scalper.client = fake_client
    scalper._company_parser = mock_company
    scalper._companies = start_dict
    correct_companies = {'test_code': {'code': 'test_code', 'growth': None}}

    _ = await scalper._scalp_company_growth(test_data)

    assert scalper._companies == correct_companies
