import zmq
import json
from concurrent.futures import ThreadPoolExecutor
from command_handler import CommandHandler
from logger import setup_logger

# Initialize the logger
logger = setup_logger("server.log")


class Server:
    def __init__(self, host="127.0.0.1", port=5555):
        self.address = f"tcp://{host}:{port}"
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REP)  # REP: Server responds to requests
        self.command_handler = CommandHandler()

    def start(self):
        self.socket.bind(self.address)
        logger.info(f"Server started at {self.address}")
        print(f"Server listening on {self.address}")

        with ThreadPoolExecutor() as executor:
            while True:
                try:
                    # Wait for a client request
                    message = self.socket.recv_string()
                    logger.info(f"Received request: {message}")
                    
                    # Parse the request
                    request = json.loads(message)
                    
                    # Handle the request in a thread pool
                    future = executor.submit(self.handle_request, request)
                    response = future.result()

                    # Send the response
                    self.socket.send_string(json.dumps(response))
                    logger.info(f"Sent response: {response}")
                except Exception as e:
                    error_message = {"status": "error", "message": str(e)}
                    logger.error(f"Error: {str(e)}")
                    self.socket.send_string(json.dumps(error_message))

    def handle_request(self, request):
        """
        Handling incoming JSON requests and delegating to the appropriate handler.
        """
        try:
            command_type = request.get("command_type")
            if not command_type:
                raise ValueError("Missing 'command_type' in request.")

            if command_type == "os":
                return self.command_handler.handle_os_command(request)
            elif command_type == "compute":
                return self.command_handler.handle_compute_command(request)
            else:
                raise ValueError(f"Unknown command type: {command_type}")

        except Exception as e:
            return {"status": "error", "message": str(e)}


if __name__ == "__main__":
    server = Server()
    server.start()
