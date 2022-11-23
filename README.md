# Final-Demo-Proj
# Prerequisites
- A Python Editor of your choice
For this project the PyCharm IDE and Visual Studio Code were used for development, but the same is not required to correctly deploy the application it self.
- Install the virtual environment package
Virtual Environment (virtualenv) is a tool to create isolated Python environments. The virtualenv command creates a folder which contains all the necessary executables to use the packages that a Python project would need. The same can be installed as described in this link through the following command:
```
$ pip install virtualenv
$ mkdir new   
$ cd new   
$ virtualenv venv  
$ venv/bin/activate   
$ venv\scripts\activate  
$ pip install flask

```
- For this Project needs sqlite.
```
pip install pysqlite
```
# Deployment
```
$ python app.py
```
The same will enable the project to be accessed by you web browser trough a URL displayed by the mentioned command execution.
