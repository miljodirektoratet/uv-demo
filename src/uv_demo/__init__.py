"""
uv-demo.

A Python project built with UV.
"""

from importlib.metadata import version

__version__ = version("uv-demo")


def main() -> None:
    """
    Main entry point for uv-demo.

    Display a welcome message and version information.
    """
    print("Hello from uv-demo!")
    print(f"Version: {__version__}")


if __name__ == "__main__":
    main()
