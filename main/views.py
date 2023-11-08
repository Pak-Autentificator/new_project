from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import Post
from django.views.generic import ListView

from django.views.generic import DetailView
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required



from .forms import OrderForm

def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()  # Сохранение данных заказа в базе данных
            return redirect('admin:main', app_label='main')  # Перенаправление пользователя в админку
    else:
        form = OrderForm()
    return render(request, 'main/order_checkout.html', {'form': form})


#-----------------------------------------------------------------------------------------

def index(request):
    new_post = Post.objects.all()
    return render(request, 'main/index.html', {'new_post': new_post})

class PostDetailView(DetailView):
    model = Post
    template_name = 'main/sell.html'
    context_object_name = 'post'

#-----------------------------------------------------------------------------------------

def cart_view(request):
    return render(request, 'main/cart.html')

#-----------------------------------------------------------------------------------------

from django.shortcuts import render

def order_checkout(request):
    # Получите информацию о товаре, например, используя переданный идентификатор товара
    product_id = request.GET.get('product_id')
    product = Post.objects.get(id=product_id)

    context = {
        'product': product,
    }

    return render(request, 'main/order_checkout.html', context)


#-----------------------------------------------------------------------------------------


class Search(ListView):
    template_name = 'main/base.html'
    context_object_name = 'post'
    paginate_by = 5

    def get_queryset(self):
        return Post.object.filter(title_icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context
