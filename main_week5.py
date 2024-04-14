# import os
# import sys
# from unittest.mock import patch


# def main_test():
#     week = 'week05'
#     folder_path = "python作業評分/week5_copy"
#     for test_file in os.listdir(folder_path):
#         if test_file == '.DS_Store':
#             continue
#         print(f'{folder_path}/{test_file}/{week}')
#         if os.path.exists(f'{folder_path}/{test_file}/{week}'):
#             path = f'{folder_path}/{test_file}/{week}'
#         elif os.path.exists(f'{folder_path}/{test_file}/to_student'):
#             path = f'{folder_path}/{test_file}/to_student'
#         sys.path.insert(0, path)
#         try:
#             if os.path.exists(f'{path}/student_dict.db'):    
#                 os.remove(f'{path}/student_dict.db')
#             elif os.path.exists(f'{path}/student_dict'):
#                 os.remove(f'{path}/student_dict')
#             with open(f'{path}/student_dict.db', 'w') as f:
#                 f.write('')
#             from main import main

#             with patch('builtins.input', side_effect=['show','add','aaa','python','66','exit','show','del','aaa','exit','exit']):
#                 # main()
#                 try:
#                     main()
#                 except Exception as e:
#                     print(e)
#                     with open('error.txt', 'w') as f:
#                         f.write(f'Error in {test_file}')
#             print()
#             print("---------------------------------------------------------------------------------------------------")
#         except Exception as e:
#             with open('error.txt', 'w') as f:
#                 f.write(f'Error in {test_file} : {e}') 
        
        

# if __name__ == '__main__':
#     main_test()


import os
import sys
from unittest.mock import patch
from io import StringIO


def main_test():
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
        try:
            if os.path.exists(f'{path}/student_dict.db'):    
                os.remove(f'{path}/student_dict.db')
            elif os.path.exists(f'{path}/student_dict'):
                os.remove(f'{path}/student_dict')
            with open(f'{path}/student_dict.db', 'w') as f:
                f.write('')
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
    """  # 输入预期输出结果

            with patch('builtins.input', side_effect=inputs):
                with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                    main()
                actual_output = mock_stdout.getvalue().replace('\n', '').strip()
                print(actual_output)
                print('-'*50)
                print(expected_output)
                assert actual_output == expected_output.replace('\n', '').strip(), f"Test failed in {test_file}"
                
            print()
            print("---------------------------------------------------------------------------------------------------")
        except Exception as e:
            with open('error.txt', 'w') as f:
                f.write(f'Error in {test_file} : {e}') 
        
        

if __name__ == '__main__':
    main_test()
