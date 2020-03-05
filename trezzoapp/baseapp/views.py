from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.

def index(request):
    return render(request, "index.html")

def service(request):
    return render(request, "service.html")


def about(request):
    return render(request, "about.html")

def contact(request):
    from_addr = 'triadmailbox@gmail.com'
    to_addr = ['raghu.pyr@gmail.com']
    if request.method == "POST":
        fname = request.POST['fname']
        print(fname)
        email = request.POST['email']
        print(email)
        pnumber = request.POST['pnumber']
        print(pnumber)
        messagetxt = request.POST['messagetxt']
        print(messagetxt)
        subject = request.POST['subject']
        print(subject)
        #lsname - request.POST['lsname']
        #print(fname, lsname, email, pnumber, messagetxt)
        send_mail("ContactForm Enquiry: "+subject, messagetxt, from_addr, to_addr)
        return HttpResponseRedirect("")
    return render(request, "contact.html")

def ml(request):
    return render(request, "mlpage.html") 