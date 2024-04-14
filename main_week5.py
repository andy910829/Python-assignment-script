import os
import sys
from unittest.mock import patch
from io import StringIO
import pickle
import importlib

def main():
    folder_path = "python作業評分/week5_copy"
    for test_file in os.listdir(folder_path):
        if test_file == '.DS_Store':
            continue
        test_file_path = os.path.join(folder_path, test_file)
        files_in_test_file = os.listdir(test_file_path)
        path = f'{folder_path}/{test_file}/{files_in_test_file[1]}'
        sys.path.clear()
        print(f'path: {path}')
        sys.path.append(path)
        
        with open("student_dict.db", "wb") as fp:
            pickle.dump({}, fp)
        try:
            test(test_file=test_file, path=path)
        except Exception as e:
            with open('error.txt', 'a') as f:
                f.write(f'Error in {test_file} : {e}\n') 

def test(test_file, path):
    spec = importlib.util.spec_from_file_location("main", f"{path}/main.py")
    main_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(main_module)
    print(f"The path of imported main module: {main_module.__file__}")
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
            main_module.main()
        actual_output = mock_stdout.getvalue().strip()
    assert actual_output == expected_output, f"Test failed in {test_file} : {actual_output}"
    print()
    print("---------------------------------------------------------------------------------------------------")
    
if __name__ == '__main__':
    main()
