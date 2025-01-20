import os
import platform
import subprocess
import psutil
from datetime import datetime
import time
import sys


# Function to detect OS
def detect_os():
    os_info = platform.system()
    return os_info

# Function to collect logs (XAMPP/WAMP Apache, MySQL, etc.)
def collect_logs():
    logs = []
    
    # Windows paths for XAMPP and WAMP
    if platform.system() == "Windows":
        os.system("cls")
        print("\033[33m")
        print("""
        ███████╗███████╗██████╗ ██╗   ██╗███████╗██████╗     ███████╗ ██████╗ ██████╗ ███████╗███╗   ██╗███████╗██╗ ██████╗
        ██╔════╝██╔════╝██╔══██╗██║   ██║██╔════╝██╔══██╗    ██╔════╝██╔═══██╗██╔══██╗██╔════╝████╗  ██║██╔════╝██║██╔════╝
        ███████╗█████╗  ██████╔╝██║   ██║█████╗  ██████╔╝    █████╗  ██║   ██║██████╔╝█████╗  ██╔██╗ ██║███████╗██║██║     
        ╚════██║██╔══╝  ██╔══██╗╚██╗ ██╔╝██╔══╝  ██╔══██╗    ██╔══╝  ██║   ██║██╔══██╗██╔══╝  ██║╚██╗██║╚════██║██║██║     
        ███████║███████╗██║  ██║ ╚████╔╝ ███████╗██║  ██║    ██║     ╚██████╔╝██║  ██║███████╗██║ ╚████║███████║██║╚██████╗
        ╚══════╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝    ╚═╝      ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝ ╚═════╝
              For Window Operating System Plateform Developed by Muhammad Sudais Usmani , Happy Forensic :)
        """)
        print("\033[0m") 
        xampp_paths = {
            "access_log": r"C:\xampp\apache\logs\access.log",
            "error_log": r"C:\xampp\apache\logs\error.log",
            "httpd_pid": r"C:\xampp\apache\logs\httpd.pid",
            "install_log": r"C:\xampp\apache\logs\install.log",
            "ssl_log": r"C:\xampp\apache\logs\ssl_request.log"
        }

        # Collect logs from XAMPP
        for log_name, log_path in xampp_paths.items():
            if os.path.exists(log_path):
                logs.append({
                    "log_name": log_name,
                    "log_path": log_path,
                    "content": read_log_content(log_path)
                })
    
    else:
        os.system("clear")
        print("\033[33m")
        print("""
        ███████╗███████╗██████╗ ██╗   ██╗███████╗██████╗     ███████╗ ██████╗ ██████╗ ███████╗███╗   ██╗███████╗██╗ ██████╗
        ██╔════╝██╔════╝██╔══██╗██║   ██║██╔════╝██╔══██╗    ██╔════╝██╔═══██╗██╔══██╗██╔════╝████╗  ██║██╔════╝██║██╔════╝
        ███████╗█████╗  ██████╔╝██║   ██║█████╗  ██████╔╝    █████╗  ██║   ██║██████╔╝█████╗  ██╔██╗ ██║███████╗██║██║     
        ╚════██║██╔══╝  ██╔══██╗╚██╗ ██╔╝██╔══╝  ██╔══██╗    ██╔══╝  ██║   ██║██╔══██╗██╔══╝  ██║╚██╗██║╚════██║██║██║     
        ███████║███████╗██║  ██║ ╚████╔╝ ███████╗██║  ██║    ██║     ╚██████╔╝██║  ██║███████╗██║ ╚████║███████║██║╚██████╗
        ╚══════╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝    ╚═╝      ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝ ╚═════╝
              For Linux Operating System Plateform Developed by Muhammad Sudais Usmani , Happy Forensic :)
        """)
        # Linux log paths for Apache
        apache_log_paths = {
            "access_log": "/var/log/apache2/access.log",
            "error_log": "/var/log/apache2/error.log",
            "httpd_pid": "/var/run/apache2/httpd.pid",
            "install_log": "/var/log/apache2/install.log",  # Custom log if needed
            "ssl_log": "/var/log/apache2/ssl_request.log"
        }

        # Collect Apache logs from Linux
        for log_name, log_path in apache_log_paths.items():
            if os.path.exists(log_path):
                logs.append({
                    "log_name": log_name,
                    "log_path": log_path,
                    "content": read_log_content(log_path)
                })
    
    return logs

# Function to read log content
def read_log_content(log_path):
    try:
        with open(log_path, "r") as f:
            content = f.readlines()  # Read the entire log content
        return content
    except Exception as e:
        return [f"Error reading file: {e}"]

# Function to fetch system information
def get_system_info():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    network = psutil.net_if_addrs()
    
    return {
        "CPU Usage (%)": cpu,
        "Memory Usage (%)": memory.percent,
        "Disk Usage (%)": disk.percent,
        "Network Interfaces": network
    }

# Function to fetch Windows user list
def get_windows_user_list():
    try:
        result = subprocess.check_output("net user", shell=True, universal_newlines=True)
        return result
    except Exception as e:
        return f"Error fetching user list: {e}"

# Function to fetch Active network connections
def get_active_network_connections():
    connections = psutil.net_connections(kind='inet')
    active_connections = []
    for conn in connections:
        active_connections.append({
            "local_address": conn.laddr,
            "remote_address": conn.raddr,
            "status": conn.status
        })
    return active_connections

# Function to fetch disk usage
def get_disk_usage():
    partitions = psutil.disk_partitions()
    disk_info = []
    for partition in partitions:
        usage = psutil.disk_usage(partition.mountpoint)
        disk_info.append({
            "caption": partition.device,
            "description": partition.fstype,
            "filesystem": usage.percent
        })
    return disk_info

# Function to generate HTML report with forensic information
def generate_html_report(logs, system_info, user_list, active_connections, disk_usage):
    html_content = f"""
    <html>
        <head>
            <title>Server Forensic Report</title>
            <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet">
            <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
            <script src="https://cdn.jsdelivr.net/npm/datatables@1.11.5/js/jquery.dataTables.min.js"></script>
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/datatables@1.11.5/css/jquery.dataTables.min.css">
            <style>
                pre {{
                    white-space: pre-wrap;
                    word-wrap: break-word;
                }}
                table {{
                    width: 100%;
                    border-collapse: collapse;
                }}
                th, td {{
                    border: 1px solid #ddd;
                    padding: 8px;
                }}
                th {{
                    background-color: #f2f2f2;
                }}
                .navbar {{
                    margin-bottom: 20px;
                }}
                .log-content {{
                    font-family: monospace;
                    white-space: pre-wrap;
                    word-wrap: break-word;
                }}
                .access_log {{
                    background-color: #d9f7d9;
                }}
                .error_log {{
                    background-color: #f7d9d9;
                }}
                .httpd_pid {{
                    background-color: #d9d9f7;
                }}
                .install_log {{
                    background-color: #f9f7d9;
                }}
                .ssl_log {{
                    background-color: #d9f7f9;
                }}
                .dataTables_filter {{
                    float: right;
                    margin-bottom: 20px;
                }}
                .table-responsive {{
                    overflow-x: auto;
                }}
            </style>
        </head>
        <body>
            <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
                <a class="navbar-brand" href="#">Forensic Report</a>
                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarNav">
                    <ul class="navbar-nav ml-auto">
                        <li class="nav-item">
                            <a class="nav-link" href="https://github.com/Dit-Developers/" target="_blank">GitHub</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="https://www.linkedin.com/in/muhammad-sudais-usmani-950889311/" target="_blank">LinkedIn</a>
                        </li>
                    </ul>
                </div>
            </nav>
            <div class="container">
                <h1 class="text-center my-4">Server Forensic Report</h1>
                <p><strong>Report generated at:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
                <p><strong>Operating System:</strong> {platform.system()}</p>
                
                <h3>System Information:</h3>
                <table class="table table-striped">
                    <thead>
                        <tr>
                            <th>Metric</th>
                            <th>Value</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr><td>CPU Usage</td><td>{system_info["CPU Usage (%)"]}%</td></tr>
                        <tr><td>Memory Usage</td><td>{system_info["Memory Usage (%)"]}%</td></tr>
                        <tr><td>Disk Usage</td><td>{system_info["Disk Usage (%)"]}%</td></tr>
                        <tr><td>Network Interfaces</td><td>{', '.join(system_info["Network Interfaces"].keys())}</td></tr>
                    </tbody>
                </table>

                <h3>Log Paths:</h3>
                <table class="table table-striped">
                    <thead>
                        <tr>
                            <th>Log Type</th>
                            <th>Log Path</th>
                        </tr>
                    </thead>
                    <tbody>
    """
    
    # Display the logs paths
    for log in logs:
        html_content += f"""
            <tr class="{log['log_name']}">
                <td>{log['log_name']}</td>
                <td>{log['log_path']}</td>
            </tr>
        """
    
    html_content += """
                    </tbody>
                </table>

                <h3>Logs Content:</h3>
                <div class="table-responsive">
                    <table id="logsTable" class="table table-striped">
                        <thead>
                            <tr>
                                <th>Log Type</th>
                                <th>Content</th>
                            </tr>
                        </thead>
                        <tbody>
    """
    
    # Populate the logs content table with full log content
    for log in logs:
        row_class = log['log_name'].replace("_", "").lower()  # Log name to class for coloring
        log_content = "".join(log['content'])
        html_content += f"""
            <tr class="{row_class}">
                <td>{log['log_name']}</td>
                <td class="log-content">{log_content}</td>
            </tr>
        """
    
    html_content += """
                    </tbody>
                </table>
                </div>

                <h3>Windows User List:</h3>
                <pre>{user_list}</pre>

                <h3>Active Network Connections:</h3>
                <table class="table table-striped">
                    <thead>
                        <tr>
                            <th>Local Address</th>
                            <th>Remote Address</th>
                            <th>Status</th>
                        </tr>
                    </thead>
                    <tbody>
    """
    
    for conn in active_connections:
        html_content += f"""
            <tr>
                <td>{conn['local_address']}</td>
                <td>{conn['remote_address']}</td>
                <td>{conn['status']}</td>
            </tr>
        """
    
    html_content += """
                    </tbody>
                </table>

                <h3>Disk Usage:</h3>
                <table class="table table-striped">
                    <thead>
                        <tr>
                            <th>Partition</th>
                            <th>Used Space</th>
                            <th>Free Space</th>
                        </tr>
                    </thead>
                    <tbody>
    """
    
    for disk in disk_usage:
        html_content += f"""
            <tr>
                <td>{disk['caption']}</td>
                <td>{disk['filesystem']}%</td>
            </tr>
        """
    
    html_content += """
                    </tbody>
                </table>
            </div>
            <script>
                $(document).ready(function() {{
                    $('#logsTable').DataTable();
                }});
            </script>
        </body>
    </html>
    """
    
    return html_content

# Main function to generate report
def main():
    logs = collect_logs()
    system_info = get_system_info()
    user_list = get_windows_user_list()
    active_connections = get_active_network_connections()
    disk_usage = get_disk_usage()
    
    html_report = generate_html_report(logs, system_info, user_list, active_connections, disk_usage)
    
    # Save the HTML report to a file
    with open("forensic_report.html", "w") as f:
        f.write(html_report)

    def typing_animation(text, delay=0.01):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

    print("\033[32m")

    typing_animation("\n*********************************************************************************")
    typing_animation("*  Server forensic report generated successfully!  *")
    typing_animation("*  Forensic report generated successfully as 'forensic_report.html'.  *")
    typing_animation("*  This Tool is Developed by Muhammad Sudais Usmani *")
    typing_animation("***********************************************************************************\n")

    print("\033[0m")

# Run the script
main()
