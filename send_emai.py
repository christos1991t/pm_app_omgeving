import smtplib as sm
import ssl


def send_email(message_user):
    host = "smtp.gmail.com"
    port = 465

    username = "cjgh2007@gmail.com"
    password = "hxyntdfnrwolhzje"
    mail_user = "cjgh2007@gmail.com"

    context = ssl.create_default_context()

    with sm.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, mail_user, message_user)
