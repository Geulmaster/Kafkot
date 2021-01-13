from configparser import ConfigParser
from pathlib import Path

def config_reader():
    config_file = Path(__file__).parent / 'configuration.ini'
    parser = ConfigParser()
    parser.read(config_file)
    return parser