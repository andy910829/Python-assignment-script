class PrintAll:
    def __init__(self, student_dict):
        self.student_dict = student_dict

    def execute(self, dummy):
        execution_result = {
            "status": "OK",
            "parameters": self.student_dict
        }

        return self.student_dict, execution_result
