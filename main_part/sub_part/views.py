from django.shortcuts import render,redirect
from . models import indexregister,contacts,addcourse,allstudents,category,feedback,packagecreate,alladminuser,allinstructor,zoommeet
import easygui
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as adminlog
from django.contrib.auth import logout as instruclog
from django.conf import settings
from django.core.mail import send_mail



# Create your views here.
       
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html') 


def addnewcourse(request):
    return render(request,'addnewcourse.html')

def adminregi(request):
    return render(request,'adminregi.html')


def all_student_instructor(request):
    ex3=allstudents.objects.all()
    context={'ex3':ex3}
    return render(request,'all_student_instructor.html',context)


def all_admin(request):
    ex8=alladminuser.objects.all()
    context={'ex8':ex8}
    return render(request,'all_admin.html',context)

def blog(request):
    return render(request,'blog.html')


def admin_user_create(request):
    return render(request,'admin_user_create.html')


def all_categories(request):
    ex5=category.objects.all()
    context={'ex5':ex5}
    return render(request,'all_categories.html',context)

def contact(request):
    return render(request,'contact.html')


def category_create(request):
    return render(request,'category_create.html')


def coursecomment(request):
    ex12=feedback.objects.all()
    context={'ex12':ex12}
    return render(request,'coursecomment.html',context)

def courses(request):
    return render(request,'courses.html')


def courseview(request):
    ex11=addcourse.objects.all()
    context={'ex11':ex11}
    return render(request,'courseview.html',context)


def instructor_pack(request):
    ex6=packagecreate.objects.all()
    context={'ex6':ex6}
    return render(request,'instructor_pack.html',context)


def package_create(request):
    return render(request,'package_create.html')

def events(request):
    return render(request,'events.html')


def home(request):
    return render(request,'home.html')


def all_student_admin(request):
    ex3=allstudents.objects.all()
    context={'ex3':ex3}
    return render(request,'all_student_admin.html',context)

@login_required(login_url='instruclogin')
def index2(request):
    return render(request,'index2.html')
    
@login_required(login_url='adminlogin')
def index3(request):
    return render(request,'index3.html')

def instruclogin(request):
    if request.method=='POST':
        if allinstructor.objects.filter(Username=request.POST['Username'],password=request.POST['password']).exists():
            ex9=allinstructor.objects.get(Username=request.POST['Username'],password=request.POST['password'])
            easygui.msgbox('Logged succesfully..!!')
            return render(request,'index2.html',{'ex9':ex9})
        else:
            context={'msg':'Please enter vali Email and Password'}
            return render(request,'instruclogin.html',context)
    return render(request,'instruclogin.html')

def instructreg(request):
    return render(request,'instructreg.html')


def message(request):
    ex2=contacts.objects.all()
    context={'ex2':ex2}
    return render(request,'message.html',context)


def quiz(request):
    return render(request,'quiz.html')

def studentreg(request):
    return render(request,'studentreg.html')


def all_instructor(request):
    ex9=allinstructor.objects.all()
    context={'ex9':ex9}
    return render(request,'all_instructor.html',context)

def shop(request):
    return render(request,'shop.html')


def all_courses(request):
    ex11=addcourse.objects.all()
    context={'ex11':ex11}
    return render(request,'all_courses.html',context)

def teachers(request):
    return render(request,'teachers.html')

def zoom(request):
    return render(request,'zoom.html')

def forgetpass_admin(request):
    return render(request,'forgetpass_admin.html')

def forgetpass_instructor(request):
    return render(request,'forgetpass_instructor.html')

def forgetpass_student(request):
    return render(request,'forgetpass_student.html')

#index page
def indexreg(request):
    if request.method=='POST':
        ex1=indexregister(name=request.POST['name'],
                 mail_id=request.POST['mail_id'],
                 phone_number=request.POST['phone_number'],
                )
        ex1.save()
        subject = 'Welcome to MASTERIO LEARNING '
        message = 'The capacity to learn is a gift;The ability to learn is a skill;The willingness to learn is a choice..! Hope you enjoy with our learning system and  technologies..! '
        email_from = settings.EMAIL_HOST_USER
        recepient = request.POST.get('mail_id')
        print("check:",recepient)
        send_mail(subject, 
            message, email_from, [recepient], fail_silently = False)
        easygui.msgbox('your response saved succesfully..!!')
        return redirect(studentlogin)
    return render(request,'indexreg.html')
def contactreg(request):
    if request.method=='POST':
        ex2=contacts(your_name=request.POST['your_name'],
                    email=request.POST['email'],
                    phone_number=request.POST['phone_number'],
                    messege=request.POST['messege']
                )
        ex2.save()
        subject = 'Welcome to MASTERIO LEARNING '
        message = 'Thank you for the response..!!'
        email_from = settings.EMAIL_HOST_USER
        recepient = request.POST.get('email')
        print("check:",recepient)
        send_mail(subject, 
            message, email_from, [recepient], fail_silently = False)
        easygui.msgbox('your response saved succesfully..!!')
        return redirect(contact)
    return render(request,'contactreg.html')

def teachersreg(request):
    if request.method=='POST':
        ex12=feedback(Course_Name=request.POST['Course_Name'],
                      Message=request.POST['Message'],
                      datetime=request.POST['datetime']
                       )
        ex12.save()
        easygui.msgbox('your feedback sent successfully..!!')
        return redirect(teachers)
    return render(request,'teachersreg.html') 
def commentsdelete(request,id):
    ex12=feedback.objects.get(id=id)
    ex12.delete()
    easygui.msgbox("your data has been deleted successfully")
    return redirect(message)              

def messagedelete(request,id):
    ex2=contacts.objects.get(id=id)
    ex2.delete()
    easygui.msgbox("your data has been deleted successfully")
    return redirect(message) 
# for student 
def stureg(request):
    if request.method=='POST':
        if allstudents.objects.filter(Username=request.POST['Username']):
            easygui.msgbox("This Username has already taken")
        elif  allstudents.objects.filter(Mail_id=request.POST['Mail_id']):
            easygui.msgbox("This Mail_id has already taken")
        else:
            ex3=allstudents(Username=request.POST['Username'],
                        First_name=request.POST['First_name'],
                        Last_name=request.POST['Last_name'],
                        Mail_id=request.POST['Mail_id'],
                        password=request.POST['password']
                 
                )
            ex3.save()
            subject = 'Welcome to MASTERIO LEARNING '
            message = 'The capacity to learn is a gift;The ability to learn is a skill;The willingness to learn is a choice..! Hope you enjoy with our learning system and  technologies..! '
            email_from = settings.EMAIL_HOST_USER
            recepient = request.POST.get('Mail_id')
            print("check:",recepient)
            send_mail(subject, 
                message, email_from, [recepient], fail_silently = False)
            easygui.msgbox('your response saved succesfully..!!')
            return redirect(studentlogin)
    return render(request,'studentreg.html')
def studentlogin(request):
    if request.method=='POST':
        if allstudents.objects.filter(Username=request.POST['Username'],password=request.POST['password']).exists():
            ex3=allstudents.objects.get(Username=request.POST['Username'],password=request.POST['password'])
            easygui.msgbox('Logged succesfully..!!')
            return render(request,'index.html',{'ex3':ex3})
        else:
            context={'msg':'Please enter valid Username and Password'}
            return render(request,'studentlogin.html',context)
    return render(request,'studentlogin.html') 

def forgetpass_stureg(request):
    if request.method=='POST':
        ex3=allstudents(Username=request.POST['Username'],
                        First_name=request.POST['First_name'],
                        Last_name=request.POST['Last_name'],
                        Mail_id=request.POST['Mail_id'],
                        password=request.POST['password']
                 
                )
        ex3.save()
        subject = 'Welcome to MASTERIO LEARNING '
        message = 'Your password changed successfully!!'
        email_from = settings.EMAIL_HOST_USER
        recepient = request.POST.get('Mail_id')
        print("check:",recepient)
        send_mail(subject, 
            message, email_from, [recepient], fail_silently = False)
        easygui.msgbox('your response saved succesfully..!!')
        return redirect(studentlogin)
    return render(request,'forgetpass_stureg.html')

def student_edit(request,id):
    ex3=allstudents.objects.get(id=id)
    return render(request,'student_edit.html',{'ex3':ex3})
def stuupdate(request,id):
    ex3=allstudents(id=id,Username=request.POST['Username'],
                 First_name=request.POST['First_name'],
                 Last_name=request.POST['Last_name'],
                 Mail_id=request.POST['Mail_id'],
                 password=request.POST['password'])
    ex3.save()
    easygui.msgbox("your data has been updated successfully")
    return redirect(all_student_admin)

def studelete(request,id):
    ex3=allstudents.objects.get(id=id)
    ex3.delete()
    easygui.msgbox("your data has been deleted successfully")
    return redirect(all_student_admin)


def student_edit_instructor(request,id):
    ex3=allstudents.objects.get(id=id)
    return render(request,'student_edit.html',{'ex3':ex3})
def stuupdatinstructor(request,id):
    ex3=allstudents(id=id,Username=request.POST['Username'],
                 First_name=request.POST['First_name'],
                 Last_name=request.POST['Last_name'],
                 Mail_id=request.POST['Mail_id'],
                 password=request.POST['password'])
    ex3.save()
    easygui.msgbox("your data has been updated successfully")
    return redirect(all_student_instructor)

def studeleteinstructor(request,id):
    ex3=allstudents.objects.get(id=id)
    ex3.delete()
    easygui.msgbox("your data has been deleted successfully")
    return redirect(all_student_instructor)


#admin dashboard
def adminlogin(request):
    if request.method=='POST':
        if alladminuser.objects.filter(Username=request.POST['Username'],password=request.POST['password']).exists():
            ex8=alladminuser.objects.get(Username=request.POST['Username'],password=request.POST['password'])
            easygui.msgbox('Logged succesfully..!!')
            return render(request,'index3.html',{'ex8':ex8})
        else:
            context={'msg':'Please enter valid username and Password'}
            return render(request,'adminlogin.html',context)
    return render(request,'adminlogin.html')
def adminreg(request):
    if request.method=='POST':
        if alladminuser.objects.filter(Username=request.POST['Username']):
            easygui.msgbox("This Username has already taken")
        elif  alladminuser.objects.filter(Mail_id=request.POST['Mail_id']):
            easygui.msgbox("This Mail_id has already taken")
        else:
            ex8=alladminuser(Username=request.POST['Username'],
                 First_name=request.POST['First_name'],
                 Last_name=request.POST['Last_name'],
                 Mail_id=request.POST['Mail_id'],
                 password=request.POST['password']
                 
                )
            ex8.save()
            subject = 'Welcome to MASTERIO LEARNING '
            message = 'The capacity to lead is a gift;The ability to lead is a skill;The willingness to lead is a choice..! Hope you enjoy your duty..!'
            email_from = settings.EMAIL_HOST_USER
            recepient = request.POST.get('Mail_id')
            print("check:",recepient)
            send_mail(subject, 
                message, email_from, [recepient], fail_silently = False)
            easygui.msgbox('your response saved succesfully..!!')
            return redirect(adminlogin)
    return render(request,'adminregi.html')

def forgetpass_adminreg(request):
    if request.method=='POST':
        ex8=alladminuser(Username=request.POST['Username'],
                 First_name=request.POST['First_name'],
                 Last_name=request.POST['Last_name'],
                 Mail_id=request.POST['Mail_id'],
                 password=request.POST['password']
                 
                )
        ex8.save()
        subject = 'Welcome to MASTERIO LEARNING '
        message = 'Your password changed successfully!!'
        email_from = settings.EMAIL_HOST_USER
        recepient = request.POST.get('Mail_id')
        print("check:",recepient)
        send_mail(subject, 
            message, email_from, [recepient], fail_silently = False)
        easygui.msgbox('your response saved succesfully..!!')
        return redirect(adminlogin)
    return render(request,'forgetpass_adminreg.html')


def admin_user_createreg(request):
     if request.method=='POST':
        ex8=alladminuser(Username=request.POST['Username'],
                 First_name=request.POST['First_name'],
                 Last_name=request.POST['Last_name'],
                 Mail_id=request.POST['Mail_id'],
                 password=request.POST['password']
                 
                )
        ex8.save()
        easygui.msgbox('your response saved succesfully..!!')
        return redirect(all_admin)
     return render(request,'admin_user_createreg.html') 

 
def admin_my_profile(request,id):
    ex8=alladminuser.objects.get(id=id)
    return render(request,'admin_my_profile.html',{'ex8':ex8})
def adminupdate(request,id):
    ex8=alladminuser(id=id,Username=request.POST['Username'],
                 First_name=request.POST['First_name'],
                 Last_name=request.POST['Last_name'],
                 Mail_id=request.POST['Mail_id'],
                 password=request.POST['password'])
    ex8.save()
    easygui.msgbox("your data has been updated successfully")
    return redirect(all_admin)

def admindelete(request,id):
    ex8=alladminuser.objects.get(id=id)
    ex8.delete()
    easygui.msgbox("your data has been deleted successfully")
    return redirect(all_admin)
    
    

def packagecreatereg(request):
    if request.method == 'POST':
        ex6=packagecreate()
        ex6.Enter_Price=request.POST.get('Enter_Price')
        ex6.Commission=request.POST.get('Commission')
        
        if len(request.FILES) != 0:
            ex6.image=request.FILES['image']
        
        ex6.save()
        easygui.msgbox('data saved succesfully..!!')
        return redirect(instructor_pack)  
    return render(request,'packagecreatereg.html')


def package_create_edit(request,id):
    ex6=packagecreate.objects.get(id=id)
    return render(request,'package_create_edit.html',{'ex6':ex6})
def packageupdate(request,id):
    ex6=packagecreate(id=id,Enter_Price=request.POST['Enter_Price'],
                 Commission=request.POST['Commission'],
                 image=request.POST['image']
                 )
    ex6.save()
    easygui.msgbox("your data has been updated successfully")
    return redirect(instructor_pack)

def packagedelete(request,id):
    ex6=packagecreate.objects.get(id=id)
    ex6.delete()
    easygui.msgbox("your data has been deleted successfully")
    return redirect(instructor_pack)

def categorycreatereg(request):
    if request.method == 'POST':
        ex5=category()
        ex5.category_name=request.POST.get('category_name')
        ex5.Parent_Category=request.POST.get('Parent_Category')
        
        if len(request.FILES) != 0:
            ex5.image=request.FILES['image']
       
        ex5.save()
        easygui.msgbox('data saved succesfully..!!')
        return redirect(all_categories)


def category_edit(request,id):
    ex5=category.objects.get(id=id)
    return render(request,'category_edit.html',{'ex5':ex5})
def categoryupdate(request,id):
    ex5=category(id=id,Enter_Price=request.POST['Enter_Price'],
                 Parent_Category=request.POST['Parent_Category'],
                 image=request.POST['image']
                 )
    ex5.save()
    easygui.msgbox("your data has been updated successfully")
    return redirect(all_categories)

def categorydelete(request,id):
    ex5=category.objects.get(id=id)
    ex5.delete()
    easygui.msgbox("your data has been deleted successfully")
    return redirect(all_categories)

# instructor page
def instructoreg(request):
    if request.method=='POST':
        if allinstructor.objects.filter(Username=request.POST['Username']):
            easygui.msgbox("This Username has already taken")
        elif  allinstructor.objects.filter(Mail_id=request.POST['Mail_id']):
            easygui.msgbox("This Mail_id has already taken")
        else:
            ex9=allinstructor(Username=request.POST['Username'],
                 First_name=request.POST['First_name'],
                 Last_name=request.POST['Last_name'],
                 Mail_id=request.POST['Mail_id'],
                 password=request.POST['password']
                )
            ex9.save()
            subject = 'Welcome to MASTERIO LEARNING '
            message = 'The capacity to teach is a gift;The ability to teach is a skill;The willingness to teach is a choice..! Hope you enjoy your duty..!'
            email_from = settings.EMAIL_HOST_USER
            recepient = request.POST.get('Mail_id')
            print("check:",recepient)
            send_mail(subject, 
                message, email_from, [recepient], fail_silently = False)
            easygui.msgbox('your response saved succesfully..!!')
            return redirect(instruclogin)
    return render(request,'instructreg.html')
def forgetpass_insreg(request):
    if request.method=='POST':
        ex9=allinstructor(Username=request.POST['Username'],
                 First_name=request.POST['First_name'],
                 Last_name=request.POST['Last_name'],
                 Mail_id=request.POST['Mail_id'],
                 password=request.POST['password']
                 
                )
        ex9.save()
        subject = 'Welcome to MASTERIO LEARNING '
        message = 'Your password changed successfully!!'
        email_from = settings.EMAIL_HOST_USER
        recepient = request.POST.get('Mail_id')
        print("check:",recepient)
        send_mail(subject, 
            message, email_from, [recepient], fail_silently = False)
        easygui.msgbox('your response saved succesfully..!!')
        return redirect(instruclogin)
    return render(request,'forgetpass_insreg.html')

def instructor_edit(request,id):
    ex9=allinstructor.objects.get(id=id)
    return render(request,'instructor_edit.html',{'ex9':ex9})
def instructupdate(request,id):
    ex9=allinstructor(id=id,Username=request.POST['Username'],
                 First_name=request.POST['First_name'],
                 Last_name=request.POST['Last_name'],
                 Mail_id=request.POST['Mail_id'],
                 password=request.POST['password'])
    ex9.save()
    easygui.msgbox("your data has been updated successfully")
    return redirect(all_instructor)

def instrucdelete(request,id):
    ex9=allinstructor.objects.get(id=id)
    ex9.delete()
    easygui.msgbox("your data has been deleted successfully")
    return redirect(all_instructor)

def zoomreg(request):
     if request.method=='POST':
        ex10=zoommeet(Password=request.POST['Password'],
                 token=request.POST['token'])
        ex10.save()
        easygui.msgbox('your response saved succesfully..!!')
        return redirect(zoom)
     return render(request,'zoomreg.html')

def addnewcoursereg(request):
     if request.method=='POST':
        ex11=addcourse()
        ex11.course_title=request.POST.get('course_title')
        ex11.slug=request.POST.get('slug')
        ex11.course_level=request.POST.get('course_level')
        ex11.short_description=request.POST.get('short_description')
        ex11.overview_url=request.POST.get('overview_url')
        ex11.provider=request.POST.get('provider')
        ex11.requirements=request.POST.get('requirements')
        ex11.outcome=request.POST.get('outcome')
        ex11.tags=request.POST.get('tags')
        ex11.free_course=request.POST.get('free_course')
        ex11.price=request.POST.get('price')
        ex11.discount=request.POST.get('discount')
        ex11.language=request.POST.get('language')
        ex11.meta_title=request.POST.get('meta_title')
        ex11.meta_description=request.POST.get('meta_description')
        ex11.Category=request.POST.get('Category')

        if len(request.FILES) != 0:
            ex11.image=request.FILES['image']
        
        ex11.save()
        easygui.msgbox('your response saved succesfully..!!')
        return redirect(courseview)


def courseview_edit(request,id):
    ex11=addcourse.objects.get(id=id)
    return render(request,'courseview_edit.html',{'ex11':ex11})
def courseviewupdate(request,id):
    ex11=addcourse(id=id,course_title=request.POST['course_title'],
                    slug=request.POST['slug'],
                    course_level=request.POST['course_level'],
                    short_description=request.POST['short_description'],
                    image=request.POST['image'],
                    overview_url=request.POST['overview_url'],
                    provider=request.POST['provider'],
                    requirements=request.POST['requirements'],
                    outcome=request.POST['outcome'],
                    tags=request.POST['tags'],
                    free_course=request.POST['free_course'],
                    price=request.POST['price'],
                    discount=request.POST['discount'],
                    language=request.POST['language'],
                    meta_title=request.POST['meta_title'],
                    meta_description=request.POST['meta_description'],
                    Category=request.POST['Category'])
    ex11.save()
    easygui.msgbox("your data has been updated successfully")
    return redirect(courseview)

def courseviewdelete(request,id):
    ex11=addcourse.objects.get(id=id)
    ex11.delete()
    easygui.msgbox("your data has been deleted successfully")
    return redirect(courseview)

#logout
def logout(request):
    adminlog(request)
    easygui.msgbox(" you are logged out!!")
    return render(request,'adminlogin.html')
def logout(request):
    instruclog(request)
    easygui.msgbox(" you are logged out!!")
    return render(request,'instruclogin.html')

