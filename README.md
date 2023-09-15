# pysec2023


# EXERCISE 1

OS : Win10

Powershell uzstāda pyenv-win
'''
Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" 
-OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"
'''

CMD uzstāda vajadzīgās python versijas

C:\Windows\System32>pyenv install 3.11.5
:: [Info] ::  Mirror: https://www.python.org/ftp/python
:: [Downloading] ::  3.11.5 ...
:: [Downloading] ::  From https://www.python.org/ftp/python/3.11.5/python-3.11.5-amd64.exe
:: [Downloading] ::  To   C:\Users\Lektors\.pyenv\pyenv-win\install_cache\python-3.11.5-amd64.exe
:: [Installing] ::  3.11.5 ...
:: [Info] :: completed! 3.11.5

C:\Windows\System32>pyenv install 2.7.2
:: [Info] ::  Mirror: https://www.python.org/ftp/python
:: [Downloading] ::  2.7.2 ...
:: [Downloading] ::  From https://www.python.org/ftp/python/2.7.2/python-2.7.2.amd64.msi
:: [Downloading] ::  To   C:\Users\Lektors\.pyenv\pyenv-win\install_cache\python-2.7.2.amd64.msi
:: [Installing] ::  2.7.2 ...
:: [Info] :: completed! 2.7.2


Apskata uzstādītās versijas

C:\Windows\System32>python3 --version
Python 3.11.5

C:\Windows\System32>python --version
Python 2.7.2


Maina versijas

C:\Windows\System32>pyenv global 2.7.2

C:\Windows\System32>pyenv version
2.7.2 (set by C:\Users\Lektors\.pyenv\pyenv-win\version)

C:\Windows\System32>pyenv global 3.11.5

C:\Windows\System32>pyenv version
3.11.5 (set by C:\Users\Lektors\.pyenv\pyenv-win\version)




EXERCISE 2



Uzstāda virtualenv

C:\Windows\System32>pip install virtualenv
Collecting virtualenv
  Obtaining dependency information for virtualenv from https://files.pythonhosted.org/packages/4e/8b/f0d3a468c0186c603217a6656ea4f49259630e8ed99558501d92f6ff7dc3/virtualenv-20.24.5-py3-none-any.whl.metadata
  Downloading virtualenv-20.24.5-py3-none-any.whl.metadata (4.5 kB)
Collecting distlib<1,>=0.3.7 (from virtualenv)
  Obtaining dependency information for distlib<1,>=0.3.7 from https://files.pythonhosted.org/packages/43/a0/9ba967fdbd55293bacfc1507f58e316f740a3b231fc00e3d86dc39bc185a/distlib-0.3.7-py2.py3-none-any.whl.metadata
  Downloading distlib-0.3.7-py2.py3-none-any.whl.metadata (5.1 kB)
Collecting filelock<4,>=3.12.2 (from virtualenv)
  Obtaining dependency information for filelock<4,>=3.12.2 from https://files.pythonhosted.org/packages/5e/5d/97afbafd9d584ff1b45fcb354a479a3609bd97f912f8f1f6c563cb1fae21/filelock-3.12.4-py3-none-any.whl.metadata
  Downloading filelock-3.12.4-py3-none-any.whl.metadata (2.8 kB)
Collecting platformdirs<4,>=3.9.1 (from virtualenv)
  Obtaining dependency information for platformdirs<4,>=3.9.1 from https://files.pythonhosted.org/packages/14/51/fe5a0d6ea589f0d4a1b97824fb518962ad48b27cd346dcdfa2405187997a/platformdirs-3.10.0-py3-none-any.whl.metadata
  Downloading platformdirs-3.10.0-py3-none-any.whl.metadata (11 kB)
Downloading virtualenv-20.24.5-py3-none-any.whl (3.7 MB)
   ---------------------------------------- 3.7/3.7 MB 12.0 MB/s eta 0:00:00
Downloading distlib-0.3.7-py2.py3-none-any.whl (468 kB)
   ---------------------------------------- 468.9/468.9 kB 28.7 MB/s eta 0:00:00
Downloading filelock-3.12.4-py3-none-any.whl (11 kB)
Downloading platformdirs-3.10.0-py3-none-any.whl (17 kB)
Installing collected packages: distlib, platformdirs, filelock, virtualenv
Successfully installed distlib-0.3.7 filelock-3.12.4 platformdirs-3.10.0 virtualenv-20.24.5



Izveido, aktivizē un deaktivizē virtuālās python vides

C:\Windows\system32>cd c:\python

c:\python>virtualenv --python C:\Users\Lektors\AppData\Local\Programs\Python\Python311\python.exe venv3.11
created virtual environment CPython3.11.5.final.0-64 in 967ms
  creator CPython3Windows(dest=C:\python\venv3.11, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=C:\Users\Lektors\AppData\Local\pypa\virtualenv)
    added seed packages: pip==23.2.1, setuptools==68.2.0, wheel==0.41.2
  activators BashActivator,BatchActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator
  
  
  c:\python>.\venv3.11\Scripts\activate

(venv3.11) c:\python>


(venv3.11) C:\python>deactivate
C:\python>



C:\python>virtualenv --python C:\Users\Lektors\AppData\Local\Programs\Python\Python311\python.exe venv2.7
created virtual environment CPython3.11.5.final.0-64 in 843ms
  creator CPython3Windows(dest=C:\python\venv2.7, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=C:\Users\Lektors\AppData\Local\pypa\virtualenv)
    added seed packages: pip==23.2.1, setuptools==68.2.0, wheel==0.41.2
  activators BashActivator,BatchActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator

C:\python>.\venv2.7\Scripts\activate

(venv2.7) C:\python>


C:\python>dir
 Volume in drive C has no label.
 Volume Serial Number is 0002-6A0A

 Directory of C:\python

09/14/2023  07:12 PM    <DIR>          .
09/14/2023  07:12 PM    <DIR>          ..
09/14/2023  07:12 PM    <DIR>          venv2.7
09/14/2023  06:47 PM    <DIR>          venv3.11


Dažādās vidēs uzstāda dažādas biblotēkas

C:\python>.\venv3.11\Scripts\activate

(venv3.11) C:\python>pip install google
Collecting google
  Downloading google-3.0.0-py2.py3-none-any.whl (45 kB)
     ---------------------------------------- 45.3/45.3 kB 448.9 kB/s eta 0:00:00
Collecting beautifulsoup4 (from google)
  Downloading beautifulsoup4-4.12.2-py3-none-any.whl (142 kB)
     ---------------------------------------- 143.0/143.0 kB 2.1 MB/s eta 0:00:00
Collecting soupsieve>1.2 (from beautifulsoup4->google)
  Obtaining dependency information for soupsieve>1.2 from https://files.pythonhosted.org/packages/4c/f3/038b302fdfbe3be7da016777069f26ceefe11a681055ea1f7817546508e3/soupsieve-2.5-py3-none-any.whl.metadata
  Downloading soupsieve-2.5-py3-none-any.whl.metadata (4.7 kB)
Downloading soupsieve-2.5-py3-none-any.whl (36 kB)
Installing collected packages: soupsieve, beautifulsoup4, google
Successfully installed beautifulsoup4-4.12.2 google-3.0.0 soupsieve-2.5


(venv3.11) C:\python>pip install numpy
Collecting numpy
  Obtaining dependency information for numpy from https://files.pythonhosted.org/packages/72/b2/02770e60c4e2f7e158d923ab0dea4e9f146a2dbf267fec6d8dc61d475689/numpy-1.25.2-cp311-cp311-win_amd64.whl.metadata
  Downloading numpy-1.25.2-cp311-cp311-win_amd64.whl.metadata (5.7 kB)
Downloading numpy-1.25.2-cp311-cp311-win_amd64.whl (15.5 MB)
   ---------------------------------------- 15.5/15.5 MB 21.1 MB/s eta 0:00:00
Installing collected packages: numpy
Successfully installed numpy-1.25.2

(venv3.11) C:\python>pip install pandas
Collecting pandas
  Obtaining dependency information for pandas from https://files.pythonhosted.org/packages/b7/f8/32d6b5aa4c4bc045fa2c4c58f88c325facc54721956c6313f0afea8ea853/pandas-2.1.0-cp311-cp311-win_amd64.whl.metadata
  Downloading pandas-2.1.0-cp311-cp311-win_amd64.whl.metadata (18 kB)
Requirement already satisfied: numpy>=1.23.2 in c:\python\venv3.11\lib\site-packages (from pandas) (1.25.2)
Collecting python-dateutil>=2.8.2 (from pandas)
  Downloading python_dateutil-2.8.2-py2.py3-none-any.whl (247 kB)
     ---------------------------------------- 247.7/247.7 kB 1.3 MB/s eta 0:00:00
Collecting pytz>=2020.1 (from pandas)
  Obtaining dependency information for pytz>=2020.1 from https://files.pythonhosted.org/packages/32/4d/aaf7eff5deb402fd9a24a1449a8119f00d74ae9c2efa79f8ef9994261fc2/pytz-2023.3.post1-py2.py3-none-any.whl.metadata
  Downloading pytz-2023.3.post1-py2.py3-none-any.whl.metadata (22 kB)
Collecting tzdata>=2022.1 (from pandas)
  Downloading tzdata-2023.3-py2.py3-none-any.whl (341 kB)
     ---------------------------------------- 341.8/341.8 kB 3.6 MB/s eta 0:00:00
Collecting six>=1.5 (from python-dateutil>=2.8.2->pandas)
  Downloading six-1.16.0-py2.py3-none-any.whl (11 kB)
Downloading pandas-2.1.0-cp311-cp311-win_amd64.whl (11.0 MB)
   ---------------------------------------- 11.0/11.0 MB 16.4 MB/s eta 0:00:00
Downloading pytz-2023.3.post1-py2.py3-none-any.whl (502 kB)
   ---------------------------------------- 502.5/502.5 kB 7.9 MB/s eta 0:00:00
Installing collected packages: pytz, tzdata, six, python-dateutil, pandas
Successfully installed pandas-2.1.0 python-dateutil-2.8.2 pytz-2023.3.post1 six-1.16.0 tzdata-2023.3

(venv3.11) C:\python>deactivate

C:\python>.\venv2.7\Scripts\activate

(venv2.7) C:\python>pip install pytest
Collecting pytest
  Obtaining dependency information for pytest from https://files.pythonhosted.org/packages/df/d0/e192c4275aecabf74faa1aacd75ef700091913236ec78b1a98f62a2412ee/pytest-7.4.2-py3-none-any.whl.metadata
  Downloading pytest-7.4.2-py3-none-any.whl.metadata (7.9 kB)
Collecting iniconfig (from pytest)
  Downloading iniconfig-2.0.0-py3-none-any.whl (5.9 kB)
Collecting packaging (from pytest)
  Downloading packaging-23.1-py3-none-any.whl (48 kB)
     ---------------------------------------- 48.9/48.9 kB 354.7 kB/s eta 0:00:00
Collecting pluggy<2.0,>=0.12 (from pytest)
  Obtaining dependency information for pluggy<2.0,>=0.12 from https://files.pythonhosted.org/packages/05/b8/42ed91898d4784546c5f06c60506400548db3f7a4b3fb441cba4e5c17952/pluggy-1.3.0-py3-none-any.whl.metadata
  Downloading pluggy-1.3.0-py3-none-any.whl.metadata (4.3 kB)
Collecting colorama (from pytest)
  Downloading colorama-0.4.6-py2.py3-none-any.whl (25 kB)
Downloading pytest-7.4.2-py3-none-any.whl (324 kB)
   ---------------------------------------- 324.5/324.5 kB 2.9 MB/s eta 0:00:00
Downloading pluggy-1.3.0-py3-none-any.whl (18 kB)
Installing collected packages: pluggy, packaging, iniconfig, colorama, pytest
Successfully installed colorama-0.4.6 iniconfig-2.0.0 packaging-23.1 pluggy-1.3.0 pytest-7.4.2

(venv2.7) C:\python>pip install socket
ERROR: Could not find a version that satisfies the requirement socket (from versions: none)
ERROR: No matching distribution found for socket

(venv2.7) C:\python>pip install cryptography
Collecting cryptography
  Obtaining dependency information for cryptography from https://files.pythonhosted.org/packages/30/56/5f4eee57ccd577c261b516bfcbe17492838e2bc4e2e92ea93bbb57666fbd/cryptography-41.0.3-cp37-abi3-win_amd64.whl.metadata
  Downloading cryptography-41.0.3-cp37-abi3-win_amd64.whl.metadata (5.3 kB)
Collecting cffi>=1.12 (from cryptography)
  Downloading cffi-1.15.1-cp311-cp311-win_amd64.whl (179 kB)
     ---------------------------------------- 179.0/179.0 kB 14.2 kB/s eta 0:00:00
Collecting pycparser (from cffi>=1.12->cryptography)
  Downloading pycparser-2.21-py2.py3-none-any.whl (118 kB)
     ---------------------------------------- 118.7/118.7 kB 302.1 kB/s eta 0:00:00
Downloading cryptography-41.0.3-cp37-abi3-win_amd64.whl (2.6 MB)
   ---------------------------------------- 2.6/2.6 MB 1.2 MB/s eta 0:00:00
Installing collected packages: pycparser, cffi, cryptography
Successfully installed cffi-1.15.1 cryptography-41.0.3 pycparser-2.21

(venv2.7) C:\python>pip freeze
cffi==1.15.1
colorama==0.4.6
cryptography==41.0.3
iniconfig==2.0.0
packaging==23.1
pluggy==1.3.0
pycparser==2.21
pytest==7.4.2

(venv2.7) C:\python>deactivate
C:\python>.\venv3.11\Scripts\activate

(venv3.11) C:\python>pip freeze
beautifulsoup4==4.12.2
google==3.0.0
numpy==1.25.2
pandas==2.1.0
python-dateutil==2.8.2
pytz==2023.3.post1
six==1.16.0
soupsieve==2.5
tzdata==2023.3

(venv3.11) C:\python>deactivate
C:\python>

