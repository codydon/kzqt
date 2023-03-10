from rest_framework import viewsets
from .serializers import EmployeeSerializer
from .models import Employee
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse, HttpResponse
import json
from django.conf import settings

from django.template import Context
from django.core.mail import EmailMessage




class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('EmployeeId')
    serializer_class = EmployeeSerializer
    authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    def create(self, request):
        if request.method == 'POST':
            data = json.loads(request.body)
            verification_token = verification_token_generator.generate_verification_token()  # generate verification token
            employee = Employee(
                EmployeeId=data['employee_id'],
                Name=data['name'],
                DOB=data.get('dob', None),
                PhoneNumber=data.get('phone_number', None),
                IDnumber=data.get('id_number', None),
                KRAPIN=data.get('kra_pin', None),
                Email=data['email'],
                Role=data.get('role', None),
                Password=data.get('password', None),
                Email_verified=False,
                Verification_token=verification_token
            )
            
        #    send mail
            try:
                subject = "Kaziquest Verification Link"
                content = """
                <html>
                <head>
                <style>
                a {
                    color: #008080;
                    font-size: 30px;
                }
                p {
                    color: black;
                }
                </style>
                </head>
                <body>
                <h3>Click on this link to verify your email</h3>
                <h4>
                    <a href='"""+settings.F_URL+"""/verify_email/"""+verification_token+"""/'>
                        <h5>click here</h5>
                    </a>
                </h4>
                </body>
                </html>
                """
                self.send_email(subject, content,  data["email"])
            except Exception as e:
                return JsonResponse({'error': e})
            
            employee.save()

            return JsonResponse({'success': True, 'data': data})

        return JsonResponse({'success': False, 'error': 'Invalid request method'})
    
    def send_email(self, subject, content , recipient_list):
        smtp_server = settings.EMAIL_HOST
        smtp_port = settings.EMAIL_PORT
        smtp_username = settings.EMAIL_HOST_USER
        smtp_password = settings.EMAIL_HOST_PASSWORD

        message = MIMEMultipart("alternative")
        message["Subject"] = subject
        message["To"] = recipient_list

        
        body = MIMEText(content, "html")
        message.attach(body)
        
        import ssl

        try:
             # Create secure connection with server and send email
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", smtp_port, context=context) as server:
                server.login(smtp_username,  smtp_password)
                server.sendmail(smtp_server, recipient_list, message.as_string())
                print("EMAIL SENT")
        except Exception as e:
            print("Error sending email", e , smtp_password, smtp_username)

    def verify_email(self, request, token):
        # Check if the ID exists in the verification_token column of the Employee table
        try:
            employee = Employee.objects.get(Verification_token=token)
            return JsonResponse({'resp': 1 }, status=200)
        except Employee.DoesNotExist:
              return JsonResponse({'resp': 0 }, status=400)
    



   
    

import hashlib
import datetime
from django.contrib.auth.tokens import PasswordResetTokenGenerator


class VerificationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, timestamp):
        return hashlib.sha256(str(timestamp).encode('utf-8')).hexdigest()

    def generate_verification_token(self):
        timestamp = datetime.datetime.now().timestamp()
        hash_value = self._make_hash_value(timestamp)
        return hash_value


verification_token_generator = VerificationTokenGenerator()

import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailSender:
    def __init__(self, subject, message, recipient_list):
        self.subject = subject
        self.message = message
        self.recipient_list = recipient_list
        # self.email_from = os.environ.get('EMAIL_HOST_USER')
        self.email_from = "dev45cody@gmail.com"
        self.email_password = "#codyDon45"

    def send_email(self):
        msg = MIMEMultipart()
        msg['From'] = self.email_from
        msg['To'] = ', '.join(self.recipient_list)
        msg['Subject'] = self.subject
        msg.attach(MIMEText(self.message, 'plain'))

        try:
            smtp_server = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
            smtp_server.ehlo()
            smtp_server.starttls()
            smtp_server.login(self.email_from, self.email_password)
            smtp_server.sendmail(self.email_from, self.recipient_list, msg.as_string())
            smtp_server.quit()
        except Exception as e:
            print(str(e))

        
        




