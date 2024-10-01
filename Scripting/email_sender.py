import smtplib
# for email transfer protocol
from email.message import EmailMessage
from string import Template
from pathlib import Path
# above two libraries if we want to use html in content (custom message) , look into docs
'''
#               only changes 
make an index.html file with vvariable as $name (name is variable name , key to dict)
html= Template(Path('index.html').read_text())
email.set_content(html.substitute({'name': 'tintin',..}),'html') 
'''
# send an email without opening browser
# navigate to google account app passwords to get password specific for the app

email = EmailMessage()
email['from'] = 'Swayam Singal'
email['to'] = 'swayamsingal.social@gmail.com'
email['subject'] = 'You won a million dollars!'

email.set_content('i am a python master') # can be anything , even html

with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('swayam.singal@gmail.com','litf umdo wyui mwes')
    smtp.send_message(email)
    print('all good boss')

