"""
============================================================
Network Scanner & Port Checker
Author: Yonathan Toledano

Extended Description:
This script is a basic network diagnostic and scanning tool
designed for IT and network administrators.

It performs the following tasks:
1. Checks host availability using ICMP (ping)
2. Scans common TCP ports on reachable hosts
3. Displays a clean and readable scan report

The script is READ-ONLY and does NOT modify any system or
network configuration. It is safe to run in production
environments for diagnostic purposes.

------------------------------------------------------------
How to Run:
1. Make sure Python 3.7 or later is installed
2. Open a terminal / command prompt
3. Navigate to the script directory:
   cd path/to/script
4. Run the script:
   python network_scanner.py

------------------------------------------------------------
Tested On:
- Windows 10 / 11
- Windows Server
- Linux (basic compatibility)
------------------------------------------------------------
"""

# ================================
# IMPORTS
# ================================

# Used to execute system commands (ping)
import subprocess

# Used to create TCP connections (port scanning)
import socket

# Used to detect the operating system (Windows/Linux)
import platform

# Used to generate timestamps for reports
from datetime import datetime


# ================================
# CONFIGURATION SECTION
# ================================
# ⚠️ THIS IS THE MAIN SECTION YOU SHOULD EDIT ⚠️

# List of hosts to scan
# You can add:
# - IP addresses
# - DNS names
# - Servers, routers, firewalls, etc.
hosts = [
    "8.8.8.8",         # Google Public DNS
    "1.1.1.1",         # Cloudflare Public DNS
    "192.168.1.1"      # Example local gateway
]

# List of TCP ports to scan
# Common IT / network ports:
# 22   = SSH
# 80   = HTTP
# 443  = HTTPS
# 3389 = RDP
ports = [22, 80, 443, 3389]

# Timeout (in seconds) for each port connection attempt
# Increase if scanning slow or remote networks
timeout = 1


# ================================
# FUNCTION: PING HOST
# ================================
def ping_host(host):
    """
    Purpose:
    Checks if a host is reachable using ICMP (ping).

    How it works:
    - Uses the system 'ping' command
    - Adjusts parameters for Windows or Linux automatically

    Returns:
    True  -> Host is reachable
    False -> Host is unreachable
    """

    # Windows uses '-n', Linux/macOS use '-c'
    param = "-n" if platform.system().lower() == "windows" else "-c"

    # Build the ping command
    command = ["ping", param, "1", host]

    try:
        # Run the ping command silently
        result = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        # Return True if ping succeeded
        return result.returncode == 0

    except Exception as e:
        print(f"Error pinging {host}: {e}")
        return False


# ================================
# FUNCTION: PORT SCANNER
# ================================
def scan_ports(host):
    """
    Purpose:
    Scans a list of TCP ports on a given host.

    How it works:
    - Creates a TCP socket
    - Attempts to connect to each port
    - If connection succeeds -> port is open

    Returns:
    List of open ports
    """

    open_ports = []

    for port in ports:
        try:
            # Create a TCP socket
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

                # Set timeout to avoid hanging
                sock.settimeout(timeout)

                # connect_ex returns 0 if successful
                if sock.connect_ex((host, port)) == 0:
                    open_ports.append(port)

        except Exception as e:
            print(f"Error scanning {host}:{port} -> {e}")

    return open_ports


# ================================
# FUNCTION: REPORT GENERATOR
# ================================
def generate_report(results):
    """
    Purpose:
    Prints a formatted summary of scan results.

    Input:
    Dictionary containing scan data for each host
    """

    print("\n" + "=" * 60)
    print("NETWORK SCAN REPORT")
    print(f"Generated: {datetime.now()}")
    print("=" * 60)

    for host, data in results.items():
        status = "Reachable" if data["reachable"] else "Unreachable"
        ports = (
            ", ".join(str(p) for p in data["open_ports"])
            if data["open_ports"]
            else "None"
        )

        print(f"{host:15} | Status: {status:12} | Open Ports: {ports}")

    print("=" * 60 + "\n")


# ================================
# MAIN EXECUTION
# ================================
# This block ensures the script runs only when executed directly
# and not when imported as a module

if __name__ == "__main__":

    print("\nStarting Network Scan...\n")

    # Dictionary to store scan results
    scan_results = {}

    # Loop through each host
    for host in hosts:

        # Step 1: Ping the host
        reachable = ping_host(host)

        # Step 2: Scan ports only if host is reachable
        open_ports = scan_ports(host) if reachable else []

        # Store results
        scan_results[host] = {
            "reachable": reachable,
            "open_ports": open_ports
        }

        # Print real-time status
        status = "OK" if reachable else "FAILED"
        print(f"[{status}] {host}")

    # Generate final report
    generate_report(scan_results)
