### Python Test Framework for testing Frontend and Backend functionality

#

#### Framework schema
![image](https://github.com/coastal-lines/PythonTestFramework/blob/master/doc/images/project_diagram.png?raw=true)

#

#### Test types
| HTTP/WS   | Web | Desktop | Mobile | Visual Tests
|-----------| ------ | ------ | ------ | ------ |
| API       | BDD | Windows | Android | Appium
| WebSocket | BrowserStack |||Karaburma|
|           |Selenium |

#

#### Used python version
- 3.12.2

#

#### Used applications and services
For some of API tests you have to have an Azure DevOps account.
<br />
Also your machine should has FreeQuizMaker for some Desktop tests.
<br />
For BrowserStack tests you should use your own access key and login.
<br />
Android tests use Android Emulator.

| API  | Web |Desktop | Mobile
| ------ | ------ | ------ | ------ |
| Azure DevOps | BrowserStack | Free Quiz Maker | Aptitude 

#

#### Installation (cmd)
- Please check your python version 
```sh
python --version
```
- Clone this project into your machine
```sh
cd <your_projects_folder>
git clone https://github.com/coastal-lines/PythonTestFramework.git & cd PythonTestFramework
```
- Create virtual environment and activate it
```sh
python -m venv venv
venv\Scripts\activate
```
- Install requirements
```sh
pip install -r requirements.txt
```
- Install [Karaburma](https://github.com/coastal-lines/Karaburma) as an additional requirements
```sh
:: Download Karaburma and install all requirements
cd <your_projects_folder>
git clone https://github.com/coastal-lines/Karaburma.git & cd Karaburma
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

:: Install Karaburma into PythonTestFramework as package
deactivate
cd .. & cd PythonTestFramework
venv\Scripts\activate
cd .. & cd Karaburma
python setup.py install
```

#

#### How to run tests
- Single test
```sh
cd PythonTestFramework
venv\Scripts\python.exe -m pytest -p no:warnings -k "test_name"
```

- Single test with Allure report
```sh
cd PythonTestFramework
venv\Scripts\python.exe -m pytest --alluredir=.\resources\logs\allure-report\ -k "test_name"
```
```sh
<allure_folder>\allure-commandline\dist\bin\allure.bat serve <your_projects_folder>\PythonTestFramework\resources\logs\allure-report\
```
