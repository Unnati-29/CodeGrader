# submissions/executor.py

import subprocess
import sys

TIMEOUT_SECONDS = 5


def execute_code(code, input_data):
    try:
        result = subprocess.run(
            [sys.executable, "-c", code],   
            input=input_data,
            capture_output=True,
            text=True,
            timeout=TIMEOUT_SECONDS,
        )

        if result.returncode != 0:
            return f"Error: {result.stderr.strip()}"

        return result.stdout.strip()

    except subprocess.TimeoutExpired:
        return "Error: Code took too long to execute (possible infinite loop)"

    except Exception as e:
        return f"Error: {str(e)}"