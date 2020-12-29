import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("sender_email_ID", "gmail_App_password")
message = input("Enter your test case format here(press enter only at the end): ")
try:
    s.sendmail("sender_email_ID", "receiver_email_ID", message)
    print("Mail sent successfully, Thank you")
    s.quit()
except SMTPException:
    print("Error: unable to send mail")
