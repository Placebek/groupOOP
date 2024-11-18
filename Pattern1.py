# 1-нұсқа
class Faculty:
    def __init__(self, name):  
        self.name = name

    def __str__(self):  
        return f"Faculty: {self.name}"


class University:
    def __init__(self, name): 
        self.name = name
        self.faculties = []

    def add(self, faculty):
        self.faculties.append(faculty)

    def remove(self, name):
        self.faculties = [f for f in self.faculties if f.name != name]

    def show(self):
        print(f"University: {self.name}", *self.faculties, sep="\n")

    def __del__(self): 
        print(f"Deleting {self.name} and faculties!")


uni = University("KarTU")
uni.add(Faculty("Information Technology"))
uni.add(Faculty("Information System"))
uni.show()
uni.remove("Information System")
uni.show()
del uni  
