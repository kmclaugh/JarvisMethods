#!/usr/bin/python3.2
jarvis_username = 'antonshipley@gmail.com'
jarvis_password = 'TradecraftOlympic1865'
def textsender(number,message):
    global username
    username = jarvis_username
    global password
    password = jarvis_password

    import smtplib

    server = smtplib.SMTP( "smtp.gmail.com", 587 )
    server.starttls()
    server.login( username, password )

    server.sendmail( 'kevin', '{0}@mms.att.net'.format(number), '{0}'.format(message) )




