import pytest
from client import Client


@pytest.fixture
def client():
    return Client()


def test_client_send_request_success(client, mocker):
    mock_socket = mocker.patch("zmq.Context.socket")
    mock_socket.return_value.recv_string.return_value = '{"status": "success", "result": 25}'

    request = {"command_type": "compute", "expression": "(2 + 3) * 5"}
    response = client.send_request(request)
    assert response["status"] == "success"
    assert response["result"] == 25


def test_client_send_request_error(client, mocker):
    mock_socket = mocker.patch("zmq.Context.socket")
    mock_socket.return_value.recv_string.return_value = '{"status": "error", "message": "Invalid command"}'

    request = {"command_type": "invalid"}
    response = client.send_request(request)
    assert response["status"] == "error"
    assert response["message"] == "Invalid command"
