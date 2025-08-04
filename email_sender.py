from email.mime.text import MIMEText
import smtplib

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