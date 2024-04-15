import sys
from unittest.mock import patch
from io import StringIO
import pickle


def main():
    folder_path = "/Users/laiguanhua/Desktop/python作業評分/封存/"
    sys.path.append(f'{folder_path}client')  
    with open(f"{folder_path}server/student_dict.db", "wb") as fp:
        pickle.dump({}, fp)
    test()


def test():
    from main_client import main
    inputs = ['show','exit'] 
    with patch('builtins.input', side_effect=inputs):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            main()
        actual_output = mock_stdout.getvalue().strip()
    with open('standard_output.txt', 'w') as f:
        f.write(actual_output)
    with open('standard_input.txt','w') as f:
        f.write(str(inputs))
    
if __name__ == '__main__':
    main()
