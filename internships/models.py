from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Company(models.Model):
    """ company Fields = [ name, email, website, location, description, created_at ] """
    
    name =  models.CharField( max_length=200, unique=True )
    email = models.EmailField()
    website = models.URLField( null=True, blank=True )
    location = models.CharField( max_length=200 )
    description =  models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Companies"
        
    def __str__(self) -> str:
        return self.name
    

class Student(models.Model):
    """ Student Field = [user, roll_number, degree(in choice), branch, semester, gpa, phone, resume, profile_pic, skills, created_at ] """
    DEGREE_CHOICE = [
        ('btech', 'Bachelor of Technology'),
        ('bsc-it', 'Bachelor of Science(IT)'),
        ('bca', 'Bachelor of Computer Application'),
        ('mtech', 'Master of Technology'),
        ('mca', 'Master of Computer Application'),
    ]
    
    
    user =  models.OneToOneField( User, on_delete=models.CASCADE )
    roll_number =  models.CharField( max_length=200, unique=True )
    degree = models.CharField( max_length=20, choices=DEGREE_CHOICE )
    branch = models.CharField( max_length=200 )
    semester = models.IntegerField( max_length=8, null=False)
    gpa  = models.DecimalField(max_digits=3, decimal_places=2 )
    phone = models.CharField( max_length=15 )
    
    resume = models.FileField(
        upload_to= 'resume/',
        null=True,
        blank=True
    )
    
    profile_pic = models.ImageField(
        upload_to='profile_pictures/',
        null=True,
        blank=True
    )
    
    skills = models.TextField(
        help_text= "Coma-separated list of skills (e.g. Python, Java, PHP)"
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['roll_number']
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    
class InternshipPosition(models.Model):
    """ IN_PO Fields = [ tittle, company, description, requirement, duration_weeks, stipend, location, status(choice), start_date, end_date, posted_on, update_on ] """
    
    title = models.CharField( max_length=200 )
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='positions'
    )
    
    description =  models.TextField()
    requirement = models.TextField()
    duration_weeks = models.IntegerField()
    stipend = models.DecimalField( 
        max_digits=10,
        decimal_places=2,
        null=True, 
        blank=True 
    )
    
    location = models.CharField( max_length=200 )
    
    STATUS_CODE = [
        ('open', 'OPEN'),
        ('closed', 'CLOSED'),
        ('filled', 'FILLED'),
    ]
    
    status = models.CharField(
        max_length=15,
        choices=STATUS_CODE,
        default='open'
    )
     
    start_date = models.DateField()
    end_date = models.DateField()
    
    posted_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-posted_on']
    
    def __str__(self) -> str:
        return f'{self.title} at {self.company}'
    
class Application(models.Model):
    ''' 
    Application Field = [ student, position, status(choice), cover_letter, resume, applied_on ]
    '''
    
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name='applications'
    )
    
    position = models.ForeignKey(
        InternshipPosition, on_delete=models.CASCADE, related_name='application'
    )
    
    STATUS_CHOICE = [
        ('applied', 'Applied'),
        ('under_review', 'Under Review'),
        ('shortlisted', 'Shortlisted'),
        ('rejected', 'Rejected'),
        ('accepted', 'Accepted'),
    ]
    
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICE,
        default='applied'
    )
    
    cover_letter = models.TextField()
    
    resume = models.FileField(
        upload_to='application/', 
    )
    
    applied_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = [ 'student', 'position']
        ordering = ['-applied_on']
        
    def __str__(self) -> str:
        return f"{self.student} applied for {self.position.title}"
    
