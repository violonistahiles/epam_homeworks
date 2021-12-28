# from unittest.mock import Mock, patch, AsyncMock
#
# import pytest
#
# from homework10.connection import URLReader
#
#
# # class FakeResponse:
# #     def __init__(self, status, text):
# #         self.status = status
# #         self.text_response = text
# #
# #     def text(self, encoding):
# #         return self.text_response
#
#     # async def __aenter__(self):
#     #     self._conn = connect('wss://ws.binaryws.com/websockets/v3')
#     #     self.websocket = await self._conn.__aenter__()
#     #     return self
#     #
#     # async def __aexit__(self, *args, **kwargs):
#     #     await self._conn.__aexit__(*args, **kwargs)
#
#
# class FakeSession:
#     def __init__(self,  status, text, iter_resp):
#         self.resp = iter_resp
#         self.status = status
#         self.text_response = text
#
#     def get(self, url):
#         return self.__aenter__()
#
#     def __aenter__(self):
#         return self
#
#     def __aexit__(self, *args):
#         pass
#
#     def __await__(self):
#         return self.resp
#
#     # def __iter__(self):
#     #     return self.resp
#     #
#     # def __next__(self):
#     #     return iter(self.resp)
#     #
#     # def __aiter__(self):
#     #     return self
#
#     # def text(self, encoding):
#     #     return self.text_response
#     #
#     # async def __anext__(self):
#     #     data = await self.fetch_data()
#     #     if data:
#     #         return data
#     #     else:
#     #         raise StopAsyncIteration
#     #
#     # async def fetch_data(self):
#     #     return self
#
#
# # @pytest.mark.asyncio
# # @patch('aiohttp.ClientSession')
# # async def test_that_mock_can_be_awaited(mock_session):
# #     fake_url = 'fake_url'
# #     mock2 = AsyncMock()
# #     mock2.status.return_value = 200
# #     mock2.text.return_value = 'fake_text'
# #     mock3 = AsyncMock()
# #     mock3.__aenter__.return_value = mock2
# #
# #     mock1 = AsyncMock()
# #     mock1.get = mock3
# #
# #     mock_session.return_value = mock1
# #     correct_response = 'fake_text'
# #
# #     client = URLReader()
# #
# #     response = await client.get_page(fake_url)
# #
# #     assert response == correct_response
#
#
# @pytest.mark.asyncio
# @patch('aiohttp.ClientSession')
# async def test_lala(mock_session):
#
#     fake_url = 'fake_url'
#     mock2 = AsyncMock()
#     mock2.status.return_value = 200
#     mock2.text.return_value = 'fake_text'
#     resp = mock2
#     session = FakeSession(200, 'fake_text', resp)
#     # mock_session = session
#     # url_mock.read.side_effect = ['_i_<response_i>'.encode('utf-8')]
#     # correct_response = '_i_<response_i>'.encode('utf-8')
#     mock_session.return_value = session
#     correct_response = 'fake_text'
#
#     client = URLReader()
#
#     response = await client.get_page(fake_url)
#
#     assert response == correct_response
