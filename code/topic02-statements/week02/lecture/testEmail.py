# send an email via gmail
# author Andrew Beatty

import smtplib

username = 'andrewbeattycourse@gmail.com'
password ='qqihejnivuhewpla'
toEmail = 'andrew.beatty@gmit.ie'
message = 'hi there'

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(username, password)
server.sendmail(username, toEmail, message)
