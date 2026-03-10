from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import Student
import json
from django.views.decorators.csrf import csrf_exempt
from .forms import StudentForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

#POST - create student
@csrf_exempt
@login_required
def create_student(request):
    if request.method == "POST":
        data = json.loads(request.body)
        student = Student.objects.create(
            name=data['name'],
            email=data['email'],
            age=data['age']
        )
        return JsonResponse({"message": "Student created"},status=201)
    
def get_students(request):
    students = list(Student.objects.values())
    return JsonResponse(students, safe=False)


#update
@login_required

@csrf_exempt
def update_student(request, id):
    if request.method == "PUT":
        data = json.loads(request.body)
        student = Student.objects.get(id=id)
        student.name = data['name']
        student.age = data['age']
        student.email = data['email']
        student.save()
        return JsonResponse({"message": "Student updated"})
    # delete
@csrf_exempt
def delete_student(request, id):
    if request.method == "DELETE":
        
        student = Student.objects.get(id=id)
        
        student.delete()
        return JsonResponse({"message": "Student deleted"})
    

# forms
@csrf_exempt
@login_required

def students_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_create')
    else:
        form = StudentForm()

    return render(request, 'student_form.html', {'form': form})  


#Read
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students':students})

#update
def update_student(request, id):
    student = Student.objects.get(id=id)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)

    return render(request, 'update.html', {'form': form})        

#Delete
def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('student_list')



# authentication
def register(request):
    form= UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('login')
    else:
        form = UserCreationForm()
        return render(request, 'register.html',{"form":form})
        
def user_login(request):
    if request.method =='POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username= form.cleaned_data.get('username')
            password= form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
    else:form=AuthenticationForm()
    return render(request,'login.html',{'form':form})


def user_logout(request):
    logout(request)
    return redirect('login')


from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')


def staff_page(request):
    if request.user.is_staff:
        return HttpResponse("welcome staff user")
    else:
        return HttpResponse("access denied")
    

    
    
#after create superuser 
@login_required
def admin_page(request):
    if request.user.is_superuser:
        return HttpResponse("welcome Admin")
    else:
        return HttpResponse("only Admin Allowed")
    













    