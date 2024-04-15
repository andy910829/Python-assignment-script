class PrintAll:
    def __init__(self, socket_client):
        self.socket_client = socket_client

    def execute(self):
        self.socket_client.send_command("show", dict())
        result = self.socket_client.wait_response()

        if result['status'] == "OK":
            student_dict = result['parameters']
            print ("\n==== student list ====\n")
            for name, basic_info in student_dict.items():
                print("Name: {}".format(name))
                for subject, score in basic_info['scores'].items():
                    print("  subject: {}, score: {}".format(subject, score))
                print()
            
            print ("======================")
        else:
            print("    Retrieve data fail")
