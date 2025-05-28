from mcp.server.fastmcp import FastMCP
from app import getHoliday

# Initialize MCP server
mcp = FastMCP("holiday-checker-mcp")

@mcp.tool()
async def check_holiday(country: str, year: int, month: int, day: int) -> dict:
    """
    Get holiday information for a given country and date.
    """
    result = getHoliday(country, year, month, day)
    return result

if __name__ == "__main__":
    mcp.run(transport="stdio")
