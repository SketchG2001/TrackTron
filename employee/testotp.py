
import smtplib
from socket import gaierror

smtp_host = 'smtp.gmail.com'
smtp_port = 587
smtp_user = 'testingsketch@gmail.com'
smtp_password = 'bplf oskl jrgw joqx'

try:
    server = smtplib.SMTP(smtp_host, smtp_port)
    server.starttls()
    server.login(smtp_user, smtp_password)
    print("SMTP connection successful")
except gaierror as e:
    print(f"Failed to connect to SMTP server: {e}")
except smtplib.SMTPAuthenticationError as e:
    print(f"SMTP authentication failed: {e}")
except Exception as e:
    print(f"SMTP connection error: {e}")
finally:
    if 'server' in locals():
        server.quit()  # Close the SMTP connection if it was successfully opened

