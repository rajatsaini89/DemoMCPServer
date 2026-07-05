from fastmcp import FastMCP

mcp = FastMCP(name = "IT Helpdesk MCP server")

@mcp.tool
def classify_ticket(issue_description: str) -> dict:
    """
      Classify and IT support ticket based on the issue description.
    """

    issue = issue_description.lower()

    if any(word in issue for word in ["vpn", "network", "wifi", "internet"]):
        category = "Network"
        team = "Infrastructure Team"

    elif any(word in issue for word in ["password", "login", "authentication", "account"]):
        category = "Access Management"
        team = "Identity & Access Team"

    elif any(word in issue for word in ["laptop", "screen", "keyboard", "mouse", "hardware"]):
        category = "Hardware"
        team = "Desktop Support"

    elif any(word in issue for word in ["email", "outlook", "mail", "inbox"]):
        category = "Email"
        team = "Messaging Team"

    else:
        category = "General Software"
        team = "App Support"

    return {"category": category, "team": team}


@mcp.tool
def generate_troubleshooting_steps(issue_type: str) -> list[str]:
    """
    Return standard troubleshooting steps for common issues.
    """

    issue = issue_type.lower()

    if issue == "vpn":
        return [
            "Check internet connectivity.",
            "Restart the VPN client.",
            "Verify your credentials.",
            "Reconnect to the VPN.",
            "Contact Infrastructure Team if the issue persists."
        ]

    elif issue == "password":
        return [
            "Verify the username.",
            "Check if Caps Lock is enabled.",
            "Reset the password if needed.",
            "Try logging in again."
        ]

    elif issue == "email":
        return [
            "Check internet connectivity.",
            "Restart Outlook.",
            "Verify mailbox quota.",
            "Check server connection."
        ]

    else:
        return [
            "Restart the application.",
            "Reboot the computer.",
            "Capture the error message.",
            "Contact IT Support if unresolved."
        ]


@mcp.tool
def estimate_resolution_time(priority: str) -> str:
    """
    Estimate the expected resolution time.
    """

    priority = priority.lower()

    mapping = {
        "critical": "Within 2 Hours",
        "high": "Within 8 Hours",
        "medium": "Within 1 Business Day",
        "low": "Within 3 Business Days"
    }

    return mapping.get(priority, "To Be Determined")


if __name__ == "__main__":
   # mcp.run(transport="http", host="0.0.0.0", port=8080)
     mcp.run() #-> for local use