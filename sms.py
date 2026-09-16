class Student:
    def __init__(self,name,age,roll_no):
     self.name = name
     self.age = age
     self.roll_no = roll_no
    def display(self):
        print("Name: ",self.name)
        print("age: ",self.age)
        print("roll_no: ",self.roll_no)
class studentmanagment:
   def __init__(self):
      self.students = []
   def add_student(self):
    print("\n------ADD STUDENT------")
    name = input("Enter your Name: ")
    age = int(input("Enter your age: "))
    roll_no = int(input("Enter roll_no: "))
    studend = Student(name,age,roll_no)
    self.students.append(studend)
    print("successfully added!!!")
   def view_student(self):
    print("\n----ALL STUDENTS----")  
    if len(self.students) == 0:
      print("No Student Found ")
    for student in self.students:
        student.display()
        print("-----------")  
   def search_student(self):
       print("----SEARCH BY ROLLNO----") 
       roll_no = int(input("Enter Roll_no: "))
       for student in self.students:
          if student.roll_no==roll_no:
             print("STUDENT FOUND!!")
             student.display()
             return
       print("student  not found")  
   def update_studend(self):
    print("----UPDATE STUDENT----")
    roll_no = int(input("Enter roll_no to update: "))
    for student in self.students:
       if student.roll_no ==roll_no:
          print("Student found! ")
          new_name =    input("Enter new name: ")
          new_age = int(input("Enter new age: "))
          student.name= new_name
          student.age = new_age
          print("STUDENT UPDATED SUCCESSFULLY!!")
          return
       print("STUDENT NOT FOUND! ") 
   def delete_student(self):
    print("----DELETE STUDENT----")
    roll_no = int(input("Enter rollno to delete: "))
    for student in self.students:
       if student.roll_no == roll_no:
          self.students.remove(student)
          print("Student deleted successfully!!")
          return
    print("STUDENT NOT FOUND! ")   

sms = studentmanagment()
while True:
   print("1:ADD STUDENT: ")
   print("2:VIEW STUDENT: ")
   print("3:SEARCH STUDENT: ")
   print("4:UPDATE STUDENT: ")
   print("5:DELETE STUDENT: ")
   print("6:EXIT!!")
   choice = int(input("Enter your choice: "))
   if choice == 1:
      sms.add_student()
   elif choice == 2:
      sms.view_student()
   elif choice == 3:
      sms.search_student()
   elif choice == 4:
      sms.update_studend()
   elif choice == 5:
      sms.delete_student()
   elif choice==6:
      print("Thank you for using student managment system!!")
      break
   else:
      print("INVALID CHOICE!!")