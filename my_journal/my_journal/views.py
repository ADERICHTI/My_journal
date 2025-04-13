from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from . import firebaseDB
import json

class database:

    def __init__(self, data):
        self.data = data
        self.obj_list = []
        
    def all(self):
        class Db:
            ID: str
            log: str
            link: str
            no: str

        for i in self.data:
            H = self.data[i]
            obj = Db()
            obj.ID = i
            if "log" in H and "image-link" in H and "no" in H:
                obj.log = H["log"]
                obj.link = H["image-link"]
                obj.no = H["no"]

            self.obj_list.append(obj)

        return self.obj_list
    

def MDB(id, Data):

    data = firebaseDB.readDB()
    if not isinstance(data, dict):
        if data[id] not in data:
            data[id] = Data
        else:
            Data["no"] = len(RDB())+1
            data[id] = Data
        firebaseDB.updateDB(data)
    else:
        Data["no"] = 1
        firebaseDB.updateDB({id:Data})


def RDB():
    data = firebaseDB.readDB()
    hashmap = {}
    for ind, i in enumerate(data):
        hashmap[i] =  data[i]
    return hashmap

def Login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username= username, password= password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request, "login.html", {"msg": "Incorrect credentials"})
        
    return render(request, "login.html", {"msg":"None"})

def Logout(request):
    logout(request)
    return redirect("login")

@login_required
def home(request):

    data = RDB()
    logs = []
    if data:
        db = database(data)

        logs = db.all()

    return render(request, 'index.html', {"logs": logs})

@login_required
def journal(request):
    if request.method == "POST":
        data = request.POST
        ID = data["id"]
        Data = {"log":data["body"], "image-link":data["link"]}
        match data["value"]:
            case "update":
                MDB(id = ID, Data=Data)
            case "new":
                MDB(id = ID, Data=Data)


    return redirect('home')
