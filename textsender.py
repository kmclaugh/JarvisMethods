#!/Library/Frameworks/Python.framework/Versions/3.2/bin/python3.2

def textsender(number,message):

    import smtplib

    server = smtplib.SMTP( "smtp.gmail.com", 587 )
    server.starttls()
    server.login( 'antonshipley@gmail.com', 'F=kqq/r2' )

    server.sendmail( 'kevin', '{0}@mms.att.net'.format(number), '{0}'.format(message) )




