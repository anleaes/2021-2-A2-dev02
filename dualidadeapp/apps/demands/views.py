from django.shortcuts import render, get_object_or_404, redirect
from .forms import DemandForm, DemandTeamLikeForm
from .models import Demand, DemandTeamLike, Team

# Create your views here.
def add_demand(request):
    template_name = 'demands/add_demand.html'
    context = {}
    if request.method == 'POST':
        form = DemandForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('demands:list_demands')
    form = DemandForm()
    context['form'] = form
    return render(request, template_name, context)

def list_demands(request):
    template_name = 'demands/list_demands.html'
    demands = Demand.objects.filter()
    context = {
        'demands': demands
    }
    return render(request, template_name, context)

def demand_detail(request, id_demand):
    template_name = 'demands/demand_detail.html'
    demand = get_object_or_404(Demand, id=id_demand)
    demandTeamLikes = DemandTeamLike.objects.filter()
    context = {
        'demand': demand,
        'demandTeamLikes': demandTeamLikes
    }
    if request.method == "POST":
        print("POSTTTTTTTT")
        team_id = request.POST['accept']
        print("TEAM ID: " + team_id)
        if team_id:
            team = Team.objects.get(id=int(team_id))
            if team:
                demand.team = team
                demand.status = 'Em andamento'
                demand.save()
                return redirect('demands:list_demands')

    return render(request, template_name, context)
    
def edit_demand(request, id_demand):
    template_name = 'demands/add_demand.html'
    context ={}
    demand = get_object_or_404(Demand, id=id_demand)
    if request.method == 'POST':
        form = DemandForm(request.POST, request.FILES,  instance=demand)
        if form.is_valid():
            form.save()
            return redirect('demands:list_demands')
    form = DemandForm(instance=demand)
    context['form'] = form
    return render(request, template_name, context)
    
def demand_add_like(request, id_demand):
    template_name = 'demands/demand_add_like.html'
    context ={}
    if request.method =='POST':
        form = DemandTeamLikeForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            demand = Demand.objects.get(id=id_demand)
            f.demand = demand
            f.save()
            form.save_m2m()
            return redirect('demands:list_demands')
        form = DemandForm()
        context['form'] = form

    return render(request, template_name, context)

def delete_demand(request, id_demand):
    demand = Demand.objects.get(id=id_demand)
    demand.delete()
    return redirect('demands:list_demands')

def search_demands(request):
    template_name = 'demands/list_demands.html'
    query = request.GET.get('query')
    demands = Demand.objects.filter(title__icontains=query) | Demand.objects.filter(description__icontains=query)
    context = {
        'demands': demands,
    }
    return render(request,template_name, context)