import smtplib, ssl
import sys

class send_email:
    
    def __init__(self, path=" ", sender_email = "user_email", password = "password", receiver_email = "reciever_email"):
        self.smtp_server = "smtp.gmail.com"
        self.port = 587  # For starttls            
        self.sender_email = sender_email
        self.password = password
        self.receiver_email = receiver_email
        if path != None:
            f = open(path,"r")
            lines = f.readlines()
            for line in lines:
                if "sender_email:" in line:
                    self.sender_email = line[14:]
                elif "password:" in line:
                    self.password = line[10:]
                elif "receiver_email:" in line:
                    self.receiver_email = line[16:]
        print(self.sender_email)
        print(self.password)
        print(self.receiver_email)
        #Create a secure SSL context
        self.context = ssl.create_default_context()

    def send(self):
        # Try to log in to server and send email
        try:
            server = smtplib.SMTP(self.smtp_server,self.port)
            server.ehlo() # Can be omitted
            server.starttls(context=self.context) # Secure the connection
            server.ehlo() # Can be omitted
            server.login(self.sender_email, self.password)
            message = self.compose_email()
            server.sendmail(self.sender_email, self.receiver_email, message)

        except Exception as e:
            # Print any error messages to stdout
            print(e)
        finally:
            server.quit() 
    
    def compose_email(self):
        message = """\
            Subject: Go to the hell, Fucking Porsche

            Go fuck yourself Porsche. """

        return message


def main():

    sender = send_email(path="./email_info_list.txt")

    print("Sending Eamil, go to hell Porsche!")
    sender.send()

if __name__ == "__main__":
    main()