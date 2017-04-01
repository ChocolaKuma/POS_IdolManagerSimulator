import random

firstName = ["Haruto","Riku","Haru","Hinata","Sora"]
lastName = ["Saito","Kobayashi","Nakamura","Yamamoto","Ito"]
minValue = 1
MaxTalent = 5
MaxEnergy = 20
MaxCuteness = 10
CurrentDay = 1
CashOnHand = 9999999
CashSign = "¥"

class actions():
    def TalentTraining(girl):
        global CashOnHand 
        CashOnHand = CashOnHand - 500
        if(girl.talent < MaxTalent):
            t = random.randint(1,4)
            Pt = girl.talent + t
            if(Pt >= MaxTalent):
                girl.talent = MaxTalent
            if(Pt < MaxTalent):
                girl.talent = girl.talent + t
    def EnergyTraining(girl):
        global CashOnHand 
        CashOnHand = CashOnHand - 500
        if(girl.energy < MaxEnergy):
            t = random.randint(1,20)
            Pt = girl.energy + t      
            if(Pt >= MaxEnergy):
                girl.energy = MaxEnergy
            if(Pt < MaxEnergy):
                girl.energy = girl.energy + t
                if(girl.energy > MaxEnergy):
                    girl.energy = MaxEnergy 
    def CuteTraining(girl):
        global CashOnHand 
        CashOnHand = CashOnHand - 500
        if(girl.cuteness < MaxCuteness):
            t = random.randint(1,MaxCuteness/2)
            Pt = girl.energy + t      
            if(Pt >= MaxCuteness):
                girl.cuteness = MaxCuteness
            if(Pt < MaxCuteness):
                girl.cuteness = girl.cuteness + t
                if(girl.cuteness > MaxCuteness):
                    girl.cuteness = MaxCuteness                    
    def PopularityTraining(girl):
        global CashOnHand 
        CashOnHand = CashOnHand - 500
        girl.energy = girl.energy - random.randint(5,10)
        girl.popularity + random.randint(5,500)  
class girl(object):
    def NameMaker(name):
        pick = random.randint(0,4)  
        r = name[pick]
        return r
    def bdaygen():
        month = random.randint(1,12)
        day = random.randint(1,12)
        r = str(month)+"/"+str(day)
        return r
    def __init__(self):
        self.fName = girl.NameMaker(firstName)
        self.lName = girl.NameMaker(lastName)
        self.age = random.randint(14,22)
        self.bday = girl.bdaygen() 
        self.talent = random.randint(1,5)
        self.energy = random.randint(5,20)
        self.cuteness = random.randint(1,10)
        self.popularity = 0
        self.signed = False

def test():
    global CashOnHand
    global CurrentDay
    g = girl()
    print(CashSign,CashOnHand)
    print("Energy:"+str(g.cuteness)+"/"+str(MaxCuteness))

    while g.cuteness < MaxCuteness:  
        actions.CuteTraining(g)
        print(CashSign,CashOnHand)
        print("Energy:"+str(g.cuteness)+"/"+str(MaxCuteness)) 
