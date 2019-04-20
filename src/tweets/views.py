from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView, CreateView

from .forms import TweetModelForm
from .models import Tweet

# Create your views here.


# Create 

class TweetCreateView(CreateView):    
    form_class = TweetModelForm
    template_name = 'tweets/create_view.html'    
    success_url = "/tweet/create/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TweetCreateView,self).form_valid(form)

# Retrieve

# Update

# Delete

# List / Search

# Retrieve

class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()
    # template_name = "tweets/detail_view.html"

    # def get_object(self):
    #     print(self.kwargs)
    #     pk = self.kwargs.get("pk")
    #     obj = get_object_or_404(Tweet, pk=pk)
    #     # return Tweet.objects.get(id=pk)
    #     return obj
    

class TweetListView(ListView):
    template_name = "tweets/list_view.html"
    queryset = Tweet.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView, self).get_context_data(*args, **kwargs)

        #print(context)
        
        #context["another_list"] = Tweet.objects.all()
        #print(context)
        return context


def tweet_detail_view(request, pk=None): # pk == id
    #obj = Tweet.objects.get(pk=pk) # GET from database
    obj = get_object_or_404(Tweet, pk=pk)
    print(obj)
    context = {
        "object":obj
    }
    return render(request, "tweets/detail_view.html",context)

# Retrieve
# def tweet_list_view(request):    
#     queryset = Tweet.objects.all()
#     print(queryset)
#     for obj in queryset:
#         print(obj.content)
#     context = {
#         "object_list" : queryset
#     }
#     return render(request, "tweets/list_view.html", context)    