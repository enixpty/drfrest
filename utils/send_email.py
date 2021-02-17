from django.core.mail import EmailMessage
import os 
class send:

    @staticmethod
    def send_email(data):
        """ send email from smpt method """

        email = EmailMessage(
            data['email_subject'],
            data['email_body'],
            os.environ.get('EMAIL_HOST_USER'),
            [data['to_email']],
            headers = {'Message-ID' : 'foo'}
        ) 
        
        email.send()