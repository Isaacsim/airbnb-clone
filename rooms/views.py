from django.views.generic import ListView, DetailView, View
from django.shortcuts import render
from django.core.paginator import Paginator
from . import models, forms

# Create your views here.


class HomeView(ListView):

    """HomeView Definition"""

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"


class RoomDetail(DetailView):

    model = models.Room


class SearchView(View):

    """Search View Definition"""

    def get(self, request):
        # default = False 가 없는 데이터에 대해 폼의 망가짐을 방지하기 위해 request가 비어있으면 바운드를 비움
        country = request.GET.get("country")
        if country:
            form = forms.SearchForm(request.GET)
            if form.is_valid():
                country = form.cleaned_data.get("country")
                city = form.cleaned_data.get("city")
                price = form.cleaned_data.get("price")
                guests = form.cleaned_data.get("guests")
                beds = form.cleaned_data.get("beds")
                bedrooms = form.cleaned_data.get("bedrooms")
                baths = form.cleaned_data.get("baths")
                instant_book = form.cleaned_data.get("instant_book")
                superhost = form.cleaned_data.get("superhost")
                room_type = form.cleaned_data.get("room_type")
                amenities = form.cleaned_data.get("amenities")
                facillities = form.cleaned_data.get("facillities")

                filter_args = {}

                if city != "Anywhere":
                    filter_args["city__startswith"] = city
                print(country)
                if country is None:
                    filter_args["country"] = "KR"
                else:
                    filter_args["country"] = country
                if room_type is not None:
                    filter_args["room_type"] = room_type
                if price is not None:
                    filter_args["price__lte"] = price
                if guests is not None:
                    filter_args["guests__gte"] = guests
                if beds is not None:
                    filter_args["beds__gte"] = beds
                if bedrooms is not None:
                    filter_args["bedrooms__gte"] = bedrooms
                if baths is not None:
                    filter_args["baths__gte"] = baths
                if instant_book is True:
                    filter_args["instant_book"] = True
                if superhost is True:
                    filter_args["host__superhost"] = True
                for amenity in amenities:
                    filter_args["amenities"] = amenity
                for facility in facillities:
                    filter_args["facillities"] = facility

                # 파지네이터를 사용할 때 쿼리셋은 정렬된 상태이어야 한다.
                qs = models.Room.objects.filter(**filter_args).order_by("-created")

                paginator = Paginator(qs, 1, orphans=1)

                page = request.GET.get("page", 1)

                rooms = paginator.get_page(page)

                roots = str(request.get_full_path_info())

                return render(
                    request,
                    "rooms/search.html",
                    {"form": form, "rooms": rooms, "roots": roots, "page": page,},
                )
        else:
            form = forms.SearchForm()
            return render(request, "rooms/search.html", {"form": form})
