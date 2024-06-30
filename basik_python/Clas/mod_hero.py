"""------------------------------Father class-------------------------------------"""
class Hero():
    """Clas to Create  Hero for my Game"""

    """First metod"""
    def __init__(self, name, level, race):
        """Initeate our hero"""
        self.name = name
        self.level = level
        self.race = race
        self.health = 100


    def show_hero(self):
        """print all parameters of this Hero"""
        discription = ("Name is " + self.name + " level is "+ str(self.level)+ " Race is "+ self.race+ " Health is "+ str(self.health).title())
        print(discription)

    def level_up(self):
        "Upgrade level"
        self.level += 1

    def set_health(self, new_health):
        self.health = new_health

    def move(self):
        """start moving hero"""
        print("hero", self.name, "start moving" )


"""-------------------------------------Children class-----------------------------------"""
class Superhero(Hero):
    """clas to create Superhero"""

    def __init__(self, name, level, race, magic_typ):
        super().__init__(name, level, race)
        self.magic_typ = magic_typ
        self.magic = 100

    def make_magic(self):
        """use magic"""
        print("skdsh")
        self.magic = self.magic - 10

    def show_hero(self):
        """print all parameters of this Hero"""
        discription = ("Name is " + self.name + " level is "+ str(self.level)+ " Race is "+ self.race + " Magic is " + self.magic_typ + " Mana pool is " + str(self.magic) + " Health is "+ str(self.health).title())
        print(discription)
