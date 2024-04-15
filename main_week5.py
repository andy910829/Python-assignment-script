import os
import subprocess
import pickle


def main():
    folder_path = "/Users/laiguanhua/Desktop/python作業評分/week5拷貝"
    for test_file in os.listdir(folder_path):
        if test_file == '.DS_Store':
            continue
        test_file_path = os.path.join(folder_path, test_file)
        files_in_test_file = os.listdir(test_file_path)
        hw_folder = get_uncompressed_folder(files_in_test_file)
        path = f'{folder_path}/{test_file}/{hw_folder}'
        if not os.path.exists(f"{path}/student_dict.db") and not os.path.exists(f"{path}/student_dict"):
            with open('error.txt', 'a') as f:
                f.write(f'Error in {test_file} : wrong path {path}\n')
            continue
        print(f"{path}/student_dict.db")
        with open(f"{path}/student_dict.db", "wb") as fp:
            pickle.dump({}, fp)
        test(path, test_file)

def test(path, test_file):
    error = f'{test_file} : passed\n-----------------------------------------\n'
    try:
        os.chdir(path)
        with open('/Users/laiguanhua/Desktop/python作業評分/standard_input.txt','r') as f:
            inputs = f.read().strip().split('\n')
        with open('/Users/laiguanhua/Desktop/python作業評分/standard_output.txt','r') as f:
            expected_output = f.read().strip()
        with open('/Users/laiguanhua/Desktop/python作業評分/temp_stdout.txt', 'w') as temp_stdout:
            subprocess.run(["python3", "main.py"], input='\n'.join(inputs), stdout=temp_stdout, text=True)
        with open('/Users/laiguanhua/Desktop/python作業評分/temp_stdout.txt', 'r') as f:
            actual_output = f.read().strip()
        assert actual_output == expected_output, f"Test failed \n{actual_output}"
        print()
        print("---------------------------------------------------------------------------------------------------")
    except AssertionError as e:
        error = f'Error in {test_file} : {e}\n-----------------------------------------\n'
    except Exception as e:
        print(e)
        error = e
    finally:
        with open('/Users/laiguanhua/Desktop/python作業評分/week5_error.txt', 'a') as f:
            f.write(error)
def get_uncompressed_folder(files):
    for folder in files:
        if not folder.endswith('.rar')and not folder.endswith('.zip'):
            return folder

if __name__ == '__main__':
    main()
