"""Tests for the main uv_demo module."""

import pytest

# Add the src directory to the Python path if not already added
# sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

from uv_demo import main


def test_main_function_output(capsys) -> None:
    """Test that the main function prints the expected output."""
    main()
    captured = capsys.readouterr()
    assert "Hello from uv-demo!" in captured.out
    assert "Version:" in captured.out
