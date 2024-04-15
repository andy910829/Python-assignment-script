import sys
import subprocess
import pickle


def main():
    week = input("Please enter the week number: ")
    if week == '5':
        folder_path = "/Users/laiguanhua/Desktop/python作業評分/封存_week5/main.py"
        sys.path.append(f'{folder_path}')  
    elif week == '6':
        folder_path = "/Users/laiguanhua/Desktop/python作業評分/封存_week6/"
        sys.path.append(f'{folder_path}')  
        with open(f"{folder_path}server/student_dict.db", "wb") as fp:
            pickle.dump({}, fp)
        folder_path += 'client/main_client.py'
    test(folder_path)


def test(path):
    print(path)
    inputs = ['show','exit'] 
    with open('/Users/laiguanhua/Desktop/python作業評分/standard_output.txt', 'w') as temp_stdout:
        subprocess.run(["python3", path], input='\n'.join(inputs), stdout=temp_stdout, text=True)
    with open('standard_input.txt','w') as f:
        f.write('\n'.join(inputs))

    
if __name__ == '__main__':
    main()
