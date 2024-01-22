class SGPA:
    def __init__(self,name,data_dict):
        self.name=name
        self.points = 0
        self.data_dict = data_dict
        self.to_points = self.calculate_points()
        self.to_credits = self.calculate_total_credits()
        print(f"The SGPA of {self.name} is {self.calculate_actual_sgpa(self.to_points,self.to_credits):.2f}")


    def calculate_points(self):
        total_points=0
        for key, value in self.data_dict.items():
            self.grade = value[0]
            if self.grade == 'O':
                self.points = 10
            elif self.grade == 'A+':
                self.points = 9
            elif self.grade == 'A':
                self.points = 8
            elif self.grade == 'B+':
                self.points = 7
            elif self.grade == 'B':
                self.points = 6
            elif self.grade == 'C':
                self.points = 5
            elif self.grade == 'P':
                self.points = 4
            elif self.grade == 'F':
                self.points = 0

            total_points += self.points*value[1]


        return total_points


    def calculate_total_credits(self):
        total_credits=0
        for key, value in self.data_dict.items():
            total_credits += value[1]
        return total_credits


    def calculate_actual_sgpa(self,tot_points,tot_credits):
        return tot_points/tot_credits



subjects_grades = {"FEE": ["O", 4], "OOPUC": ["A+", 5],"EPICS":["O",2],"DS":["O",4],"DBMS":["O",4],"CN":["A+",4]}
nm = "Anshul"

# nm=input("Enter your name : ")
# n=int(input("Enter number of subjects:"))
# for i in range(n):
#     key=input("Enter subject")
#     value1=input("Enter Grade : ")
#     value2=int(input("Enter Credits : "))
#     subjects_grades.update({key: [value1, value2]})

nm=SGPA(nm,subjects_grades)
