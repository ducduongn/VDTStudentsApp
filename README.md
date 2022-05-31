# **Cài đặt Openstack All-in-one bằng Kolla Ansible**
## **Table of Contents**

[I. Overview](#overview)   

       
-
 [II. Step-by-step](#steps)
   - [1. Set up virtual environment](#venv)            
   - [2. Install dependencies](#dependencies)    
- [References](#refs)             
----  

## I. Overview
<a name='overview'></a >      



## II. Step-by-step 
<a name='steps'></a >      

### 1. Set up virtual environment
<a name='venv'></a >      

- Firstly you need to set up an virtual environment for Python in order to keep dependencies from multiple projects not conflict with each other. If your Python version is 3.3 or above, you don't need to install anything because the standard library has already provided virtualenv under the module "venv". Just type the below command to setup virtualenv:

```
$ python -m venv ./venv  
```

- If you Python version is older, you'll need to install [this Python utility](https://virtualenv.pypa.io/en/stable/) which allows you to create and manage Python virtual environments. Use the virtualenv command to create a new virtual environment

```
virtualenv --python C:\Path\To\Python\python.exe venv
```
- To activate the virtualenv:

```
.\venv\Scripts\activate
```

### 2. Intall dependencies
<a name='dependencies'></a >      

- Firstly, install Flask and the Twilio Python SDK:

```
pip install Flask twilio
```

## Tài liệu tham khảo
<a name='refs'></a >      

[1] https://www.twilio.com/docs/usage/tutorials/how-to-set-up-your-python-and-flask-development-environment
 
