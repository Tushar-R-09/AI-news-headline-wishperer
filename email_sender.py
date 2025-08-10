from email.mime.text import MIMEText
import smtplib
import os
from dotenv import load_dotenv


load_dotenv()  # Load variables from .env

sender_email = os.getenv("sender_email")
sender_password = os.getenv("sender_password")

# Function to send email
def send_email(summary, recipient_email, sender_email, sender_password):
    try:
        msg = MIMEText(summary)
        msg['Subject'] = 'Article Summary'
        msg['From'] = sender_email
        msg['To'] = recipient_email

        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())
        return True
    except Exception as e:
        return f"Error sending email: {str(e)}"