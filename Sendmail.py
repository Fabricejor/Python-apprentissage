import smtplib

sender = "iss654864@gmail.com"
password = "fjxhsladuowjkygl"
reciever = input("Please enter your mail:")
subject = input("Please enter the subject: ")
message = input("Please enter message:")
text =f"Subject:{subject}\n\n {message}"

server= smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
if server.login(sender,password):
    print("connected successfully")
else:
    print ("Failed to login")
server.send_message(sender,reciever,message)
print("L'email a été envoyé à:" + reciever)