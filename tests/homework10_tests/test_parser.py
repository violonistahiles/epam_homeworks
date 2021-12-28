from unittest.mock import patch

from homework10.parser import (CompanyParser, ElementNotFoundError,
                               TableParser, parsing_decorator)


class FakeSoup:
    def __init__(self, fake_data):
        self.fake_data = fake_data

    def find_all(self, *args, **kwargs):
        return self.fake_data

    def find(self, *args, **kwargs):
        return self


class FakeElement:
    def __init__(self, fake_data):
        self.fake_data = fake_data

    def get(self, *args):
        return self.fake_data


class FakeTime:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __sub__(self, other):
        return self


def test_parsing_decorator():
    """
    Testing function decorated by parsing_decorator return None if
    ElementNotFoundError is raised
    """
    def some_func():
        raise ElementNotFoundError

    correct_result = None
    func_to_test = parsing_decorator(some_func)

    result = func_to_test()

    assert result == correct_result


@patch('homework10.parser.BeautifulSoup')
def test_parse_pages_number(mock_bs4):
    """Testing parse_pages_number from TableParser works as expected"""
    fake_page = 'fake_page'
    fake_data = [FakeElement('1'), FakeElement('2'), FakeElement('3')]
    fake_soup = FakeSoup(fake_data)
    mock_bs4.return_value = fake_soup
    table_parser = TableParser()
    correct_result = ['?p=2', '?p=3']

    result = table_parser.parse_pages_number(fake_page)

    assert result == correct_result


@patch('homework10.parser.BeautifulSoup')
def test_parse_companies(mock_bs4):
    """Testing parse_companies from TableParser works as expected"""
    fake_page = 'fake_page'
    fake_site = 'fake_site'
    fake_data = [FakeElement('1'), FakeElement('2'), FakeElement('3')]
    fake_soup = FakeSoup(fake_data)
    mock_bs4.return_value = fake_soup
    table_parser = TableParser()
    correct_result = ['fake_site1', 'fake_site2', 'fake_site3']

    result = table_parser.parse_companies(fake_page, fake_site)

    assert result == correct_result


@patch('homework10.parser.datetime')
def test_set_up_data_link(mock_time):
    """Testing set_up_data_link from CompanyParser works as expected"""
    fake_link = '{}{}{}'
    fake_data = 'fake_data'
    mock_time.datetime.today.return_value = FakeTime(5, 4, 3)
    mock_time.timedelta.return_value = 0
    company_parser = CompanyParser()
    correct_result = 'fake_data543543'

    result = company_parser._set_up_data_link(fake_link, fake_data)

    assert result == correct_result


def test_parse_company_db_address():
    """Testing parse_company_db_address from TableParser works as expected"""
    fake_content = '"TKData" : "155"'
    fake_soup = FakeSoup('fake_data')
    fake_soup.contents = [fake_content]
    company_parser = CompanyParser()
    company_parser._soup = fake_soup
    correct_result = '155'

    result = company_parser._parse_company_db_address()

    assert result == correct_result


def test_parse_current_value():
    """Testing parse_current_value from TableParser works as expected"""
    fake_content = '1,555.36'
    fake_soup = FakeSoup('fake_data')
    fake_soup.contents = [fake_content]
    company_parser = CompanyParser()
    company_parser._soup = fake_soup
    correct_result = 1555.36

    result = company_parser._parse_current_value()

    assert result == correct_result


def test_parse_company_code():
    """Testing parse_company_code from TableParser works as expected"""
    fake_content = 'fake code'
    fake_soup = FakeSoup('fake_data')
    fake_soup.contents = [fake_content]
    company_parser = CompanyParser()
    company_parser._soup = fake_soup
    correct_result = 'code'

    result = company_parser._parse_company_code()

    assert result == correct_result


def test_parse_company_year_growth():
    """Testing parse_company_year_growth from TableParser works as expected"""
    test_string = '[{"Close":5,}, {"Close":125.25,}, {"Close":10,}]'
    company_parser = CompanyParser()
    correct_result = 100

    result = company_parser.parse_company_year_growth(test_string)

    assert result == correct_result


@patch('homework10.parser.BeautifulSoup')
def test_parse_company(mock_bs4):
    """Testing parse_company from TableParser works as expected"""
    def fake_func(*args):
        return [*args] if args else 1

    fake_page = 'fake_page'
    fake_link = 'fake_link'
    company_parser = CompanyParser()
    company_parser._parse_name = fake_func
    company_parser._parse_current_value = fake_func
    company_parser._parse_company_code = fake_func
    company_parser._parse_company_pe = fake_func
    company_parser._parse_company_profit = fake_func
    company_parser._get_link_to_statistics = fake_func
    correct_result = {'name': 1,
                      'code': 1,
                      'price': 1,
                      'P/E': 1,
                      'link': ['fake_link'],
                      'profit': 1}

    result = company_parser.parse_company(fake_page, fake_link)

    assert result == correct_result
