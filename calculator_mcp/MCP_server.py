import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from fastmcp import FastMCP
from typing import Annotated
from pydantic import Field
from config.custom_logging_config import RequestLoggingMiddleware
from config.logging_config import configure_logging

configure_logging()

mcp = FastMCP("Calculator Server")
mcp.add_middleware(RequestLoggingMiddleware())


@mcp.tool()
def add_numbers(
    a: Annotated[float, Field(description="First number to add")],
    b: Annotated[float, Field(description="Second number to add")],
) -> float:
    """Adds two numbers together and returns the result."""
    return a + b


@mcp.tool()
def divide_numbers(
    a: Annotated[float, Field(description="Numerator (number to be divided)")],
    b: Annotated[float, Field(description="Denominator (number to divide by)")],
) -> float:
    """Divides two numbers together and returns the result."""
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

@mcp.tool()
def multiply_numbers(
    a: Annotated[float, Field(description="First number")],
    b: Annotated[float, Field(description="Second number")],
) -> float:
    """Multiplies two numbers."""
    return a * b


@mcp.tool()
def subtract_numbers(
    a: Annotated[float, Field(description="First number")],
    b: Annotated[float, Field(description="Second number")],
) -> float:
    """Subtracts second number from first."""
    return a - b


@mcp.tool()
def power(
    base: Annotated[float, Field(description="Base number")],
    exponent: Annotated[float, Field(description="Exponent")],
) -> float:
    """Raises a number to a power."""
    return base ** exponent


if __name__ == "__main__":
    print("Startar MCP-servern via SSE på http://127.0.0.1:8001/sse ...")
    
    # Kör servern specifikt i "sse"-läge så agenten kan prata med den
    mcp.run(transport="sse", host="127.0.0.1", port=8001)