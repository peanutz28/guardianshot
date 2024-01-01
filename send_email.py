import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, to_email, smtp_server, smtp_port, smtp_username, smtp_password):
    # Create the MIME object
    msg = MIMEMultipart()
    msg['From'] = smtp_username
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach the body to the email
    msg.attach(MIMEText(body, 'plain'))

    # Establish a connection to the SMTP server
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        # Log in to the SMTP server
        server.starttls()
        server.login(smtp_username, smtp_password)

        # Send the email
        server.sendmail(smtp_username, to_email, msg.as_string())

# Example usage
subject = "Test Email"
body = "This is a test email from Raspberry Pi."
to_email = "riasaheta@gmail.com"
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = "riasaheta7@gmail.com"
smtp_password = "xgps gwlf mkmm umxs"

send_email(subject, body, to_email, smtp_server, smtp_port, smtp_username, smtp_password)

