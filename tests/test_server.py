import pytest
from unittest import mock
import socket
from server import *  # Import the server logic

@mock.patch('socket.socket')
def test_receive_and_respond(mock_socket):
    mock_socket_instance = mock_socket.return_value

    # Configure mock behavior
    mock_socket_instance.recv.return_value = b'{"name": "Edward", "message": "Hello!"}'

    # Execute server code (need to adjust)
    run__server_logic()  # Replace this placeholder with how the server starts

    # Assertions
    mock_socket_instance.sendall.assert_called_with(b'{"name": "Edward", "message": "Hello!"}')  # ... and that the same data was echoed back