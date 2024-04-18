class AddStu:
    def __init__(self, student_dict):
        self.student_dict = student_dict

    def execute(self):
        duplicate = True
        while duplicate:
            name = input("  Please input a student's name or exit: ")
            duplicate = False
            if name in self.student_dict:
                duplicate = True
                print ("    {} already exists".format(name))

        if name == "exit":
            return

        score_dict = dict()

        while True:
            subject = input("  Please input a subject name or exit for ending: ")
            if subject != "exit":
                while True:
                    try:
                        score = float(input("  Please input {}'s {} score or < 0 for discarding the subject: ".format(name, subject)))
                    except Exception as e:
                        print ("    Wrong format with reason {}, try again".format(e))
                    else:
                        if score > 0.0:
                            score_dict[subject] = score
                        break
            else:
                break

        if len(score_dict) > 0:
            basic_info = {
                "name": name,
                "scores": score_dict
            }
            self.student_dict[name] = basic_info
            print("    Add {} success".format(basic_info))
        else:
            print("    Add nothing")

        return self.student_dict
