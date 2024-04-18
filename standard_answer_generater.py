import os
import subprocess
from pickle import dump


def main():
    week = input("Please enter the week number: ")

    if week == '5':
        folder_path = "standard/week5/main.py"

    elif week == '6':
        folder_path = "standard/week6/"

        with open(f"{folder_path}server/student_dict.db", "wb") as fp:
            dump({}, fp)

        folder_path += 'client/main_client.py'

    test(folder_path)

def test(path):
    inputs = ['show','exit']

    with open('output/standard_output.txt', 'w') as temp_stdout:
        subprocess.run(["python3", path], input='\n'.join(inputs), stdout=temp_stdout, text=True)

    with open('output/standard_input.txt', 'w') as f:
        f.write('\n'.join(inputs))

    if os.path.exists('student_list.db'):
        os.remove('student_list.db')

if __name__ == '__main__':
    main()