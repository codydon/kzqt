from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication
from django.http import JsonResponse,Http404
import json, jwt, datetime
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import make_password
from .models import Employee, Assets, LeaveDays, Notification
from .serializers import AssetSerializer, EmployeeSerializer, LeaveSerializer, NotificationSerializer
from .pusher import pusher_client
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password
from rest_framework.exceptions import AuthenticationFailed

class NotifyViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all().order_by('id')
    serializer_class = NotificationSerializer
    authentication_classes = [BasicAuthentication]


    def post(self, request):
        message = request.data['message']
        EmpId = request.data['EmpId']
        
        notification = Notification(EmpId=EmpId, message=message)
        notification.save()

        pusher_client.trigger('notify', 'notification', {
            'message': request.data['message'],
            })
        
        return Response([])
    
    def get_notifications(self, request):
        try:
            notifications = Notification.objects.filter(is_read=False).order_by('-timestamp')

            messages = [n.message for n in notifications]

            notifications.update(is_read=True)

            return JsonResponse({"success": True, "notifications": messages})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

   

    def update_read(self, request):
        notifications = Notification.objects.filter(is_read=False)
        notifications.update(is_read=True)
        return JsonResponse({'success': True})


class AssetsViewSet(viewsets.ModelViewSet):
    queryset = Assets.objects.all().order_by('AssetId')
    serializer_class = AssetSerializer
    authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    def fetch_assets(self, request, eid):
        try:
            assets = Assets.objects.filter(EmpId=eid).values() # convert QuerySet to list of dictionaries
            return JsonResponse({'success': True, 'assets': list(assets)}, status=200) # convert QuerySet to list
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)


    def destroy(self, request, pk):
        try:
            asset = Assets.objects.get(AssetId=pk)
            asset.delete()
            return JsonResponse({'success': True}, status=200)
        except Http404:
            return JsonResponse({'message': 'Asset not found.'}, status=404)
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=500)

    def add_asset(self, request):
        if request.method == 'POST':
            data = json.loads(request.body)
            try:
                asset_name = data['name']
                asset_id = data['id']
                description = data['description']
               

                # Create a new asset object with the employee object and save it to the database
                asset = Assets(
                    AssetName=asset_name,
                    AssetId=asset_id,
                    Description=description,
                )
                asset.save()

                # Return a success response
                return JsonResponse({'success': True})

            except Exception as e:
                # If there is an error, return an error response
                return JsonResponse({'error': str(e)}, status=500)

    def get_assets(self, request):
        if request.method == 'GET':
            # Retrieve all assets from the database
            assets = Assets.objects.all()
            # Create a list to store serialized asset objects
            serialized_assets = []
            for asset in assets:
                serialized_asset = {
                    'employeeId': asset.EmpId,
                    'asset_name': asset.AssetName,
                    'asset_id': asset.AssetId,
                    'description': asset.Description,
                    'assigned_status': asset.Assigned
                    }
                serialized_assets.append(serialized_asset)
            return JsonResponse({'success': True, 'assets': serialized_assets}, status=200)
        else:
            return JsonResponse({'success': False}, status=500)
        




    def update_asset(self, request):
        if request.method == 'POST':
            data = json.loads(request.body)
            asset_id= data['asset_id']
            try:
                asset = get_object_or_404(Assets, AssetId=asset_id)
            except Assets.DoesNotExist:
                return JsonResponse({'resp': 'Asset does not exist'})
            
            asset.AssetName = data['asset_name']
            asset.Description = data['description']
            asset.save()
            return JsonResponse({'success': True }, status=200)
        else:
            return JsonResponse({'error': 'Invalid request method'}, status=405)
        
    def assign_asset(self, request):
        try:
            if request.method == 'POST':
                data = json.loads(request.body)
                asset_id= data['asset_id']
                try:
                    asset = get_object_or_404(Assets, AssetId=asset_id)
                except Assets.DoesNotExist:
                    return JsonResponse({'resp': 'Asset does not exist'}, status=500)
                except Http404:
                    return JsonResponse({'resp': 'Asset does not exist'}, status=404)
            
                
                asset.EmpId = data['employee_id']
                asset.Assigned = True
                asset.save()
                return JsonResponse({'success': True, 'data': data}, status=200)
            else:
                return JsonResponse({'error': 'Invalid request method'}, status=405)
        except Exception as e:
                return JsonResponse({'error': str(e) }, status=500)

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('EmployeeId')
    serializer_class = EmployeeSerializer
    authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    def update_profile(self, request):
        if request.method == 'POST':
            try:
                data = json.loads(request.body)
                Employee.objects.filter(EmployeeId=data['EmployeeId']).update(
                    Name=data['Name'],
                    email=data['email'],
                    PhoneNumber=data['PhoneNumber'],
                    DOB=data['DOB'],
                    KRAPIN=data['KRAPIN'],
                    IDnumber=data['IDnumber']
                )
                return JsonResponse({'success': True})
            except Exception as e:
                return JsonResponse({'success': False, 'error': str(e)})

    def change_employee_role(self, request, eid):
        if request.method == "PUT":
            data = json.loads(request.body)
            try:
                employee = Employee.objects.get(EmployeeId=eid)
                new_role = data['role']
                employee.Role = new_role
                employee.save()
                response_data = {"success": True}
            except Employee.DoesNotExist:
                response_data = {"success": False, "error": "Employee does not exist"}
            except Exception as e:
                response_data = {"success": False, "error": str(e)}
            return JsonResponse(response_data)
        
    def get_employees(self, request):
        if request.method == 'GET':
            assets = Employee.objects.exclude(EmployeeId=None)
            # Create a list to store serialized asset objects
            serialized_assets = []
            for asset in assets:
                serialized_asset = {
                    'employee_id': asset.EmployeeId,
                    'employee_name': asset.Name,
                    'role': asset.Role,
                    # 'asset_id': asset.AssetId,
                    # 'description': asset.Description,
                    # 'assigned_status': asset.Assigned_status,
                }
                serialized_assets.append(serialized_asset)
            return JsonResponse({'success': True, 'employees': serialized_assets}, status=200)
        else:
            return JsonResponse({'success': False}, status=500)

    def create_employee(self, request):
        if request.method == 'POST':
            data = json.loads(request.body)
            verification_token = verification_token_generator.generate_verification_token()  # generate verification token
            employee = Employee.objects.create(
                Name=data['name'],
                email=data['email'],
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
    
    def reg_admin(self, request):
        if request.method == 'POST':
            data = json.loads(request.body)
            verification_token = verification_token_generator.generate_verification_token()  # generate verification token
            employee = Employee.objects.create(
                Name=data['name'],
                email=data['email'],
                Verification_token=verification_token,
                Role='admin',
                Company=data['company'],
                PhoneNumber=data['phone'],

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

            return JsonResponse({'success': True}, status=200)

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
        print(token)
        try:
            employee = Employee.objects.get(Verification_token=token)
        except Employee.DoesNotExist:
              return JsonResponse({'resp': 0 }, status=400)
        return JsonResponse({'resp': 1 }, status=200)
        
    def user_pass(self, request):
        try:
            if request.method == "POST":
                data = json.loads(request.body)
                token = data['token']
                pw = data['pw']
                #find the row with the token
                employee = get_object_or_404(Employee, Verification_token=token)
                # hash the password
                if employee.Verification_token == token and employee.Verification_token != 'verified':
                    if employee.Role == 'admin':
                        h_pw = make_password(pw)
                        last_emp = Employee.objects.latest('EmployeeId')
                        last_empId = last_emp.EmployeeId
                        if(last_empId is None):
                            empId = 'ADM_001'
                        else:
                            empId = "ADM_{:03d}".format(int(last_empId[4:]) + 1)
                        employee.Role = 'admin'
                    else:
                        h_pw = make_password(pw)
                        last_emp = Employee.objects.latest('EmployeeId')
                        last_empId = last_emp.EmployeeId
                        if(last_empId is None):
                            empId = 'EMP_001'
                        else:
                            empId = "EMP_{:03d}".format(int(last_empId[4:]) + 1)
                        employee.Role = 'unassigned'

                # return JsonResponse({'resp': empId}, status=200)
                # Update the password if the token matches
                    employee.EmployeeId = empId
                    employee.password = h_pw
                    employee.Verification_token = 'verified'
                    employee.Email_verified = True
                    employee.save()

                    #    send mail
                    try:
                        subject = "Kaziquest Staff Number"
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
                            <p> Your kaziquest staff number is : """+empId+"""
                            </p>
                        </h4>
                        </body>
                        </html>
                        """
                        self.send_email(subject, content,  employee.email)
                    except Exception as e:
                        return JsonResponse({'error': e})
            

                    return JsonResponse({'resp': 1, 'success': 'success'}, status=200)
    
                else:
                    return JsonResponse({'resp': 0}, status=500)
            else:
                return JsonResponse({'error': 'bad method'}, status=405)
        except Exception as e:
            return JsonResponse({'exception error': str(e)}, status=500)
        


    def getauth_user(self, request):
        if request.method == 'POST':
            data = json.loads(request.body)
            token = data['tkn']
            # token = request.COOKIES.get('jwt')
            if not token:
                return JsonResponse({'exception error': 'yyyy'}, status=500)

            try:
                payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            except jwt.ExpiredSignatureError:
                return JsonResponse({'exception error2': 'yyyy'}, status=500)

            user = Employee.objects.filter(EmployeeId=payload['id']).first()
            serializer = EmployeeSerializer(user)

            return JsonResponse({"success": True,  "user":serializer.data})
            # return JsonResponse({"success": tkn})

    def logout(self, request):
        response = Response()
        response.delete_cookie(key='jwt')
        response.data = {
            'jwt': None,
          'success': True
        }
        return response
    
    def emplogin(self, request):
        if request.method == 'POST':
            data = json.loads(request.body)
            employee_id = data.get('emp_id')
            password = data.get('pw')
            
            if not employee_id or not password:
                return JsonResponse({'error': 'Invalid employee ID or password'}, status=400)
            
            # Get the employee from the database
            employee = get_object_or_404(Employee, EmployeeId=employee_id)
            
            # Check if the password is correct
            if not check_password(password, employee.password):
                return JsonResponse({'error': 'Invalid employee ID or password'}, status=401)
            
            if not employee.Email_verified:
                return JsonResponse({'error': 'Email not verified'}, status=401)
            
            # Set the employee's session data to indicate that they are logged in
            payload = {
                'id': employee.EmployeeId,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=120),
                'iat': datetime.datetime.utcnow(),
            }
            token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

            response  = Response()
            response.set_cookie(key='jwt', value=token, httponly=True)
            response.data = {
                'jwt': token,
                'success': True,
                'id': employee.EmployeeId,
                'role': employee.Role,
            }

            return response 
            
            # Return a success response
            # return JsonResponse({'success': True})
        else:
            # Return an error response for invalid request methods
            return JsonResponse({'error': 'Invalid request method'}, status=405)

class LeaveDaysViewSet(viewsets.ModelViewSet):
    queryset = LeaveDays.objects.all().order_by('id')
    serializer_class = LeaveSerializer
    authentication_classes = [BasicAuthentication]

    def getRequests(self, request):
        try:
            r =  LeaveDays.objects.all().order_by('id')
            serializer = LeaveSerializer(r, many=True)
            return JsonResponse({'success': True, 'requests':serializer.data}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    def leave_request(self, request):
        if request.method == 'POST':
            data = json.loads(request.body)
            emp_id = data['eId']
            start = data['start_date']
            end = data['end_date']
            desc = data['description']

            if not emp_id or not start or not end or not desc:
                return JsonResponse({'error': 'fill all required fields'}, status=400)

            # Retrieve the employee instance using the emp_id
            try:
                employee = Employee.objects.get(EmployeeId=emp_id)
            except Employee.DoesNotExist:
                return JsonResponse({'error': 'Invalid employee ID'}, status=400)

            leave = LeaveDays.objects.create(
                StartDate=start,
                EndDate=end,
                Description=desc,
                EmpId=emp_id,
                Status="pending"
            )
            leave.save()
            return JsonResponse({"success": True}, status=200)
    
    def approveRequest(self, request):
        if request.method == 'PUT':
            data = json.loads(request.body)
            leave_id = data['id']
            status = data['status']

            if not leave_id or not status:
                return JsonResponse({'error': 'fill all required fields'}, status=400)

            try:
                leave = LeaveDays.objects.get(id=leave_id)
            except LeaveDays.DoesNotExist:
                return JsonResponse({'error': 'Invalid leave ID'}, status=400)

            leave.Status = status
            leave.save()
            return JsonResponse({"success": True}, status=200)
        

    
import hashlib
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

        
        




