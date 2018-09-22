from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from useraccounts.models import  Trader, UserAccount, Funds, User
from store.models import Device, Sensor_Post
from django.contrib.auth.decorators import login_required, permission_required
from useraccounts.forms import TraderForm, UserAccountForm
from django.views.decorators.csrf import csrf_exempt
from itertools import chain
from django.db.models import Q
from django.db.models import Sum
from datetime import datetime
import json

# Create your views here.

@login_required
def index(request):
    today = datetime.now()
    print(today)
    posts = Sensor_Post.objects.all()
    devices = Device.objects.all()
    posts_today = Sensor_Post.objects.filter(created_at__date=datetime.date(today))
    print(posts_today)
    return render(request, 'store/index.html', {'posts':posts, 'devices':devices, "posts_today":posts_today})

@csrf_exempt
def iot(request):

    if request.method == 'POST':
        try:
            sensor_data = json.loads(request.body)
            device = Device.objects.get(name = "ard01munshin")
            cleaned_time = sensor_data["time"].replace('"', "") #remove quotation marks
            cleaned_time =cleaned_time.strip() #remove leading and lagging white spaces
            cleaned_time =cleaned_time[:-6] #remove last 6xters being seconds and microseconds
            cleaned_time = datetime.strptime(cleaned_time, '%y/%m/%d,%H:%M')  #convert time format to django compatible 

            new_sensor_data = Sensor_Post(device_id = device.id, co_val = sensor_data["co"], ch4_val = sensor_data["ch4"], aq_val = sensor_data["aq"], 
                                            h_val = sensor_data["h"], sensor_time = cleaned_time)
            new_sensor_data.save()
            return HttpResponse(json.dumps({"status" :"ok", "action":"Post saved"}))

        except:
            return HttpResponse('parameter inconsistency failures')

    return HttpResponse('Unrecognisable request method, cannot understand')



def fetch(request):

    data = Sensor_Post.objects.order_by('-sensor_time')[:200]
    response = []
    for post in data:
        cleaned_time = str(post.sensor_time).replace("datetime.datetime(", "")
        cleaned_time = (cleaned_time).replace(")", "")
        cleaned_time = (cleaned_time)[:-9]
        cleaned_stime = str(post.created_at).replace("datetime.datetime(", "")
        cleaned_stime = (cleaned_stime).replace(")", "")
        cleaned_stime = (cleaned_stime)[:-16]
        new_val = {"time": cleaned_time, "s_time": cleaned_stime, "co": post.co_val, "ch4":post.ch4_val, "aq": post.aq_val,"h": post.h_val}
        response.append(new_val)

    return HttpResponse(json.dumps(response))




# @login_required
# def table(request):
#     traders = Trader.objects.all()
#     total_funds = Funds.objects.aggregate(sum=Sum('amount'))['sum']
#     useraccount = UserAccount.objects.get(user__username = request.user)
        
#     cell_leaders = UserAccount.objects.filter(user__is_superuser = False)


#     return render(request, 'store/table.html', { 'traders':traders, 'total_funds':total_funds, 'cell_leaders': cell_leaders})

# @login_required
# def add_leader(request):

#     form    = UserAccountForm()

#     traders = Trader.objects.all()
#     total_funds = Funds.objects.aggregate(sum=Sum('amount'))['sum']
#     cell_leaders = UserAccount.objects.filter(user__is_superuser = False)


#     if request.method == 'POST':
#         username = (request.POST['username'])
#         lname = (request.POST['last_name'])
#         fname = (request.POST['first_name'])
#         phone = (request.POST['phone'])
#         email = (request.POST['email'])
#         password = (request.POST['password'])
#         cell = (request.POST['cell_name'])
#         dob = (request.POST['dob'])
#         address = (request.POST['address'])
#         is_superuser = (request.POST.get('is_superuser', False))
#         user = User.objects.filter(username = username)

#         if user:
#             error = "Username already exists"
#             return render(request, 'store/add_leader.html', {"error":error, 'form':form, 'traders':traders, 'total_funds':total_funds, 'cell_leaders': cell_leaders})
        
#         new_user = User(first_name = fname, last_name = lname, username = username, email = email, is_superuser = check_value(is_superuser))

#         new_user.save()

#         new_useraccount = UserAccount( dob = format_date(dob), phone = phone, address = address,
#                                         cell = cell, user_id = new_user.id )
#         new_useraccount.save()

#         new_user.set_password(password)


#         if form.is_valid():
#             form.cleaned_data("username")
#             print("-----------------------------")

#     return render(request, 'store/add_leader.html', { 'form':form, 'traders':traders, 'total_funds':total_funds, 'cell_leaders': cell_leaders})

# @login_required
# def add(request):
#     traders = Trader.objects.all()
#     total_funds = Funds.objects.aggregate(sum=Sum('amount'))['sum']
#     cell_leaders = UserAccount.objects.filter(user__is_superuser = False)

#     form    = TraderForm()
#     result  = {}
#     if request.method == 'POST':
#         lname = (request.POST['lname'])
#         fname = (request.POST['fname'])
#         phone = (request.POST['phone'])
#         products = (request.POST['products'])
#         income = ( request.POST['income'])
#         occupation = ( request.POST['occupation'])
#         dob = ( request.POST['dob'])
#         business_date = ( request.POST['business_date'])
#         city = ( request.POST['city'])
#         business_worth = ( request.POST['business_worth'])
#         address = ( request.POST['address'])
#         why_no_spouse = ( request.POST['why_no_spouse'])
#         trade_address = ( request.POST['trade_address'])
#         why_no_spouse = ( request.POST['why_no_spouse'])
#         business_needs = ( request.POST['business_needs'])
#         supplier = ( request.POST['supplier'])
#         cell_name = ( request.POST['cell_name'])
#         num_kids = ( request.POST['num_kids'])
#         fund_needed = ( request.POST['fund_needed'])
#         do_you_save = (request.POST.get('do_you_save', False))
#         have_kids = (request.POST.get('have_kids', False))
#         change_business = (request.POST.get('change_business', False))
#         with_spouse = (request.POST.get('with_spouse', False))
#         cell_lead = User.objects.get(username = "admin")

#         # Attempt to grab information from the raw form information.
#         # Note that we make use of both UserForm and UserProfileForm.

#         if request.user.is_authenticated :

#             new_trader = Trader(lname = lname, fname = fname, phone = phone, products= products,income = income, do_you_save = check_value(do_you_save), 
#                                 have_kids = check_value(have_kids), num_kids = num_kids, occupation = occupation, business_date = format_date(business_date), dob = format_date(dob), city = city, address = address, 
#                                 trade_address = trade_address, business_worth = business_worth, with_spouse = check_value(with_spouse), why_no_spouse = why_no_spouse, 
#                                 business_needs = business_needs, supplier = supplier, change_business = check_value(change_business), fund_needed = fund_needed, 
#                                 cell_name = cell_name, cell_leader_id = cell_lead.id)


#             new_trader.save()
#             print(new_trader)

#         add_traderForm = TraderForm(request.POST)

#     return render(request, 'store/add_trader.html', { 'form':form, 'traders':traders, 'total_funds':total_funds, 'cell_leaders': cell_leaders})


# def format_date(date):
#     "**Change date format for django**"
#     date = date.split("/")

#     return (date[2]+"-"+date[1]+"-"+date[0])


# def check_value(value):
    
#     if value == "on":
#         return True
    
#     else:
#         return value









































# def category(request, slug):
#     cat = Category.objects.all()

#     subcat = SubCategory.objects.all()
#     print(type(cat))

#     products = Product.objects.all()
#     if slug != "all" :
#         products = Product.objects.filter(category__slug = slug)
#         current_category = Category.objects.get(slug = slug)
    
#     elif slug == "all":
#         products = Product.objects.all()
#         current_category = "ALL PRODUCTS"

#     return render(request, 'store/category.html', {"current_category":current_category, 'products': products, 'cat':cat, "subcat":subcat} )

# def subcategory(request, slug):
#     cat = Category.objects.all()

#     subcat = SubCategory.objects.all()
#     print(type(cat))

#     products = Product.objects.all()
#     if slug :
#         products = Product.objects.filter(subcategory__slug = slug)
#         current_category = SubCategory.objects.get(slug = slug)

#     return render(request, 'store/category.html', {"current_category":current_category, 'products': products, 'cat':cat, "subcat":subcat} )

# def single(request, slug):
#     product = Product.objects.get(slug = slug)
#     subcat = SubCategory.objects.all()
#     cat = Category.objects.all()
#     subcat = SubCategory.objects.all()
#     hotproducts = Product.objects.filter(hot = True)

#     hotproducts = Product.objects.filter(hot = True)


#     return render(request, 'store/single.html', { 'product': product, 'cat':cat, "subcat":subcat, "hotproducts":hotproducts} )


# def address(request):
#     forms = CustomersForm()
#     if request.method == "POST":
#         postmail = (request.POST["data"])
#         addresses = Customers.objects.filter(email = postmail)

#         if addresses.exists():
#             print('email exists')
#         else:
#             newmail = Customers(email = postmail)
#             newmail.save()

#     return HttpResponse(("addresses"))

# def checkout(request):
#     subcat = SubCategory.objects.all()
#     cat = Category.objects.all()
#     subcat = SubCategory.objects.all()
#     hotproducts = Product.objects.filter(hot = True)
#     print(request.GET)
#     hotproducts = Product.objects.filter(hot = True)


#     return render(request, 'store/checkout.html', { 'cat':cat, "subcat":subcat, "hotproducts":hotproducts} )

# def search(request):
#     cat = Category.objects.all() #FOR NAV BAR RENDERING AND SIDE OPTIONS RENDERING

#     subcat = SubCategory.objects.all()
#     query = (request.GET["Product"])
#     form    = SearchForm()
#     result  = {}
#     # if request.method == 'POST':
#     # Attempt to grab information from the raw form information.
#     # Note that we make use of both UserForm and UserProfileForm.
#     search_form = SearchForm(data=request.POST)
#     # if search_form.is_valid():
        
#     # query = request.GET['name']
#     # print(query)
    
        
#     try:
#         result = Product.objects.filter( Q(name__icontains = query) | Q(description__icontains = query))
#         # result2 = Product.objects.filter( Q(description__icontains = query))
#         # result = list(chain(result, result2))
#         print("result-----------------------", result)

#         return render(request, 'store/category.html', {"current_category":"RESULTS", 'products': result, 'cat':cat, "subcat":subcat} )

#     except:
#         print("result-----------------------")
#         return render(request, 'store/category.html', {"current_category":"RESULTS", 'products': result, 'cat':cat, "subcat":subcat} )
            
#     return render(request, 'store/category.html', {"current_category":"RESULTS", 'products': result, 'cat':cat, "subcat":subcat} )
