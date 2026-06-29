from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q
from .models import InternshipPosition, Company, Student, Application

# Create your views here.

# Home Page
def home(request):
    positions = InternshipPosition.objects.filter(status='open')
    companies = Company.objects.all()
    
    stats = {
        'total_positions' : InternshipPosition.objects.count(),
        'open_positions' : positions.count(),
        'total_companies' : companies.count()
    }
    
    return render(request, 'internship/home.html', {
        'positions': positions[:6],
        'companies': companies[:6],
        'stats' : stats
    })
    
  
# Browse All Positions...  
def browse_positions(request):
    positions = InternshipPosition.objects.filter(status='open')
    
    search = request.GET.get('search', '')
    location = request.GET.get('location', '')
    
    if search:
        positions = positions.filter(
            Q(title__icontians= search) | Q(description__icontains= search )
        )
    
    if location:
        positions = positions.filter( location__icontains= location)
        
    return render(request, 'internship/positions.html', {
        "positions": positions,
        "search": search,
        "location": location
    })
    
    
# positions Details
def position_detail(request, pk):
    position = get_object_or_404(InternshipPosition, pk= pk)
    can_apply = False
    already_applied = False
    
    if request.user.is_authenticated:
        try:
            student = Student.objects.get(user= request.user)
            can_apply = position.status == 'open'
            already_applied = Application.objects.filter(
                student = student,
                position= position
            )
        
        except Student.DoesNotExist:
            pass
        
    return render(request, 'internship/position_detail.html', {
        'position': position,
        'can_apply': can_apply,
        'already_applied' : already_applied
    })
    
# Apply for Position
@login_required
def apply_position(request, pk):
    position = get_object_or_404(InternshipPosition, pk= pk)
    
    try:
        student = Student.objects.get(user= request.user)
    except Student.DoesNotExist:
        messages.error(request, "Please complete your profile first.")
        return redirect('student_profile')
    
    if request.method == 'POST':
        cover_letter = request.POST.get('cover_letter')
        resume = request.FILES.get('resume')
        
        if Application.objects.filter(student= student, position= position).exists():
            messages.warning(request, 'You have already applied for this position.')
            return redirect('position_detail', pk= pk)
        
        Application.objects.create(
            student= student,
            position= position,
            cover_letter= cover_letter,
            resume= resume
        )
        
        messages.success(request, 'Application submitted successfully..!')
        return redirect('position_detail', pk= pk)
    
    return render(request, 'internship/apply.html', {'position' : position })


# Student Profile
@login_required
def student_profile(request):
    try:
        student = Student.objects.filter(user= request.user).first()
    except Student.DoesNotExist:
        student= None
        
    if request.method == "POST":
        if not student:
            student = Student.objects.get(user = request.user)
        
        student.roll_number = request.POST.get('roll_number')
        student.degree = request.POST.get('degree')
        student.branch = request.POST.get('branch')
        student.semester = request.POST.get('semester')
        student.gpa = request.POST.get('gpa')
        student.phone = request.POST.get('phone')
        student.skills = request.POST.get('skills')
        
        if 'profile_picture' in request.FILES:
            student.profile_pic = request.FILES['profile_picture']
        if 'resume' in request.FILES:
            student.resume = request.FILES['resume']
            
        student.save()
        messages.success(request, 'Profile updated successfully..!')
        return redirect('student_profile')
    
    applications = student.applications.all() if student else [] # type: ignore
        
    return render(request, 'internship/student_profile.html', {
        'student': student,
        "applications" : applications
    })
    
# Company List
def company_list(request):
    companies = Company.objects.all()
    return render(request, 'internship/companies.html', {'companies' : companies})

# Company Details
def company_detail(request, pk):
    company = get_object_or_404(Company, pk= pk)
    positions = company.positions.filter(status= 'open') # type: ignore
    return render(request, "internship/company_detail.htl", {
        'company' : company,
        'positions': positions
    })
    

# Authentication Views
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        first_name = request.POST.get('first_name')
        
        if password != confirm_password:
            messages.error(request, "Password do not match")
            return redirect('register')
        
        if User.objects.filter(username= username).exists():
            messages.error(request, "username already exists.")
            return redirect('register')
            
            
        user = User.objects.create_user(
            username= username,
            email= email,
            password= password,
            first_name= first_name
        )
        messages.success(request, 'Registration successful! please login')
        return redirect('login')
    
    return render(request, 'internship/register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username= username, password= password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {User.first_name}')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
            
    return render(request, 'internship/login.html')

def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')
    