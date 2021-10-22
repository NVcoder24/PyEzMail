import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class MIMEParts:
  TEXT = "plain"
  HTML = "html"

class Message:
  def __init__(self, subject:str):
    self.message = MIMEMultipart("alternative")
    self.message["Subject"] = subject
  
  def attach(self, part:str="", value:str=""):
    self.message.attach(MIMEText(value, part))
  
  def attach_data(self, sender:str, receiver:str):
    message = MIMEMultipart("alternative")
    message["From"] = sender
    message["To"] = receiver
  
  def as_string(self):
    return self.message.as_string()
  
  def __str__(self) -> str:
    return f"PyEzMail message\nData:\n{self.message.as_string()}"


class MailUser:
  def __init__(self, address:str, password:str):
    self.ssl = ssl.create_default_context()
    self.server = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=self.ssl)
    self.email = address
    self.password = password

  def send(self, message:Message, receiver:str):
    with self.server as server:
      server.login(self.email, self.password)
      message.attach_data(self.email, receiver)
      server.sendmail(self.email, receiver, message.as_string())

  def __str__(self):
    return f"PyEzMail user\nUser: {self.email}"