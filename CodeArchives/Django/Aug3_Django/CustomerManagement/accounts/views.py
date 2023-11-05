from django.shortcuts import render,redirect
from .models import Customer, Product,Order
from .forms import OrderForm, RegisterForm, CustomerForm
from .filters import OrderFilter
from .decorators import add_groups
from django.forms import inlineformset_factory
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {
        'form': form
    }
    return render(request, 'accounts/register.html', context=context)

def homepage(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()
    orders_count = orders.count()
    pending = orders.filter(status='Pending').count()
    delivered = orders.filter(status='Delivered').count()
    context = {
        'customers': customers,
        'orders': orders,
        'orders_count': orders_count,
        'pending': pending,
        'delivered': delivered
    }
    return render(request,"accounts/dashboard.html",context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        invalid_flag = 0
        try:
            valid_user = User.objects.get(username=username)
        except Exception as error:
            invalid_flag = 1
            messages.error(request, "Enter a valid user")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print('Valid User')
            login(request, user)
            # print(request.user.groups.all())
            return redirect('homepage')
        else:
            if invalid_flag!=1:
                messages.info(request, 'Username password incorrect')    
    return render(request, 'accounts/login.html')

def logout_user(reqeust):
    logout(reqeust)
    return redirect('login')

def products(request):
    products = Product.objects.all()
    return render(request,"accounts/products.html",{'products': products})

def createCustomer(request):
    form = CustomerForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/create-customer.html', context)

def customers(request,pk):
    customer = Customer.objects.get(id=pk)
    # q = request.GET.get('q')
    # orders = Order.objects.filter(product__name__icontains=q)
    orders = customer.order_set.all()
    orders_count = orders.count()
    orderFilter = OrderFilter(request.GET,queryset=orders)
    orders = orderFilter.qs 
    context = {
        'customer': customer,
        'orders': orders,
        'orders_count': orders_count,
        'orderFilter': orderFilter
    }
    return render(request,"accounts/customers.html",context)    

def CreateOrder(request,pk):
    OrderFormSet = inlineformset_factory(Customer,Order,fields=('product','status'))
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(instance=customer)
    if request.method == 'POST':
        formset = OrderFormSet(request.POST,instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('homepage')
    context = {'formset': formset}
    return render(request,"accounts/order.html",context)

def updateOrder(request,pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        form = OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    form = OrderForm(instance=order)
    context = {'form': form}
    return render(request,"accounts/order.html",context)
    
def deleteOrder(request,pk):
    if request.method == 'POST':    
        order = Order.objects.get(id=pk)
        order.delete()
        return redirect('homepage')
    return render(request,'accounts/delete.html')


