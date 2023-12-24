import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime

dir =os.path.dirname(os.path.abspath(__file__))
newfile=dir+f"\\Daily Newsletters\\{datetime.date.today()}.html"

# SMTP server configuration (for Gmail)
smtp_server = 'smtp.gmail.com'
smtp_port = 587  # Port 587 is for TLS
print("hey")
sender_email = os.environ.get('EMAIL_USERNAME')
sender_password = os.environ.get('EMAIL_PASSWORD')
print(sender_password)
# Create an SMTP object and establish a connection
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()  # Use TLS encryption
print("eleven")
# Log in to the SMTP server
server.login(sender_email, sender_password)
print("ten")
# Compose the email
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = 'livetigan@gmail.com'
msg['Subject'] = datetime.date.today().strftime("%B %d, %Y")+" Newsletter"
print("HIII")
# Read the HTML content from a file
with open(newfile, 'r') as html_file:
    html_content = html_file.read()

# Attach the HTML content as the email body
html_part = MIMEText(html_content, 'html')
msg.attach(html_part)

# Send the email
server.sendmail(sender_email, 'livetigan@gmail.com', msg.as_string())

# Close the connection
server.quit()
