import subprocess
import pickle
import os

def main():
    with open("/Users/laiguanhua/Desktop/python作業評分/封存/server/student_dict.db", "wb") as fp:  # Create an empty student_dict.db file in server side
        pickle.dump({}, fp)
    test()


def test():
    with open('/Users/laiguanhua/Desktop/python作業評分/standard_input.txt','r') as f:
        inputs = f.read().strip().split('\n')
    with open('/Users/laiguanhua/Desktop/python作業評分/standard_output.txt','r') as f:
        expected_output = f.read().strip()
    with open('/Users/laiguanhua/Desktop/python作業評分/temp_stdout.txt', 'w') as temp_stdout:
        subprocess.run(["python3", f"{os.path.dirname(__file__)}/main.py"], input='\n'.join(inputs), stdout=temp_stdout, text=True)
    with open('/Users/laiguanhua/Desktop/python作業評分/temp_stdout.txt', 'r') as f:
        actual_output = f.read().strip()
    try:
        assert actual_output == expected_output, f"Test failed \n{actual_output}"
    except AssertionError as e:
        print(e)

    
    

if __name__ == '__main__':
    main()


