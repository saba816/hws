#1
class Test:
    all_stats = []

    def __init__(self,name: str,something: str,money: float,grade: float):
        self.name = name
        self.__something = something
        self.money = money
        self.grade = grade

        Test.all_stats.append(self)
    
    @property
    def something(self):
        return self.__something
    
    @something.setter
    def something(self,value):
        assert len(value)>0, "It can't be empty"
        assert len(value)<10, "It's too long"

        self.__something = value

    def __repr__(self):
        return f"{self.__class__.__name__} ({self.name},{self.__something},{self.money},{self.grade})"
    
    @staticmethod
    def check_idk(z):
        return z ** 4
    
    def __check_to_check(self):
        pass

    def qaqaqad(self):
        self.__check_to_check()
        print("Result: ")
        
man1 = Test("Dio","asdfg",120,70.5)
man2 = Test("Jonatham","qwerty",150,71)
man1.something = "tortasdx"
print(Test.all_stats)
