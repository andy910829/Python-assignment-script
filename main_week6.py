import subprocess
import pickle
import os

def main():
    with open("/Users/laiguanhua/Desktop/python作業評分/封存_week6/server/student_dict.db", "wb") as fp:  # Create an empty student_dict.db file in server side
        pickle.dump({}, fp)
    folder_path = "/Users/laiguanhua/Desktop/python作業評分/week6拷貝"
    for test_file in os.listdir(folder_path):
        if test_file == '.DS_Store':
            continue
        test_file_path = os.path.join(folder_path, test_file)
        files_in_test_file = os.listdir(test_file_path)
        hw_folder = get_uncompressed_folder(files_in_test_file)
        path = f'{folder_path}/{test_file}/{hw_folder}'
        if os.path.exists(f'{path}/main.py'):
            path = f'{path}/main.py'
        elif os.path.exists(f'{path}/main_client.py'):
            path = f'{path}/main_client.py'
        else:
            with open('week6_error.txt', 'a') as f:
                f.write(f'Error in {test_file} : wrong path {path}\n-----------------------------------------\n')
            continue
        test(path, test_file)

def get_uncompressed_folder(files):
    for folder in files:
        if not folder.endswith('.rar')and not folder.endswith('.zip'):
            return folder
        
def test(path, test_file):
    error = f'{test_file} : passed\n-----------------------------------------\n'
    with open('/Users/laiguanhua/Desktop/python作業評分/standard_input.txt','r') as f:
        inputs = f.read().strip().split('\n')
    with open('/Users/laiguanhua/Desktop/python作業評分/standard_output.txt','r') as f:
        expected_output = f.read()
    with open('/Users/laiguanhua/Desktop/python作業評分/temp_stdout.txt', 'w') as temp_stdout:
        subprocess.run(["python3", path], input='\n'.join(inputs), stdout=temp_stdout, text=True)
    with open('/Users/laiguanhua/Desktop/python作業評分/temp_stdout.txt', 'r') as f:
        actual_output = f.read()
    try:
        if actual_output.strip() != expected_output.strip():
            error = f'Error in {test_file} : {actual_output}\n-----------------------------------------\n'
    except Exception as e:
        error = str(e)
        print(error)
    finally:
        with open('/Users/laiguanhua/Desktop/python作業評分/week6_error.txt', 'a') as f:
            f.write(error)

    
    

if __name__ == '__main__':
    main()


