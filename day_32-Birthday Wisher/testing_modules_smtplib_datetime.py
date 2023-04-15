
# import smtplib
#
# #  define my email address
# my_email = "santiclo.gohan@gmail.com"
# my_password = "testingground789"
# message = "Subject:This is a test\n\nThis is the body. Happyt birthday."
#
# #  establish my SMTP connection
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     #  call to start TLS to secure/encrypt our email connection
#     connection.starttls()
#     connection.login(user=my_email, password=my_password)
#
#     connection.sendmail(from_addr=my_email, to_addrs="santiclo.gohan@yahoo.com", msg=message)

import datetime as dt

now = dt.datetime.now()
print(now)
