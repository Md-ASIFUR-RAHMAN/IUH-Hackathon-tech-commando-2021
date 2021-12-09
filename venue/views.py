from django.shortcuts import render

# Create your views here.
def Home(request):
    if request.method == "GET":
        return render(request, 'venue/home.html')


    if request.method == "POST":
        name = request.POST['u-name']
        passw = request.POST['u-passw']


        if name == 'ITQAN' and passw == 'ITQAN#9696' :
            return render(request, 'venue/success.html')
        else:
            return render(request, 'venue/unsuccess.html')

def action_handler(request,action):
    if action == 'login':
        return render(request, 'venue/loginpage.html')

    elif action == 'reg':
        return render(request, 'venue/reg.html')