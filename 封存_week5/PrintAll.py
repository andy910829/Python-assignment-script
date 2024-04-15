class PrintAll:
    def __init__(self, student_dict):
        self.student_dict = student_dict

    def execute(self):
        print ("\n==== student list ====\n")
        for name, basic_info in self.student_dict.items():
            print("Name: {}".format(name))
            for subject, score in basic_info['scores'].items():
                print("  subject: {}, score: {}".format(subject, score))
            print()
        
        print ("======================")

        return self.student_dict
