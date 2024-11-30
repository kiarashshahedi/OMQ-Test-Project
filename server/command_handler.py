import subprocess


class CommandHandler:
    def handle_os_command(self, request):
        """
        Handle OS commands like 'ping' or 'ls'.
        """
        try:
            command_name = request.get("command_name")
            parameters = request.get("parameters", [])

            if not command_name:
                raise ValueError("Missing 'command_name' in OS command request.")

            # Build the command
            command = [command_name] + parameters

            # Execute the command
            result = subprocess.run(command, text=True, capture_output=True, check=True)
            return {"status": "success", "output": result.stdout}
        except subprocess.CalledProcessError as e:
            return {"status": "error", "message": e.stderr.strip()}
        except Exception as e:
            return {"status": "error", "message": str(e)}

    def handle_compute_command(self, request):
        """
        Handle Math commands like arithmetic expressions.
        """
        try:
            expression = request.get("expression")
            if not expression:
                raise ValueError("Missing 'expression' in compute command request.")

            # Evaluate the mathematical expression
            result = eval(expression, {"__builtins__": None}, {})
            return {"status": "success", "result": result}
        except Exception as e:
            return {"status": "error", "message": str(e)}
