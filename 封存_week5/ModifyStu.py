class ModifyStu:
    def __init__(self, student_dict):
        self.student_dict = student_dict

    def execute(self):
        name = input("  Please input a student's name: ")
        if name == "exit":
            return

        if name not in self.student_dict:
            print("    The name {} is not found".format(name))
        else:
            print ("  current subjects are ", end="")
            for item, _ in self.student_dict[name]["scores"].items():
                print("{} ".format(item), end="")
            print("\n")

            subject_name = input("  Please input a subject you want to change: ")
            if subject_name in self.student_dict[name]["scores"]:
                self.change_score(name, subject_name)     
            else:
                self.add_score(name, subject_name)

            return self.student_dict

    def change_score(self, name, subject_name):
        while True:
            try:
                score = float(input("  Please input {}'s new score of {}: ".format(subject_name, name)))
                break
            except Exception as e:
                print ("    Wrong format with reason {}, try again".format(e))  
        self.student_dict[name]["scores"][subject_name] = score      
        
        print("    Modify [{}, {}, {}] success".format(name, subject_name, score))

    def add_score(self, name, subject_name):
        while True:
            try:
                score = float(input("  Add a new subject for {} please input {} score or < 0 for discarding the subject: ".format(name, subject_name)))
            except Exception as e:
                print ("    Wrong format with reason {}, try again".format(e))
            else:
                if score > 0.0:
                    self.student_dict[name]["scores"][subject_name] = score
                break