import os
import sys
from unittest.mock import patch
from io import StringIO
import pickle

def main():
    week = 'week05'
    folder_path = "python作業評分/week5_copy"
    for test_file in os.listdir(folder_path):
        if test_file == '.DS_Store':
            continue
        print(f'{folder_path}/{test_file}/{week}')
        if os.path.exists(f'{folder_path}/{test_file}/{week}'):
            path = f'{folder_path}/{test_file}/{week}'
        elif os.path.exists(f'{folder_path}/{test_file}/to_student'):
            path = f'{folder_path}/{test_file}/to_student'
        sys.path.insert(0, path)
        with open("student_dict.db", "wb") as fp:
            pickle.dump({}, fp)
        try:
            test(test_file=test_file,path=path)
        except Exception as e:
            with open('error.txt', 'a') as f:
                f.write(f'Error in {test_file} : {e}\n') 

def test(test_file,path):
    from main import main
    inputs = ['show','exit']
    expected_output = """add: Add a student's name and score
del: Delete a student
modify: Modify a student's score
show: Print all
exit: Exit

==== student list ====

======================

add: Add a student's name and score
del: Delete a student
modify: Modify a student's score
show: Print all
exit: Exit
'exit'
""".strip()  # 输入预期输出结果
    with patch('builtins.input', side_effect=inputs):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                main()
        actual_output = mock_stdout.getvalue().strip()
    assert actual_output == expected_output, f"Test failed in {test_file} : {actual_output}"
    print()
    print("---------------------------------------------------------------------------------------------------")
    
    

if __name__ == '__main__':
    main()


