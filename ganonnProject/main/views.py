from django.shortcuts import render, get_object_or_404

# Create your views here.

def homeView(request):
    return render(request, 'home.html')


def gameinfoView(request, game_id):
    game_detail = get_object_or_404(Game, pk=game_id)
    return render(request, 'gameinfo.html', {'game': game_detail})
