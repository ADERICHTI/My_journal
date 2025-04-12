import firebaseDB

def MDB(id, Data):
    data = firebaseDB.readDB()
    data[id] = Data
    firebaseDB.updateDB(data)

def RDB():
    data = firebaseDB.readDB()
    hashmap = {}
    for ind, i in enumerate(data):
        if isinstance(data[i], dict):
            data[i]["no"] = ind+1
        hashmap[i] =  data[i]
    return hashmap

# print(RDB())

data = {'12/04/2025': {'image-link': 'hijhihhiud/6666666666666666666', 'log': 'This is amazing', 'no': 1}, '12304/2025': {'image-link': 'hijhihh7878787878/66666', 'log': 'vgvhggyhg', 'no': 2}}

class database:

    def __init__(self, data):
        self.obj_list = []
        
    def all(self):
        class Db:
            ID: str
            log: str
            link: str
            no: str

        for i in data:
            H = data[i]
            obj = Db()
            obj.ID = i
            if "log" in H and "image-link" in H and "no" in H:
                obj.log = H["log"]
                obj.link = H["image-link"]
                obj.no = H["no"]

            self.obj_list.append(obj)

        return self.obj_list

print(database(data).all()[1].no)