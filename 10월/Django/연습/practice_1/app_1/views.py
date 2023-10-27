from django.shortcuts import render
import random

def menu(request):
# Create your views here.
    dinner = [
        {"name" : "밥", "src" : "https://i.namu.wiki/i/b4vCFcxoyUzgBHLeqIV_Q9xEeFpK7e-H7cwLfjqzMakmfeERWKASNS8rO9VpvFqndaxD-lFplv3TK6kkLfeFaQ.webp"},
        {"name" : "라면", "src" : "https://i.namu.wiki/i/8s7OaNPsZ8KC1e8RQ6QZEwgfFUoIVVOIm0jA72-UO6Imw0OgI1aEK_DulMeXWbg4tstts3IQFMJS0jmYKD9rzQ.webp" },
        {"name" : "스파게티", "src" : "https://i.namu.wiki/i/_Y1KfAkYUNsL3o_nt_ok1BVfJJwEEO8xiVHMzsQO7fWvvtFwBAWWavROORH3dGOGtBry2kP77hhOnHNPk4Xz5Q.webp"},
        {"name" : "햄버거", "src" : "https://i.namu.wiki/i/o5lE3DhCB9NCYp_AzyPszyOblhB7JDtoWaFiV6H3NNUpKxiwyRaG0fn_XEWzc43fv5uI2cV4EDOrMth9tsbslA.webp"},
    ]
    recommend = random.choice(dinner)
    
    context = {
        'dinner' : dinner,
        'recommend' : recommend,
    }
    return render(request, 'menu.html', context)

def lotto(request):
    number = []
    for i in range(6):
        number.append(random.randrange(1,47))
    # 그냥 random.sample([range(1, 47), 6) 으로 하면 되는거였음

    rank = [{"num" : [12, 19, 21, 29, 40, 45, 1], "ranking" : "1등" }]

    context = {
        'number' : number,
        'rank' : rank,
    }
    return render(request, 'lotto.html', context)