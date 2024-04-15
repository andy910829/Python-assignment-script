class AddStu:
    def __init__(self, student_dict):
        self.student_dict = student_dict

    def execute(self, basic_info):

        if basic_info['name'] in self.student_dict:
            execution_result = {
                "status": "Fail",
                "reason": "The name already exists."
            }            
        else:
            self.student_dict[basic_info['name']] = basic_info

            execution_result = {
                "status": "OK"
            }            

        return self.student_dict, execution_result
