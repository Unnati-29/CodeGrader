from .executor import execute_code

def evaluator_submission(code,assignment):
    test_cases = assignment.test_cases.all()
    passed = 0
    total = test_cases.count()
    feedback = "" 

    for index, testcase in enumerate(test_cases, start=1):
        actual_output = execute_code(
            code,
            testcase.input_data
        )

        expected_output = testcase.expected_output.strip()

        if actual_output == expected_output:
            passed += 1

            feedback += (
                f"✅ Test Case {index}: Passed\n"
                f"Expected: {expected_output}\n"
                f"Output: {actual_output}\n\n"
            )

        else:
            feedback += (
                f"❌ Test Case {index}: Failed\n"
                f"Expected: {expected_output}\n"
                f"Output: {actual_output}\n\n"
            )

    score = (passed / total) * 100

    return score,feedback