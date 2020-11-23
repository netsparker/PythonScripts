# **Python Scripts for Netsparker Enterprise API Endpoints**

The scripts are constructed to be used through CLI. Arguments need to be passed for most of them.

## **Installation**

**1) Python**

Download & install Python 3.8 using this link: https://www.python.org/downloads/

Confirm the installation once it is done via CLI as follows;

```bash
python --version
```

**2) Libraries**

We need 2 libraries for all of the scripts. 

The first one is the *argparse* module. The argparse module makes it easy to write user-friendly command-line interfaces. The program defines what arguments it requires, and argparse will figure out how to parse those out of *sys.argv*. The argparse module also automatically generates help and usage messages and issues errors when users give the program invalid arguments. 

The second one is the *requests* module. Requests allows you to send HTTP/1.1 requests extremely easily. There’s no need to manually add query strings to your URLs, or to form-encode your POST data. Keep-alive and HTTP connection pooling are 100% automatic, thanks to *urllib3*.

To download & install both of the modules, open CLI, navigate to the project's folder and run the below command;

```bash
pip install -r requirements.txt
```

**3) Setting config.JSON File**

First, we need to configure the **config.json** according to our accounts on Netsparker Enterprise. Navigate to Netsparker Enterprise on any browser and log into your account. Click on your name which is located at the top-right corner of the page and select *API Settings*. After entering your account password, the *User ID* and the *Token* will be revealed.

In the project's folder, find and open **config.json** with a text editor. Now, copy the 2 values described above and paste it into **config.json**. The values must be inside the quotes.

As for the 3rd parameter (*API_ROOT*), it should point out to the root URL. For default, it is set to https://www.netsparkercloud.com/api/1.0/%s . If you use Netsparker Enterprise on EU region or Netsparker Enterprise On-Premises version, you need to modify this value as well. Examples;

EU Region -> "API_ROOT": "https://eu.netsparker.cloud/api/1.0/%s"
Sample On-Premises -> "API_ROOT": "https://netsparker.mycompany.com/api/1.0/%s"
Another sample On-Premises -> "API_ROOT": "http://localhost/api/1.0/%s"

Once everything is done, save & close **config.json**.

## **Running a script**

Run **cmd.exe** and navigate to the folder where the scripts are located. Execute the script file using the necessary/desired arguments. A sample command should be like this;

```bash
"script.py" -arg1 val1 -arg2 val2
```

**Tip!**: To see every argument available for each script, you can try -h with the script file;

```bash
"script.py" -h
```

The below example shows using *scans_listbywebsite* script with 2 arguments;

```bash
"scans_listbywebsite.py" -w http://php.testsparker.com/ -sort Ascending
```
