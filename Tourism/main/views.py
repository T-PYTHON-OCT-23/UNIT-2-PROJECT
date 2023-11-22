from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
# Create your views here.

# Done
def home_page_views(request:HttpRequest):
    contant = [{
        "title":"skaka",
        "paragraph":"Sakakah is an oasis town on an ancient caravan route across the Arabian peninsula.",
        "image":"{% static 'images/city/skaka/tapline.jpg' %}",
    },{
        "title":"arar",
        "paragraph":"Arar is located in northern Saudi Arabia near the Iraqi border. It is known for its fertile pasture lands",
        "image":"{% static 'images/city/arar/tapline.jpg' %}",
    },{
        "title":"tabuk",
        "paragraph":"The region is rich in antiquities and archaeological sites such as petroglyphs, inscriptions, forts, palaces, walls",
        "image":"{% static 'images/city/tbook/tabuk.jpg' %}",
    },{
        "title":"rafha",
        "paragraph":"Rafha is a town in the north of Saudi Arabia, close to the border with Iraq.",
        "image":"{% static 'images/city/rafha/tapline.jpg' %}",
    }]

    return render(request,'main/base.html',{'contants': contant})

# Done
def rafha_city_views(request:HttpRequest):
    contant = [{
        "title":"Linah",
        "paragraph":"Linah is a village north of Najd in the Kingdom of Saudi Arabia. It is considered one of the oldest settlements in the Arabian Peninsula, and one of the homes of the Zubaydah Trail, which was taken by the Iraqi pilgrim.",
        "image":"/static/images/city/rafha/linah.jpeg",
    },{
        "title":"Zbala",
        "paragraph":"The historic village of Zabala is considered one of the villages rich in antiquities, the most notable of which are the well, which takes a square shape and is carved in a distinctive way, and the ancient palace, of which only its walls and shoulders remain now, and the residential city surrounding it.",
        "image":"/static/images/city/rafha/zbala.jpg",
    }]

    return render(request,'main/rafha.html',{'contants': contant})

# Done
def tabuk_city_views(request:HttpRequest):
    contant = [{
        "title":"Tabuk Castle",
        "paragraph":"Tabuk Castle is one of the oldest landmarks that you can visit and that attracts large numbers of tourists. It was one of the most important fortresses of the Emirate of Tabuk against any external aggression. It has been converted into a museum that displays the historical events of the city of Tabuk and the conquests of our Prophet Muhammad, may God bless him and grant him peace, and the victories that were accomplished in it.",
        "image":"/static/images/city/tabuk/Tabuk-Museum.jpg",
    },{
        "title":"Mount Almond ",
        "paragraph":"Mount Al-Lour is considered one of the best places in Tabuk, which shows its charming nature. It occupies the first place in terms of height in the Tabuk region of Saudi Arabia, with a height of about 2549 meters. It was given this name due to the spread of almond trees in it, where they are covered with snow during the winter in a wonderful view.",
        "image":"/static/images/city/tabuk/Mount-Almond.jpg",
    },{
        "title":"Traces of the people of Shuaib",
        "paragraph":"If you are looking for the most important tourist attractions in Tabuk, Mada’in Shuaib will make you feel amazed when you visit it due to the elaborate engineering design with which it was built. It was carved into the mountain slopes in reverse to avoid the entry of rainwater or floods. It is also called the Al-Bidaa Monuments Area.",
        "image":"/static/images/city/tabuk/Tourism-in-Tabuk-5.webp",
    }]

    return render(request, 'main/tabuk.html',{'contants': contant})

# Done
def skaka_city_views(request:HttpRequest):
    contant = [{
        "title":"Zabaal Castle",
        "paragraph":"It is considered one of the most wonderful tourist places in Sakaka, Saudi Arabia, as it is considered one of the most important ancient fortresses protecting the city of Sakaka Al-Jawf. It is built on the highest point in the city. It was built of clay and stones, and its inception dates back more than 200 years. It was also considered the main source of water that nourishes... The city of Sakaka is located above a well filled with fresh groundwater",
        "image":"/static/images/city/skaka/Zabaal-Castle.jpg",
    },{
        "title":"Sisra Well",
        "paragraph":"One of the most famous landmarks of Al-Jawf is the Saudi Sakaka, which is named after the leader Sisera, who fought the Jews in the State of Palestine. It is an oval-shaped well that was carved in the sand rocks, and its depth reaches about 15 meters underground, and it is considered an ancient irrigation method as it is found in it. An internal canal was dug into the surrounding rocks to transport fresh water to various fields and farms.",
        "image":"/static/images/city/skaka/Sisra-Well.jpg",
    },{
        "title":"Palace Kadeer",
        "paragraph":"It is considered one of the oldest historical monuments located south of the Saudi city of Sakaka. Its length is about seven meters, and it was built from a group of sandstones of irregular shape and size bound together by clay. This palace contains two large towers through which the village was defended and any External aggression. This palace is distinguished by the presence of some large rocks that contain many ancient inscriptions and decorations.",
        "image":"/static/images/city/skaka/Palace-Kadeer.jpg",
    },{
        "title":"Columns of rodjail",
        "paragraph":"It is considered one of the most amazing tourist attractions in the city of Sakaka Al-Jawf, as it consists of rock columns built at different angles to appear in a slanted form, and its length reaches more than three meters.",
        "image":"/static/images/city/skaka/Columns-of-rodjail.jpg",
    }]

    return render(request, 'main/skaka.html',{'contants': contant})

# Done
def arar_city_views(request:HttpRequest):
    contant = [{
        "title":"Northern Border Museum",
        "paragraph":"This museum is considered one of the greatest tourist attractions in Arar, located on the northern border of the city of Arar. This museum carries many ancient heritage features, so it is called the Slave Museum. Therefore, the museum combines ancient historical monuments and cultural monuments as well. The museum is also distinguished by its large area and is divided into Many halls carry heritage.",
        "image":"/static/images/city/arar/NorthernBorderMuseum.jpg",
    },{
        "title":"Wadi Maailah Area",
        "paragraph":"The Wadi Ma'ila area includes many tourist attractions in the picturesque natural area of Arar. This area is located near the city of Arar, which is only 8 kilometers away from it. This valley area is also characterized by a large area that increases the splendor of the place and also provides an aspect of enjoyment, as the area of ​​the area is About 2 square kilometers, which increases the valley's attractiveness.",
        "image":"/static/images/city/arar/Wadi-Maailah-area.jpg",
    },{
        "title":"The old Emirate palace in Arar",
        "paragraph":"The old Emirate Palace expresses the ancient civilization in the Kingdom of Saudi Arabia. This palace was built by order of King Saud bin Abdulaziz Al Saud, as this palace served as a place that carries the meaning of stability in Arar for the prince who rules the city of Arar.",
        "image":"/static/images/city/arar/The-old-emirate-palace-in-Arar.png/",
    },{
        "title":"Al_Uaisi Natural Area",
        "paragraph":"Al-Owaisi Natural Area is one of the most famous tourist attractions in Arar, located near Arar. This area is 16 kilometers away from the city of Arar. This area is characterized by the presence of many natural landmarks such as gardens and natural flowers that increase the joy and vitality of the area.",
        "image":"/static/images/city/arar/Al_Uaisi-Natural-Area.jpg",
    }]
    return render(request, 'main/arar.html', {'contants': contant})


def dark_mode_views(request:HttpRequest):
    responce = redirect('main:home_page_views')
    responce.set_cookie("mode","dark")
    
    return responce

def light_mode_views(request:HttpRequest):
    responce = redirect('main:home_page_views')
    responce.set_cookie("mode","light")

    return responce
