import smtplib, ssl


def send_email(message):
    host = 'smtp.gmail.com'
    port = 465

    # Information for your sender email, please check the attached
    # README file for reference
    sender = 'your-gmail-account@gmail.com'
    password = 'your-app-password'

    receiver = 'your-receiver@gmail.com'
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, message)
