# paramiko-memory-monitor-alert
This python script is designed to monitor memory usage on a remote server via paramiko library and send email alerts if the available memory falls below a specified threshold. This ensures that you can take timely action to prevent potential issues due to low memory.

## Features

- Connects to a remote server using SSH
- Checks available memory in GB
- Sends email alerts if memory is below a specified threshold
- Configurable settings for server and email credentials
- Scheduled to run daily at a specific time

## Prerequisites

- Python 3.x
- Required Python libraries:
  - `paramiko`
  - `schedule`
  - `smtplib`
  - `email`
  - `datetime`

You can install the necessary libraries using `pip`:

```bash
pip install paramiko schedule
```

## Setup

1. **Clone the repository:**

```bash
git clone https://github.com/usamaabidai1/paramiko-memory-monitor-alert.git
cd paramiko-memory-monitor-alert
```

2. **Create a configuration file:**

Create a file named `config.py` and add the following content:

```python
# Server credentials
hostname = ''
username = ''
password = ''
port = 22  # Default SSH port

# Email credentials
my_email = ''
my_password = ''
recipient_email = ''

# Schedule time
schedule_time = ''
```

Modify the values with your actual server and email credentials.

3. **Run the script:**

Execute the main script to start monitoring memory and sending alerts:

```bash
paramiko-memory-monitor-alert.py
```

## Files

- `paramiko-memory-monitor-alert.py`: Main script that monitors memory and sends email alerts
- `config.py`: Configuration file containing server and email credentials

## Usage

The script connects to the specified remote server, checks the available memory, and sends an email alert if the memory is below or equal to 5 GB. It runs daily at the configured time.

## Contribution

Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
