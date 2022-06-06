from django.shortcuts import render

# Create your views here.

def Index(request):
    return render(request,'index.html')

def IndexDirectLogin(request):
    return render(request,"index-without-login.html")

def Index2(request):
    return render(request,"indexv2.html")

def Index3(request):
    return render(request,"indexv3.html")


def SearchList(request):
    return render(request,"search-listing.html")

def SearchList2(request):
    return render(request,"search-listing-two.html")

def Tutordetail(request):
    return render(request,"tutor-detail.html")

def BlogDetail(request):
    return render(request,"blog-detail-right.html")

def BlogGrid(request):
    return render(request,"blog-grid-right.html")

def HowItWorks(request):
    return render(request,"how-it-work.html")

def Package(request):
    return render(request,"package.html")

def Login(request):
    return render(request,"login.html")

def SignUp(request):
    return render(request,"signup.html")

def Forgot(request):
    return render(request,"lost-password.html")

# -----------Profile Settings------------------

def PersonalDetail(request):
    return render(request,"profile-setting-a.html")

def ContactDetail(request):
    return render(request,"profile-setting-b.html")

def EducationDetail(request):
    return render(request,"profile-setting-c.html")

def SubjectsTeach(request):
    return render(request,"profile-setting-d.html")

def MediaGallary(request):
    return render(request,"profile-setting-e.html")