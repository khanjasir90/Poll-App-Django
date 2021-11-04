from typing import Iterator
from django.shortcuts import redirect, render,HttpResponse
from django.db.models import F
from .models import Register,Poll,CheckVote
import re
from datetime import date
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def index(request):
    if request.session['username'] == None:
        return redirect('/login')
    data = Poll.objects.filter(poll_status=True).order_by('-poll_date')
    ndata = Poll.objects.filter(poll_status=False).order_by('-poll_date')
    context = {
        'poll_data' : data,
        'npoll_data':ndata
    }
    return render(request,'index.html',context)

def login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        if username == "" or username == None:
            context={
                'message': 'Username Field Cannot be Empty'
            }
            return render(request,'login.html',context)
        elif password == "" or password == None:
            context= {
                'message' : 'Password Field Cannot be Empty'
            }
            return render(request,'login.html',context)
        else:
            users_name = Register.objects.filter(username=username,password=password)
            print(users_name)
            if users_name.count() != 1:
                context = {
                    'message' : 'Wrong Credentials'
                }
                return render(request,'login.html',context)
            else:
                request.session['username'] = username
                print(request.session['username'])
                return redirect('/')
    return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        username=request.POST.get('userhandle')
        email=request.POST.get('emailid')
        password=request.POST.get('password')
        if username == "" or username == None:
            context={
                'message': 'Username Field Cannot be Empty'
            }
            return render(request,'register.html',context)
        elif email == "" or email == None:
            context={
                'message': 'Email Field cannot be Empty'
            }
            return render(request,'register.html',context)
        elif password == "" or password == None:
            context= {
                'message' : 'Password Field Cannot be Empty'
            }
            return render(request,'register.html',context)
        elif re.fullmatch(r'^(?=.*?[A-Z])(?=(.*[a-z]){1,})(?=(.*[\d]){1,})(?=(.*[\W]){1,})(?!.*\s).{8,}$',password) == None:
            context= {
                'message' : 'Password must contain minimum 8 characters and atleast 1 Uppercase,Lowercase,Digit and Special Character'
            }
            return render(request,'register.html',context)
        else:
            users_name = Register.objects.filter(username=username)
            users_email = Register.objects.filter(email=email)
            if users_name.count() > 0:
                context = {
                    'message' : 'Username Already Exists'
                }
                return render(request,'register.html',context)
            elif users_email.count() > 0:
                context = {
                    'message' : 'Email Already Exists'
                } 
                return render(request,'register.html',context)
            else:
                register = Register(username=username,email=email,password=password)
                register.save()
                return redirect('/login')
    else:
        context = {}
        return render(request,'register.html',context)

def addPoll(request):
    if request.method == 'POST':
        if request.session['username'] == None:
            return redirect('/login')
        topic=request.POST.get('topic')
        choice_one=request.POST.get('choice1')
        choice_two=request.POST.get('choice2')
        choice_three=request.POST.get('choice3')
        choice_four=request.POST.get('choice4')
        poll_date = date.today()
        poll_status = True 

        if topic == "" or choice_one == "" or choice_two == "" or choice_three == "" or choice_four == "":
            context = {
                'message' : 'No Fields should be Empty'
            }
            return render(request,'addPoll.html',context)
        else:
            poll = Poll(username=request.session['username'],topic=topic,choice_one=choice_one,
            choice_two=choice_two,choice_three=choice_three,choice_four=choice_four,
            choice_one_vote=0,choice_two_vote=0,choice_three_vote=0,choice_four_vote=0,
            poll_date=poll_date,poll_status=poll_status)
            poll.save()
            return redirect('/')
    if request.session['username'] == None:
        return redirect('login')
    return render(request,'addPoll.html')

def vote(request,id):
    if request.method == 'POST':
        if request.session['username'] == None:
            return redirect('/login')
        voted_option = request.POST.get('choice')
        print(voted_option)
        data = Poll.objects.get(id=id)
        if(voted_option == "" or voted_option == None):
            context = {
                'message' : 'Please select an option',
                'poll_data' : data
            }
            return render(request,'vote.html',context)
        checkvote_status = CheckVote.objects.filter(topic_id=id).filter(username=request.session['username'])
        print(checkvote_status)
        if checkvote_status.count() > 0:
            context = {
                'message' : 'You have already Voted',
                'poll_data': data
            }
            return render(request,'vote.html',context)
        data = Poll.objects.filter(id=id)
        for poll_data in data.iterator():
            if voted_option == poll_data.choice_one:
                Poll.objects.filter(id=id).update(choice_one_vote = F('choice_one_vote')+1)
                checkvote = CheckVote(username=request.session['username'],topic_id=id)
                checkvote.save()
                return redirect('/')
                break
            if voted_option == poll_data.choice_two:
                Poll.objects.filter(id=id).update(choice_two_vote = F('choice_two_vote')+1)
                checkvote = CheckVote(username=request.session['username'],topic_id=id)
                checkvote.save()
                return redirect('/')
                break
            if voted_option == poll_data.choice_three:
                Poll.objects.filter(id=id).update(choice_three_vote = F('choice_three_vote')+1)
                checkvote = CheckVote(username=request.session['username'],topic_id=id)
                checkvote.save()
                return redirect('/')
                break
            if voted_option == poll_data.choice_four:
                Poll.objects.filter(id=id).update(choice_four_vote = F('choice_four_vote')+1)
                checkvote = CheckVote(username=request.session['username'],topic_id=id)
                checkvote.save()
                return redirect('/')
                break
        return redirect('/')
    else:
        if request.session['username'] == None:
            return redirect('/login')
        data = Poll.objects.get(id=id)
        context={
        'poll_data':data
        }
        return render(request,'vote.html',context)

def profile(request):
    if request.session['username'] == None:
        return redirect('login')
    active_data = Poll.objects.filter(username=request.session['username']).filter(poll_status=True).order_by('-poll_date')
    non_active_data = Poll.objects.filter(username=request.session['username']).filter(poll_status=False).order_by('-poll_date')
    context = {
        'poll_data' : active_data,
        'npoll_data':non_active_data
    }
    return render(request,'profile.html',context)

def endpoll(request,id):
    if request.session['username'] == None:
        return redirect('/login')
    print(id)
    register_data = Register.objects.filter(username=request.session['username'])
    data = Poll.objects.filter(id=id).update(poll_status=False)
    mail_data = Poll.objects.filter(id=id)
    subject="Your Poll has Ended!!!"
    message=""
    for i in mail_data.iterator():
        message = "Hey " + i.username + " thankyou for creating a poll with Pollz!!! \n"+"Below are the  Details and Result of the Poll \n"+"Options : \n "+"1."+i.choice_one+" - "+str(i.choice_one_vote)+"\n 2. "+i.choice_two+" - "+str(i.choice_two_vote)+"\n 3. "+i.choice_three+" - "+str(i.choice_three_vote)+"\n 4. "+i.choice_four+" - "+str(i.choice_four_vote)+"\n Your Sincerly, \n Mohd Jasir Noor Khan \n Founder Pollz" 
    email =""
    for i in register_data.iterator():
        email = i.email
    email_from = settings.EMAIL_HOST_USER
    recipient =[ email,]
    send_mail(subject,message,email_from,recipient)

    return redirect('/profile')

def logout(request):
    if request.session['username'] == None:
        return redirect('/login')
    request.session['username'] = None
    return redirect('/login')


# message='''Hey {mail_data.username} thankyou for creating a Poll with Pollz! \n
#             Below are the Details of Poll \n
#             Topic - {mail_data.topic} \n
#             Options : 
#             1. {{mail_data.choic_one}} - {{mail_data.choice_one_vote}}\n
#             2. {{mail_data.choic_two}} - {{mail_data.choice_two_vote}} \n
#             3. {{mail_data.choic_three}} - {{mail_data.choice_three_vote}} \n
#             4. {{mail_data.choic_four}} - {{mail_data.choice_four_vote}}\n
#             \n
#             Your Sincerely,
#             Mohd Jasir Khan
#             Founder of Pollz
#             '''