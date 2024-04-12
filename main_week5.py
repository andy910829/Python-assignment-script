import os
import sys
from unittest.mock import patch


def change_file_name(folder_path):
    test_list = list()
    for filename in os.listdir(folder_path):
        src_path = os.path.join(folder_path, filename)
        new_filename = 's' + filename[:9]
        dst_path = os.path.join(folder_path, new_filename)
        os.rename(src_path, dst_path)
        test_list.append(new_filename)
        print(f"重命名 {filename} 為 {new_filename}")
    return test_list[:0]


def main_test():
    folder_path = "python作業評分/week5_copy"
    for test_file in os.listdir(folder_path):
        if test_file == '.DS_Store':
            continue
        else:
            print(f'{folder_path}/{test_file}/week05')
            if os.path.exists(f'{folder_path}/{test_file}/week05'):
                path = f'{folder_path}/{test_file}/week05'
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

                with patch('builtins.input', side_effect=['show','add','aaa','python','66','exit','show','del','aaa','exit','exit']):
                    # main()
                    try:
                        main()
                    except Exception as e:
                        print(e)
                        with open('error.txt', 'w') as f:
                            f.write(f'Error in {test_file}')
                print()
                print("---------------------------------------------------------------------------------------------------")
            except Exception as e:
                with open('error.txt', 'w') as f:
                    f.write(f'Error in {test_file} : {e}') 
        
        

if __name__ == '__main__':
    main_test()
