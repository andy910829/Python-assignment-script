import configparser

CONFIG = configparser.ConfigParser()
CONFIG.read('config/config.ini')

OUTPUT_PATH = CONFIG['config']['output_path']
FOLDER_PATH = CONFIG['config']['folder_path']
STANDARD_PATH = CONFIG['config']['standard_path']