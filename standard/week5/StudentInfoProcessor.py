import pickle

class StudentInfoProcessor:
    def read_student_file(self):
        student_list = dict()
        try:
            with open("student_list.db", "rb") as fp:
                student_list = pickle.load(fp)
        except:
            pass

        return student_list

    def restore_student_file(self, student_list):
        with open("student_list.db", "wb") as fp:
            pickle.dump(student_list, fp)
