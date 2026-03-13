import os
import sys


def test_output_file_exists():
    assert os.path.exists("/app/output.txt"), "output.txt does not exist"


def test_output_content():
    with open("/app/output.txt", "r") as f:
        content = f.read().strip()
    names = content.split("\n")
    expected = ["Alice", "Charlie", "Eve"]
    assert names == expected, f"Expected {expected}, got {names}"


def test_excluded_users():
    with open("/app/output.txt", "r") as f:
        content = f.read().strip()
    assert "Bob" not in content, "Bob (age 14) should not be in output"
    assert "Diana" not in content, "Diana (age 17) should not be in output"


if __name__ == "__main__":
    try:
        test_output_file_exists()
        test_output_content()
        test_excluded_users()
        print("All tests passed")
        sys.exit(0)
    except AssertionError as e:
        print(f"Test failed: {e}")
        sys.exit(1)
