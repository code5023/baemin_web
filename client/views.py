from django.shortcuts import render
from partner.models import Partner

# Create your views here.
def index(request):
    ctx = {}
    # partner_list = Partner.objects.filter(user = request.user.is_active)
    partner_list = Partner.objects.filter(active=True)
    category = request.GET.get("category")

    if not category:
        partner_list = Partner.objects.all()
    else:
        partner_list = Partner.objects.filter(category=category)
    category_list = set([
        (food_type.category, food_type.get_category_display()) for food_type in partner_list
    ])
    ctx.update({"partner_list" : partner_list, "category_list" : category_list})

    return render(request, "main.html", ctx)
