


def show_name(name):
    print('---->'+name)



show_name('A')



class Car :

    def __init__(self,name,color):
        self.name=name
        self.color=color


    def show_car(self,tag=None):
        t=''
        if tag is not None:
            t=tag+'===>'
        else : t='---else---'
        print(t+self.name+'@'+self.color)




car=Car('BMW','red')
car.show_car('T')