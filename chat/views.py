from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import datetime,date
from .models import Fchat,Names,Files

def home(request):
    input_msg = request.POST.get('msg')
    uploaded_file = request.FILES.get('file-input')  
    print(request)
    print(request.method)
    print(uploaded_file)
    print(input_msg)
    client_ip = request.META.get('HTTP_X_FORWARDED_FOR')
    if not client_ip:
        client_ip = request.META.get('REMOTE_ADDR')
    
    if uploaded_file:
        new_file = Files()
        new_file.file = uploaded_file  # Assign the uploaded file to new_file.file
        sender_instance = Names.objects.filter(ip=client_ip).last()
        if sender_instance:
            new_file.sender = sender_instance
        else:   
            sender_instance = Names.objects.create(ip=client_ip)
            new_file.sender = sender_instance
        new_file.created = datetime.now()
        new_file.save()
        print(f'The File {uploaded_file.name} is Saved Successfully')
    
    if input_msg:
        if input_msg == 'monsterorderclear':
            Fchat.objects.all().delete()
            print('conversation Cleared')
        else:
            if request.method == "POST":
                new_msg = Fchat()  
                new_msg.message = input_msg 
                sender_instance = Names.objects.filter(ip=client_ip).last()
                print(sender_instance)
                if sender_instance:
                    new_msg.sender = sender_instance
                else:
                    # If the Names instance doesn't exist, create a new one
                    sender_instance = Names.objects.create(ip=client_ip)
                    new_msg.sender = sender_instance
                new_msg.created = datetime.now()
                new_msg.save()
                print(f'The Message {new_msg} is Saved Successfully')
                return redirect('home')

            else:
                return HttpResponse(
                    '''
                    <div style="display: flex;justify-content:center;">
                        <p style="color:red;font-size:1.7em;">You Will Be Banned</p>
                        <p>GET requests are not allowed on this server</p>
                    <div>
                    '''
                )


    return render(
        request,
        'home.html',
        {
            'time': datetime.now(),
            'msg_list': Fchat.objects.all(),
            'file_list': Files.objects.all(),
        }
    )

'''
    new_usr = Names
    new_usr.name = client_ip
'''

def login(request):
    client_ip = request.META.get('HTTP_X_FORWARDED_FOR')
    if not client_ip:
        client_ip = request.META.get('REMOTE_ADDR')
    if request.method == 'POST':
        og_req = request.POST.get('usrname')
        print("Username from request:", og_req)
        lges = f"Client IP: {client_ip}"
        print(lges)
        # Try to create a new Names instance
        new_usr = Names()
        new_usr.ip=client_ip
        new_usr.name=og_req
        try:
            new_usr.save()
            print("New Names instance saved successfully.")
        except Exception as e:
            print("Error saving Names instance:", e)
        
        return redirect('home')  
    return render(
        request,
        'login.html',
    )
