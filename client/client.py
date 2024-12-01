import zmq
import json


class Client:
    def __init__(self, host="127.0.0.1", port=1234):
        self.address = f"tcp://{host}:{port}"
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REQ)  # REQ: Client sends requests

    def send_request(self, request):
        """
        Send a JSON request to the server and receive a response.
        """
        try:
            # Serialize the request as JSON and send it
            self.socket.connect(self.address)
            self.socket.send_string(json.dumps(request))

            # Wait for the response from the server
            response = self.socket.recv_string()
            return json.loads(response)
        except Exception as e:
            return {"status": "error", "message": str(e)}
        finally:
            self.socket.disconnect(self.address)

    def display_response(self, response):
        """
        Display the server's response in a readable format.
        """
        if response["status"] == "success":
            if "output" in response:
                print(f"Command Output:\n{response['output']}")
            elif "result" in response:
                print(f"Computation Result: {response['result']}")
        else:
            print(f"Error: {response['message']}")


if __name__ == "__main__":
    client = Client()

    while True:
        print("\nChoose a command type:")
        print("1. OS Command")
        print("2. Compute Command")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == "1":
            command_name = input("Enter OS command name (e.g., ping): ").strip()
            parameters = input("Enter command parameters (space-separated): ").strip().split()
            request = {
                "command_type": "os",
                "command_name": command_name,
                "parameters": parameters
            }

        elif choice == "2":
            expression = input("Enter a math expression (e.g., (2+3)*5): ").strip()
            request = {
                "command_type": "compute",
                "expression": expression
            }

        elif choice == "3":
            print("Exiting client.")
            break

        else:
            print("Invalid choice. Please try again.")
            continue

        print("\nSending request to server...")
        response = client.send_request(request)
        client.display_response(response)
