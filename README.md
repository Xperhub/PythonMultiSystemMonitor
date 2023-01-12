# PythonMultiSystemMonitor
A python script that can be use to Monitor Multiple System. 


The python script is use to Monitor Multiple system at a go and send email alert to specific user when the system is down.


#Implementation

The scripts make use of python ThreadPoolExecutor which makes it easy to start up a group of threads and it’s part of the standard library in concurrent.futures (as of Python 3.2).

I used python built smtplib to send my email using gmail smtp details.


I also implemented logging the response of the process.

It is a simple python script.
