from AddStu import AddStu
from PrintAll import PrintAll
from StudentInfoProcessor import StudentInfoProcessor
from SocketServer import SocketServer

action_list = {
    "add": AddStu, 
    "show": PrintAll
}

class JobDispatcher:
    def __init__(self):
        self.student_dict = StudentInfoProcessor().read_student_file()
    
    def job_execute(self, command, parameters):
        self.student_dict, execute_result = action_list[command](self.student_dict).execute(parameters)
        return execute_result

    def job_finish(self):
        StudentInfoProcessor().restore_student_file(self.student_dict)

def main():
    job_dispatcher = JobDispatcher()
    server = SocketServer(job_dispatcher)
    server.daemon = True
    server.serve()

    # because we set daemon is true, so the main thread has to keep alive
    while True:
        command = input()
        if command == "finish":
            break
    
    server.server_socket.close()
    job_dispatcher.job_finish()
    print("leaving ....... ")

main()