class Robot:
    def __init__(self, parancs, dic):
        self.parancs = parancs
        self.dic = dic
    def count(self):
        for i in self.parancs:
            if i in dic.keys():
                dic[i] += 1
            else:
                dic[i] = 1
        for i in dic.keys():
            print(f"{i} betűk száma: {dic[i]}")
        return dic
    def egyszerusit(self):
        if "E" in dic.keys():
            if "D" in dic.keys():
                if dic["E"] >= dic["D"]:
                    dic["E"] = dic["E"] - dic["D"]
                    dic["D"] = 0
                else:
                    dic["D"] = dic["D"] - dic["E"]
                    dic["E"] = 0
        if "K" in dic.keys():
            if "N" in dic.keys():
                if dic["K"] >= dic["N"]:
                    dic["K"] = dic["K"] - dic["N"]
                    dic["N"] = 0
                else:
                    dic["N"] = dic["N"] - dic["K"]
                    dic["K"] = 0
        print("Egy legröbidebb út parancsszava:", end=" ")
        if "E" in dic.keys():
            print("E"*dic["E"], end="")
        if "D" in dic.keys():
            print("D"*dic["D"], end="")
        if "K" in dic.keys():
            print("K"*dic["K"], end="")
        if "N" in dic.keys():
            print("N"*dic["N"], end="")

dic = {}
parancs = []
utasitas = input("")
utasitas = utasitas.strip().upper()

for i in utasitas:
    parancs.append(i)

robot = Robot(parancs, dic)

robot.count()
robot.egyszerusit()