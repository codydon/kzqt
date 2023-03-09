from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Employee, LeaveDays, Assets, AssetTrack

# Create your views here.

def index(request):
    return HttpResponse("Hello, world! This is the index page.")

def d(request):
    return HttpResponse("dummyf")

def create_employee(request):
    return "nmefika"
    if request.method == 'POST':
        # Get the form data from the request
        name = request.POST['name']
        dob = request.POST['dob']
        phone_number = request.POST['phone_number']
        id_number = request.POST['id_number']
        krapin = request.POST['krapin']
        email = request.POST['email']
        role = request.POST['role']
        password = request.POST['password']
        
        # Create a new Employee instance with the form data
        employee = Employee(name=name, DOB=dob, PhoneNumber=phone_number, IDnumber=id_number, KRAPIN=krapin, Email=email, Role=role, Password=password)
        
        # Save the Employee instance to the database
        employee.save()
        
        # Redirect to a success page
        return render(request, 'success.html')
    
    # Render the employee creation form
    return render(request, 'create_employee.html')

# //saving leave details
def create_leave(request):
    if request.method == 'POST':
        # Get the form data from the request
        employee_id = request.POST['employee_id']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        description = request.POST['description']
        status = request.POST['status']
        
        # Retrieve the employee associated with the given ID
        employee = Employee.objects.get(pk=employee_id)
        
        # Create a new LeaveDays instance with the form data and the retrieved employee
        leave = LeaveDays(EmployeeId=employee, startDate=start_date, EndDate=end_date, Description=description, Status=status)
        
        # Save the LeaveDays instance to the database
        leave.save()
        
        # Redirect to a success page
        return render(request, 'success.html')
    
    # Render the leave creation form
    return render(request, 'create_leave.html')

def create_asset(request):
    if request.method == 'POST':
        # Get the form data from the request
        employee_id = request.POST['employee_id']
        asset_name = request.POST['asset_name']
        asset_id = request.POST['asset_id']
        description = request.POST['description']
        
        # Retrieve the employee associated with the given ID
        employee = Employee.objects.get(pk=employee_id)
        
        # Create a new Assets instance with the form data and the retrieved employee
        asset = Assets(EmployeeId=employee, AssetName=asset_name, AssetId=asset_id, Description=description)
        
        # Save the Assets instance to the database
        asset.save()
        
        # Redirect to a success page
        return render(request, 'success.html')
    
    # Render the asset creation form
    return render(request, 'create_asset.html')


def create_asset_track(request):
    if request.method == 'POST':
        # Get the form data from the request
        asset_id = request.POST['asset_id']
        date_issued = request.POST['date_issued']
        condition_issued = request.POST['condition_issued']
        issued_desc = request.POST['issued_desc']
        date_returned = request.POST['date_returned']
        condition_returned = request.POST['condition_returned']
        returned_desc = request.POST['returned_desc']
        
        # Retrieve the asset associated with the given ID
        asset = Assets.objects.get(pk=asset_id)
        
        # Create a new AssetTrack instance with the form data and the retrieved asset
        asset_track = AssetTrack(AssetId=asset, DateIssued=date_issued, ConditionIssued=condition_issued,
                                 IssuedDesc=issued_desc, DateReturned=date_returned,
                                 ConditionReturned=condition_returned, ReturnedDesc=returned_desc)
        
        # Save the AssetTrack instance to the database
        asset_track.save()
        
        # Redirect to a success page
        return render(request, 'success.html')
    
    # Render the asset track creation form
    return render(request, 'create_asset_track.html')

def get_employee(request):
    employees = Employee.objects.all().values()
    return JsonResponse({'employees': list(employees)})

def get_leave_days(request):
    leave_days = LeaveDays.objects.all().values()
    return JsonResponse({'leave_days': list(leave_days)})

def get_assets(request):
    assets = Assets.objects.all().values()
    return JsonResponse({'assets': list(assets)})

def get_asset_track(request):
    asset_track = AssetTrack.objects.all().values()
    return JsonResponse({'asset_track': list(asset_track)})



