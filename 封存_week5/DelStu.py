class DelStu:
    def __init__(self, student_dict):
        self.student_dict = student_dict

    def execute(self):
        name = input("  Please input a student's name: ")
        if name == "exit":
            return

        if name in self.student_dict:
            del self.student_dict[name]
            print("    Del {} success".format(name))
        else:
            print("    The name {} is not found".format(name))
        
        return self.student_dict
