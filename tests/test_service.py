import pytest
import source.service as service
import requests
import unittest.mock as mock

# MOCKING
@mock.patch('source.service.get_user_by_id')
def test_get_user_by_id(mock_user):
    mock_user.return_value = 'Mocked Alice'
    user_name = service.get_user_by_id(2)

    assert user_name == 'Mocked Alice'

@mock.patch('requests.get')
def test_get_users(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {'id':1, 'name':'John Doe'}
    mock_get.return_value = mock_response
    data = service.get_users()

    assert data == {'id':1, 'name':'John Doe'}


@mock.patch('requests.get')
def test_get_users_error(mock_err):
    mock_resp = mock.Mock()
    mock_resp.status_code = 400
    mock_err.return_value = mock_resp
    with pytest.raises(requests.HTTPError):
        service.get_users()

