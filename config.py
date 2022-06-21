#! ../venv/bin/python3

from configparser import ConfigParser

from logging import raiseExceptions


def config(file_name='database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(file_name)
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raiseExceptions(f'Section {section} is not found in {file_name} file')
    return db
