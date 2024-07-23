import paramiko
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import date, datetime

hostname = '192.168.1.13'
username = 'sam'
password = 'asd@1441'
port = 22  # Default SSH port

# Create SSH client and connect to the server
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    client.connect(hostname=hostname, port=port, username=username, password=password)
except Exception as e:
    print(f"Failed to connect to the server: {e}")
    exit(1)

# Execute the command to check memory
mycmd = "free -g | grep Mem | awk '{print $7}'"
stdin, stdout, stderr = client.exec_command(mycmd)
mycmdout = stdout.read().decode().strip()

# Close the SSH connection
client.close()

# Check if the memory is less than or equal to 3 GB
if int(mycmdout) <= 5:
    # Define current date and time
    day = date.today()
    time = datetime.now()
    my_custom = day.strftime("%B %d %Y")
    current_time = time.strftime("%I:%M:%S %p")

    # Email credentials
    my_email = 'nasirhaneeffiverr@gmail.com'
    my_password = 'oetc oxvo jsjg almr'

    # Create the email message
    msg = MIMEMultipart()
    msg['Subject'] = f"ALERT: Memory Available {mycmdout} GB on JBOSS Server at {my_custom} {current_time}"
    msg['From'] = my_email
    msg['To'] = 'iusaamaabid@gmail.com'

    # HTML content for the email
    body = """
    <html>
      <body>
        <p><b><i>Hi Team,<br>Please check JBOSS server memory.</i></b></p>
      </body>
    </html>
    """
    msg.attach(MIMEText(body, 'html'))

    # Send the email
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()  # Secure the connection
            connection.login(user=my_email, password=my_password)
            connection.send_message(msg)
            print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
else:
    print(f"Memory available is {mycmdout} GB, no email sent.")
