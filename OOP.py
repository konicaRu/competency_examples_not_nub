class Driver:
    name = "Hill"
    greeting = 'Hi'
    age = 26
    growth = 156
    weight = 55
    speed_reaction = 12
    experience = 15
    aggressiveness = 50
    mood = 'lower'

    def go(self, speed):#меняем скорость
        self.speed_reaction = speed

    def food(self, food):#кормим пилота
        self.weight += food

    def dr_Senna(self): #меняем пилота
        self.name = "Senna"
        self.greeting = 'Fuck'
        self.age = 22
        self.growth = 170
        self.weight = 59
        self.speed_reaction = 20
        self.experience = 6
        self.aggressiveness = 100
        self.mood = 'middle'

    @classmethod
    def kind_dr(cls):#гоночная серия
        return 'Formula1'


my_drS = Driver()
my_drS.dr_Senna()
my_drS.go(50)
my_drS.food(120)

print(my_drS.name, my_drS.speed_reaction, my_drS.weight)
print(Driver.kind_dr())


# VPN сервис
class VPN_server:
    server_location = 'USA'
    data_transfer_rate = 100
    encryption_level = 256
    ip_address = 'stat'

    def ip_st(self):
        self.ip_address = 'stat'

    def ip_din(self):
        self.ip_address = 'dinam'

    def locat_serv(self, country):
        self.server_location = country

    def ip_Germ(self):
        self.server_location = 'Germany'
        self.data_transfer_rate = 150
        self.encryption_level = 356
        self.ip_address = 'dinam'

    @classmethod
    def server(cls):
        return 'server'
