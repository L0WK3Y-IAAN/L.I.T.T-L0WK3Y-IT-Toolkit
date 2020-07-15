from setuptools import setup

APP = ['L.I.T.T  by @L0WK3Y_IAANSEC.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['certifi'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires={'py2app'},

)