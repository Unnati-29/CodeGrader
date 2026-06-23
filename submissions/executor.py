import io
import sys

def execute_code(code,input_data):
    old_stdin = sys.stdin
    old_stdout = sys.stdout

    sys.stdin = io.StringIO(input_data)
    sys.stdout = io.StringIO()

    try:
        exec(code)

        output = sys.stdout.getvalue().strip()

    except Exception as e:
        output = str(e)

    finally:
        sys.stdin = old_stdin
        sys.stdout = old_stdout

    return output