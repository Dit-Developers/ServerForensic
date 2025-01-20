# ServerForensic

**Web Server Forensic Tool** for collecting logs, system information, and identifying active services running on web servers (Apache, MySQL, Nginx, PHP). This tool generates a forensic report in HTML format with a clean and responsive UI using **Bootstrap**. It supports **XAMPP** and **WAMP** servers on Windows and **Apache** on Linux systems.

## Features

- **OS Detection**: Identifies the operating system of the server (Linux or Windows).
- **Service Detection**: Detects running services such as Apache, MySQL, PHP, and Nginx based on the OS.
- **Log Collection**: Collects key server logs like `access.log`, `error.log`, `ssl_request.log`, and more.
  - Supports both **XAMPP** and **WAMP** servers on Windows.
  - Supports **Apache** logs on Linux.
- **System Information**: Collects system information such as:
  - Uptime
  - CPU Info
  - Memory Info
  - File System Info
- **Responsive HTML Report**: Generates an HTML report with a yellow banner and a clean layout, utilizing **Bootstrap** for responsiveness.
- **GitHub & LinkedIn Links**: Includes links to the project's **GitHub** and **LinkedIn** profiles in the navigation bar.

## Installation

1. **Prerequisites**:
   - Python 3.x installed on your machine.
   - Required Python libraries: `platform`, `subprocess`.

2. **Clone the Repository**:
   Clone the repository to your local machine or download the files from GitHub:

```bash
git clone https://github.com/Dit-Developers/ServerForensic.git
```
3. **Install Dependencies**:
You don't need to install any external dependencies as the code primarily uses Python's built-in libraries like `platform`, `subprocess`, and `os`.

4. **Run the Script**:
After cloning or downloading the project, navigate to the project directory in your terminal or command prompt.

Run the Python script to generate the forensic report:
```bash
python web_server_forensic.py
```
5. **View the Report**:
After running the script, it will generate an HTML report named `server_forensic_report.html`. Open this file in any browser to view the detailed forensic report.

The forensic report will include the following sections:
- **Logs**: Displaying collected logs for Apache and MySQL services (if available).
- **System Information**: Displaying system details such as CPU, memory, file system, etc.
- **Navigation Bar**: Includes links to **GitHub** and **LinkedIn** profiles.

**Report Output like**
```bash
# Server Forensic Report

**Report generated at:** 2025-01-20 15:45:32  
**Operating System:** Windows

## System Information:

| Metric             | Value      |
|--------------------|------------|
| **CPU Usage**      | 15%        |
| **Memory Usage**   | 60%        |
| **Disk Usage**     | 78%        |
| **Network Interfaces** | Ethernet, Wi-Fi |

## Log Paths:

| Log Type    | Log Path                                              |
|-------------|-------------------------------------------------------|
| **access_log**  | `C:\xampp\apache\logs\access.log`                     |
| **error_log**   | `C:\xampp\apache\logs\error.log`                      |
| **httpd_pid**   | `C:\xampp\apache\logs\httpd.pid`                      |
| **install_log** | `C:\xampp\apache\logs\install.log`                    |
| **ssl_log**     | `C:\xampp\apache\logs\ssl_request.log`                |

## Logs Content:

| Log Type    | Content                                                                 |
|-------------|-------------------------------------------------------------------------|
| **access_log**  | `127.0.0.1 - - [20/Jan/2025:15:30:01 +0000] "GET /index.html HTTP/1.1" 200 432` |
| **error_log**   | `AH00558: apache2: Could not reliably determine the server's fully qualified domain name` |
| **httpd_pid**   | `12345`                                                                 |
| **install_log** | `Installing Apache 2.4.51`                                             |
| **ssl_log**     | `ssl_error: Certificate Expired`                                      |

## Windows User List:

| **User List** |
|---------------|
| Administrator |
| User1         |
| Guest         |

## Active Network Connections:

| **Local Address**   | **Remote Address**  | **Status**     |
|---------------------|---------------------|----------------|
| 192.168.1.2:80     | 192.168.1.5:123     | ESTABLISHED    |
| 192.168.1.2:443    | 192.168.1.4:80      | LISTENING      |

## Disk Usage:

| **Partition** | **Used Space (%)** |
|---------------|--------------------|
| C:\           | 80%                |
| D:\           | 55%                |
```

## Contribution

Contributions are welcome! If you want to add features, improve the code, or fix bugs, please submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

- **GitHub**: [https://github.com/Dit-Developers/ServerForensic](https://github.com/Dit-Developers/ServerForensic)
- **LinkedIn**: [https://www.linkedin.com/in/muhammad-sudais-usmani-950889311/](https://www.linkedin.com/in/muhammad-sudais-usmani-950889311/)

---

This script generates a forensic report from the server logs and system information of your machine. It collects essential data including Apache/XAMPP logs, system resource usage (CPU, memory, disk), active network connections, and more. Developed by Muhammad Sudais Usmani, the tool is designed to assist forensic investigators in gathering valuable system data for analysis.

It collects and displays Apache/XAMPP logs (for both Linux and Windows platforms), fetches system information like CPU, memory, disk usage, and network interfaces, and generates detailed HTML reports with logs, system info, network connections, and disk usage. The script supports both Windows and Linux environments.

No installation is required. Simply run the Python script on your server or local machine. Prerequisites include Python 3.x installed and the required Python libraries: `psutil`, `platform`, `subprocess`, and `os`.

To execute the forensic report generation, run:
```bash
python web_server_forensic.py
```
The script will generate an HTML report named `forensic_report.html` in the same directory as the script.

The generated report contains:
- **System Information**: Details about CPU, memory, disk usage, and network interfaces.
- **Logs**: Apache/XAMPP logs, including access, error, SSL, and more, along with their content.
- **Windows User List**: List of users on Windows systems.
- **Active Network Connections**: List of active network connections with local and remote addresses and statuses.
- **Disk Usage**: Information about disk usage on different partitions.

Below is an overview of the script's structure:
- `detect_os`: Detects the operating system of the machine.
- `collect_logs`: Collects relevant logs based on the OS (Windows for XAMPP, Linux for Apache).
- `read_log_content`: Reads the content of the log files.
- `get_system_info`: Fetches system resource usage details using the `psutil` library.
- `generate_html_report`: Generates a styled HTML report based on collected data.
- `main`: The entry point of the script, which runs the above functions and generates the final report.

This project is licensed under the MIT License - see the LICENSE file for details. If you have any questions, feel free to reach out to me on LinkedIn or visit my GitHub page.

