import sys
from unittest.mock import patch
from io import StringIO
import pickle


def main():
    week = input("Please enter the week number: ")
    if week == '5':
        folder_path = "/Users/laiguanhua/Desktop/python作業評分/封存_week5/"
        sys.path.append(f'{folder_path}')  
        test_week5()
    elif week == '6':
        folder_path = "/Users/laiguanhua/Desktop/python作業評分/封存_week6/"
        sys.path.append(f'{folder_path}client')  
        with open(f"{folder_path}server/student_dict.db", "wb") as fp:
            pickle.dump({}, fp)
        test_week6()


def test_week6():
    from main_client import main
    inputs = ['show','exit'] 
    with patch('builtins.input', side_effect=inputs):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            main()
        actual_output = mock_stdout.getvalue().strip()
    with open('standard_output.txt', 'w') as f:
        f.write(actual_output)
    with open('standard_input.txt','w') as f:
        f.write('\n'.join(inputs))

def test_week5():
    from main import main
    inputs = ['show','exit'] 
    with patch('builtins.input', side_effect=inputs):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            main()
        actual_output = mock_stdout.getvalue().strip()
    with open('standard_output.txt', 'w') as f:
        f.write(actual_output)
    with open('standard_input.txt','w') as f:
        f.write('\n'.join(inputs))
    
if __name__ == '__main__':
    main()
