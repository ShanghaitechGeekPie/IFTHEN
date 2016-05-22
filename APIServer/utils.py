def sendmail(to, msg):
    try:
        import smtplib
        from email.mime.text import MIMEText
        msg = MIMEText(msg)

        msg['Subject'] = 'Notification from IFTHEN'
        msg['From'] = 'revolutionist@163.com'
        msg['To'] = to
        s = smtplib.SMTP('smtp.163.com')
        s.login('revolutionist', 'c5201314')
        s.send_message(msg)
        s.quit()
        return 'succeed'
    except:
        return 'failed'
