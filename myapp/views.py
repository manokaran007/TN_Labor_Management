from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login ,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from .models import UserProfile, Complaint
import smtplib
from email.message import EmailMessage


def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        photo = request.FILES.get('photo')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        state = request.POST.get('state')
        contact = request.POST.get('contact')
        department = request.POST.get('department')
        bank = request.POST.get('bank')
        current_location = request.POST.get('current-location')
        working_state = request.POST.get('working-state')
        location = request.POST.get('location')
        experience = request.POST.get('experience')
        district = request.POST.get('district')
        occupation = request.POST.get('occupation')
        salary = request.POST.get('salary')
        vaccine = request.POST.get('vaccine')
        employer = request.POST.get('employer')
        marital_status = request.POST.get('marital-status')

        UserProfile.objects.create(
            name=name,
            photo=photo,
            email=email,
            dob=dob,
            gender=gender,
            address=address,
            state=state,
            contact=contact,
            department=department,
            bank=bank,
            current_location=current_location,
            working_state=working_state,
            location=location,
            experience=experience,
            district=district,
            occupation=occupation,
            salary=salary,
            vaccine=vaccine,
            employer=employer,
            marital_status=marital_status,
        )
        
        cuser=User.objects.create_user(contact,email,password)
        print(cuser)

        cuser.save()
        
        if cuser:
            send_email(request,email,name)

        return redirect('login')  

    return render(request, 'register.html')
@login_required
def updateprofile(request):
    user = request.user
    profile = get_object_or_404(UserProfile, contact=request.user)

    if request.method == 'POST':
        profile.name = request.POST.get('name')
        profile.email = request.POST.get('email')
        profile.dob = request.POST.get('dob')
        profile.gender = request.POST.get('gender')
        profile.address = request.POST.get('address')
        profile.state = request.POST.get('state')
        profile.contact = request.POST.get('contact')
        profile.department = request.POST.get('department')
        profile.bank = request.POST.get('bank')
        profile.current_location = request.POST.get('current-location')
        profile.working_state = request.POST.get('working-state')
        profile.location = request.POST.get('location')
        profile.experience = request.POST.get('experience')
        profile.district = request.POST.get('district')
        profile.occupation = request.POST.get('occupation')
        profile.salary = request.POST.get('salary')
        profile.vaccine = request.POST.get('vaccine')
        profile.employer = request.POST.get('employer')
        profile.marital_status = request.POST.get('marital-status')


        profile.email = request.POST.get('email') or user.email

        if request.FILES.get('photo'):
            profile.photo = request.FILES.get('photo')

        profile.save()
        return redirect('profile')  # Redirect after successful update

    context = {
        'name': profile.name,
        'email': profile.email,
        'contact': profile.contact,
        'photo': profile.photo,
        'dob': profile.dob,
        'gender': profile.gender,
        'address': profile.address,
        'state': profile.state,
        'department': profile.department,
        'bank': profile.bank,
        'current_location': profile.current_location,
        'working_state': profile.working_state,
        'location': profile.location,
        'experience': profile.experience,
        'district': profile.district,
        'occupation': profile.occupation,
        'salary': profile.salary,
        'vaccine': profile.vaccine,
        'employer': profile.employer,
        'marital_status': profile.marital_status,
    }

    return render(request, 'update_profile.html', context)
@staff_member_required
def admin_home(request):
    return render(request, 'admin_home.html')
def user_login(request):
    if (request.method == 'POST'):
        uname = request.POST.get('mobile')
        pword = request.POST.get('password')
        users = authenticate(request,username=uname,password=pword)
        print(uname,pword)
        print(users)
        if users:
            if users.is_superuser:
                
                login(request,users)
                return redirect('admin_home')
                
            else:
                login(request,users)
                return redirect('home')
        else:
            return HttpResponse("Username or password is incorrect")
       
        
    return render(request,'login.html')

@login_required
def home(request):
   
    
    name =  UserProfile.objects.get(contact=request.user)
    print(name.name)
    return render(request,'home.html',{'user':name.name})

@login_required
def profile(request):
    profile = get_object_or_404(UserProfile, contact=request.user)

    context = {
        'name': profile.name,
        'email': profile.email,
        'contact': profile.contact,
        'photo': profile.photo,
        'dob': profile.dob,
        'gender': profile.gender,
        'address': profile.address,
        'state': profile.state,
        'department': profile.department,
        'bank': profile.bank,
        'current_location': profile.current_location,
        'working_state': profile.working_state,
        'location': profile.location,
        'experience': profile.experience,
        'district': profile.district,
        'occupation': profile.occupation,
        'salary': profile.salary,
        'vaccine': profile.vaccine,
        'employer': profile.employer,
        'marital_status': profile.marital_status,
    }

    return render(request, 'profile.html', context)


def complaint(request):
    profile = get_object_or_404(UserProfile, contact=request.user)
    if request.method == 'POST':
        name = profile.name
        contact = profile.contact
        email = profile.email
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        Complaint.objects.create(
            name=name,
            contact=contact,
            email=email,
            subject=subject,
            message=message
        )
        complaint_email(request,email,name,subject)
        return redirect('complaint_success')  # Replace with success URL or page
    return render(request, 'complaint.html', {'complaint': {}})

def complaint_success(request):
    return render(request, 'complaint_success.html')
def complaint_email(request,to_email,name,subject):
    # complaint = Complaint.objects.get(email=to_email)
    
            
    msg = EmailMessage()
    msg['From'] = 'tamilnadulabour2025@gmail.com'
    msg['To'] = to_email
    msg['Subject'] = 'Complaint Submitted'
    content = f"Hi {name}  Your complaint  for {subject} is successful sent to Tamil Nadu Govt. Login to check your profile."
    msg.set_content(content)

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.starttls()
            smtp.login('tamilnadulabour2025@gmail.com', 'bisl ssuv ywqz sxiw')
            smtp.send_message(msg)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

    return 

def complaint_status(request):
    complaints = Complaint.objects.filter(contact=request.user)  # or request.user.phone if needed
    return render(request, 'complaint_status.html', {'complaints': complaints})

@staff_member_required
def update_status_page(request):
    message = ''
    if request.method == 'POST':
        complaint_id = request.POST.get('complaint_id')
        try:
            complaint = Complaint.objects.get(id=complaint_id)
            complaint.status = 'solved'
            complaint.save()
            message = f"Complaint ID {complaint_id} marked as solved."
            status_send_email(request,complaint.email,complaint.name,complaint.subject)
        except Complaint.DoesNotExist:
            message = "Complaint not found."

    return render(request, 'update_status.html', {'message': message})
@staff_member_required
def show_complaint_status(request):
    processing_complaints = Complaint.objects.filter(status='processing')
    solved_complaints = Complaint.objects.filter(status='solved')

    context = {
        'processing_complaints': processing_complaints,
        'solved_complaints': solved_complaints,
    }

    return render(request, 'complaint_status_list.html', context)

def status_send_email(request,to_email,name,subject):
    msg = EmailMessage()
    msg['From'] = 'tamilnadulabour2025@gmail.com'
    msg['To'] = to_email
    msg['Subject'] = 'Problem Solved'
    content = f"Hi {name} Your complaint for {subject} is successfully solved. Login to check your profile."
    msg.set_content(content)

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.starttls()
            smtp.login('tamilnadulabour2025@gmail.com', 'bisl ssuv ywqz sxiw')
            smtp.send_message(msg)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

    return 
def help(request):
    return render(request, 'help.html')

def about(request):
    return render(request, 'about.html')

def send_email(request,to_email,name):
    msg = EmailMessage()
    msg['From'] = 'tamilnadulabour2025@gmail.com'
    msg['To'] = to_email
    msg['Subject'] = 'Registration Successful'
    content = f"Welcome {name} Your Registration is successful in Tamil Nadu Govt. Job Portal. Login to check your profile."
    msg.set_content(content)

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.starttls()
            smtp.login('tamilnadulabour2025@gmail.com', 'bisl ssuv ywqz sxiw')
            smtp.send_message(msg)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

    return 
def user_logout(request):
    logout(request)  # This clears the session and logs out the user
    return redirect('login')  # Redirect to login page after logout


def custom_404_view(request, exception):
    return render(request, '404.html', status=404)

