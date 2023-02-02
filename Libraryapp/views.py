from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_control, never_cache

from Libraryapp.models import Student, Course, Books, Issue_Book


# Create your views here.

def admin_reg_fun(request):
    return render(request,'adminregister.html',{'data':''})




def admin_regdata_fun(request):
    user_name = request.POST['txtusername']
    user_email = request.POST['txtemail']
    user_pswd = request.POST['txtpawd']
    if User.objects.filter(Q(username=user_name) | Q(email=user_email)).exists():
        return render(request,'adminregister.html',{'data': 'Username,email  already exists'})
    else:
        u1 = User.objects.create_superuser(username=user_name, email=user_email, password=user_pswd)
        u1.save()
        return redirect('log')



def student_reg_fun(request):
    c1=Course.objects.all()
    return render(request,'studentregister.html',{'course':c1})



def student_regdata_fun(request):
        user_name =request.POST['txtname']
        user_phno=request.POST['txtnum']
        if Student.objects.filter(Q(Stud_Name=user_name) & Q(Stud_Phno=user_phno)).exists():
            return render(request,'studentregister.html',{'data':'username and phno is already exists'})
        else:
            s1=Student()
            s1.Stud_Name=request.POST['txtname']
            s1.Stud_Phno=request.POST['txtnum']
            s1.Stud_Sem=request.POST['txtsem']
            s1.Stud_pass=request.POST['txtpawd']
            s1.Stud_Course=Course.objects.get(Course_Name=request.POST['ddlcourse'])
            s1.save()
            return redirect('log')



def adminhome(request):
    return render(request,'adminhome.html')



def log_fun(request):
    return render(request,'login.html')



def logdata_fun(request):
    s1 = Student.objects.get(Stud_Name=request.session['name'])
    user_name = request.POST['txtusername']
    user_pswd = request.POST['txtpawd']
    user1=authenticate(username = user_name,password = user_pswd)
    if user1 is not None:
        if user1.is_superuser:
            return redirect('adminhome')


    elif Student.objects.filter(Q(Stud_Name=user_name) & Q(Stud_pass=user_pswd)).exists():
        request.session['name'] = user_name
        return render(request, 'studenthome.html',{'data':s1})

    else:
        return render(request,'login.html',{'data':'User is not super user'})



def home_fun(request):
    return redirect('adminhome')



def addbook_fun(request):
    c1=Course.objects.all()
    return render(request,'addbook.html',{'data':c1})



def readbookdata_fun(request):
    b1=Books()
    b1.Books_Name=request.POST['txtname']
    b1.Author_Name=request.POST['txtauthor']
    b1.Course_id=Course.objects.get(Course_Name=request.POST['ddlcourse'])
    b1.save()
    return redirect('add')



def displaybook_fun(request):
    b1=Books.objects.all()
    return render(request,'displaybook.html',{'data':b1})



def update_fun(request,id):
    b1=Books.objects.get(id=id)
    course=Course.objects.all()
    if request.method == 'POST':
        b1.Books_Name=request.POST['txtbook']
        b1.Author_Name=request.POST['txtaname']
        b1.Course_id=Course.objects.get(Course_Name=request.POST['ddlcourse'])
        b1.save()
        return redirect('display')
    return render(request,'update.html',{'data':b1,'Course_data':course})



def delete_fun(request,id):
    b1=Books.objects.get(id=id)
    b1.delete()
    return redirect('display')



def log_out_fun(request):
    return redirect('log')



def assign_fun(request):
    c1 = Course.objects.all()
    return render(request,'assignbook.html',{'course':c1})



def assignbook_fun(request):

    c1=Course.objects.all()
    if request.method == 'POST':
        Student_sem=request.POST['txtsem']
        Student_Course=request.POST['ddlcourse']
        s1=Student.objects.filter(Q(Stud_Sem=Student_sem) & Q(Stud_Course=Course.objects.get(Course_Name=Student_Course)))
        b1 = Books.objects.filter(Course_id=Course.objects.get(Course_Name=Student_Course))
        return render(request,'assignbook.html',{'data':s1,'book':b1,'course':c1})
    return render(request,'assignbook.html',{'course':c1})



def assignbookdata_fun(request):

    i1=Issue_Book()
    i1.Stud_Name=Student.objects.get(Stud_Name=request.POST['ddlstudname'])
    i1.Book_Name=Books.objects.get(Books_Name=request.POST['ddlbookname'])
    i1.Start_Date=request.POST['txtsdate']
    i1.End_Date=request.POST['txtedate']
    i1.save()
    return redirect('assign')



def issuebook_fun(request):
    i1=Issue_Book.objects.all()
    return render(request,'issuebook.html',{'data':i1})



def update2_fun(request,id):
    i1=Issue_Book.objects.get(id=id)
    b1=Books.objects.all()
    if request.method =='POST':
        i1.Stud_Name=Student.objects.get(Stud_Name=request.POST['tbsname'])
        i1.Book_Name=Books.objects.get(Books_Name=request.POST['ddlbname'])
        i1.Start_Date=request.POST['tbsdate']
        i1.End_Date=request.POST['tbedate']
        i1.save()
        return redirect('issue')
    return render(request,'update2.html',{'data':i1,'book':b1})



def delete2_fun(request,id):
    i1=Issue_Book.objects.get(id=id)
    i1.delete()
    return redirect('issue')



#student functions


def studenthome(request):
    s1 = Student.objects.get(Stud_Name=request.session['name'])
    return render(request,'studenthome.html',{'data':s1})



def issuebkdet_fun(request):
    b1=Issue_Book.objects.filter(Stud_Name=Student.objects.get(Stud_Name=request.session['name']))
    return render(request,'issuedbkdet.html',{'data':b1 })



def Student_pro(request):
    s1=Student.objects.get(Stud_Name=request.session['name'])
    return render(request,'profile.html',{'data':s1})


def Update_pro(request,id):
    s1=Student.objects.get(id=id)
    if request.method == 'POST':
        s1.Stud_Name =request.POST['txtName']
        s1.Stud_Phno =request.POST['txtPhno']
        s1.Stud_Sem =request.POST['txtSem']
        s1.Stud_pass =request.POST['txtPswd']
        s1.save()
        return redirect('studenprofile')
    return render(request,'updateprofile.html',{'data':s1})


def logoutstd_fun(request):
    return redirect('log')
