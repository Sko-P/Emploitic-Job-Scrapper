# Emploitic-Job-Scrapper

## Description 
Scraps the job offers available when entering a specefic keyword.  

**Selenium** is used to scrap the website. 

## Installation

Steps to use this scrapper : 

* Install the requirements : 

```bash
pip install requirements.txt
```

**NOTE:** The webdriver of the web browser you are using is <ins>**mandatory**</ins> for the functionnality of **Selenium**. Make sure to download that and to set its path as an argument for the <ins>emploi</ins> object you'll initialize in your file (See steps below).

## Usage

* Import the class into your project :  
```python
from emploi import emploi
```
* In your file, initialize an <ins>emploi</ins> object, set its argument (webdriver) and call its main.
```python
webdriver = 'C:\\Users\\yourusername\\Downloads\\chromedriver_win32\\chromedriver' #Webdriver used here is Chrome's one
a = emploi(webdriver)
jobs = a.main("python") #returns a list of jobs related to "python" in string format in case there are jobs, otherwise an empty list
```
## Demonstration

```python
jobs = a.main("python")
print(jobs)
```
Result in terminal :
```bash
DevTools listening on ws://127.0.0.1:53682/devtools/browser/0cb053a0-b5c4-45b5-a8ff-332f20320503
Développeur Python
Développeur sénior (Web ou Mobile)
Développeur
Software engineer
Développeur Odoo
Développeur DevOps
Développeur DevOps
Développeur Fullstack
Ingénieur Data Scientist
Développeur Machine Learning
Ingénieur de formation junior
Développeur Web et Mobile
End to End Transport Architect Responsible
Développeur Fullstack (systèmes embarqués /AI)
Ingénieur Développement Front-End & Back-End
Ingénieur intégration Systèmes embarqués
```


## Contact
mail : kmedelbachir@gmail.com


  
