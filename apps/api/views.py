from django.shortcuts import render, get_object_or_404
from .models import News, Media



# Create your views here.
def index(request):
    # Bu funksiya 'templates' papkasidagi 'home.html' faylini topadi
    # va uni brauzerga yuboradi.
    return render(request, 'base.html')
    
def report_view(request):
    return render(request, "report.html")




def news_list(request):
    news = News.objects.filter(is_published=True).order_by('-created_at')
    return render(request, 'news/news_list.html', {'news': news})

def news_detail(request, id):
    item = get_object_or_404(News, id=id, is_published=True)
    return render(request, 'news/news_detail.html', {'item': item})


def media_list(request):
    media = Media.objects.filter(is_published=True).order_by('-created_at')
    return render(request, "media_list.html", {"media": media})

def policy(request):
    return render(request, 'policy.html', {
        'policies': [1,2,3,4,5,6,7]
    })



def quality(request):
    return render(request, 'projects/quality.html')

def gender(request):
    return render(request, 'projects/gender.html')

def economic(request):
    return render(request, 'projects/economic.html')

def peace(request):
    return render(request, 'projects/peace.html')

def partnerships(request):
    return render(request, 'projects/partnerships.html')
def industry(request):
    return render(request, 'projects/industry.html')

def statistics_view(request):
    return render(request, "we_have/statistics.html")

def student_engagement_view(request):
    return render(request, "we_have/student_engagement.html")

def student_womens_empowerment(request):
    return render(request, "we_have/womens_empowerment.html")

def sustainable_economy(request):
    return render(request, "we_have/sustainable_economy.html")

def custom_404(request, exception):
    return render(request, '404.html', status=404)

def quality1(request):
    return render(request, "quality/quality1.html")

def quality2(request):
    return render(request, "quality/quality2.html")

def quality3(request):
    return render(request, "quality/quality3.html")

def quality4(request):
    return render(request, "quality/quality4.html")
def quality5(request):
    return render(request, "quality/quality5.html")
def quality6(request):
    return render(request, "quality/quality6.html")
def quality7(request):
    return render(request, "quality/quality7.html")
def quality8(request):
    return render(request, "quality/quality8.html")
def quality9(request):
    return render(request, "quality/quality9.html")
def quality10(request):
    return render(request, "quality/quality10.html")
def quality11(request):
    return render(request, "quality/quality11.html")
def quality12(request):
    return render(request, "quality/quality12.html")
def quality13(request):
    return render(request, "quality/quality13.html")


def gender1(request):
    return render(request, "gender/gender1.html")
def gender2(request):
    return render(request, "gender/gender2.html")
def gender3(request):
    return render(request, "gender/gender3.html")
def gender4(request):
    return render(request, "gender/gender4.html")
def gender5(request):
    return render(request, "gender/gender5.html")

def economic1(request):
    return render(request, "economic/ecanomic1.html")
def economic2(request):
    return render(request, "economic/ecanomic2.html")
def economic3(request):
    return render(request, "economic/ecanomic3.html")


def partnerships1(request):
    return render(request, "partnerships/partnerships1.html")
def partnerships2(request):
    return render(request, "partnerships/partnerships2.html")
def partnerships3(request):
    return render(request, "partnerships/partnerships3.html")
def partnerships4(request):
    return render(request, "partnerships/partnerships4.html")


def place1(request):
    return render(request, "place/place1.html")
def place2(request):
    return render(request, "place/place2.html")


def industry1(request):
    return render(request, "industry/industry1.html")
def industry2(request):
    return render(request, "industry/industry2.html")
def industry3(request):
    return render(request, "industry/industry3.html")