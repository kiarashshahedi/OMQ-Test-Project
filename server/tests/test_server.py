import pytest
from server.command_handler import CommandHandler


@pytest.fixture
def command_handler():
    return CommandHandler()


def test_os_command_success(command_handler):
    request = {
        "command_type": "os",
        "command_name": "echo",
        "parameters": ["Hello, World!"]
    }
    response = command_handler.handle_os_command(request)
    assert response["status"] == "success"
    assert "Hello, World!" in response["output"]


def test_os_command_failure(command_handler):
    request = {
        "command_type": "os",
        "command_name": "invalid_command"
    }
    response = command_handler.handle_os_command(request)
    assert response["status"] == "error"


def test_compute_command_success(command_handler):
    request = {
        "command_type": "compute",
        "expression": "(2 + 3) * 5"
    }
    response = command_handler.handle_compute_command(request)
    assert response["status"] == "success"
    assert response["result"] == 25


def test_compute_command_invalid_expression(command_handler):
    request = {
        "command_type": "compute",
        "expression": "2 / 0"
    }
    response = command_handler.handle_compute_command(request)
    assert response["status"] == "error"
