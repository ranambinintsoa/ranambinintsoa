- 👋 Hi, I’m @ranambinintsoa
- 👀 I’m interested in ...
- 🌱 I’m currently learning ...
- 💞️ I’m looking to collaborate on ...
- 📫 How to reach me ...
- 😄 Pronouns: ...
- ⚡ Fun fact: ...

<!---
ranambinintsoa/ranambinintsoa is a ✨ special ✨ repository because its `README.py` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->
import pandas as pd
import requests
from bs4 import BeautifulSoup
import csv
import matplotlib.pyplot as plt

keywords = ['STATISTICS', 'STATISTICAL', 'INFECTIOUS', 'EPIDEMIC','ENGINEER' , 'ENGINEERING' , 'FINANCE']
Organisation , Duty_Station , Level_Grade , Contract_Type = [] , [] ,[] ,[] 
Post_Title, Reference , Closing_Date , Posting_Retrieved = [] ,[] ,[], []
voit_details ={}
url = "https://unjoblist.org/lists/Organisation/all/"
for page in range(1,6):
    
    response = requests.get(url + str(page))
    if response.status_code == 200:

        soup = BeautifulSoup(response.text, 'html.parser')

        job_listings = soup.find_all('tr')
        
        count = 0
        for job in job_listings:

            data = [td.text.strip() for td in job.find_all('td')]
            
            here = soup.select('a[href^="https://unjoblist.org/vacancy/"]')
            list_here = list(here)
            if count > 0:

                Organisation.append(data[0])
                Duty_Station.append(data[1])
                Level_Grade.append(data[2])
                Contract_Type.append(data[3])
                Post_Title.append(data[4])
                Reference.append(str(list_here[count-1])[9:46])
                Closing_Date.append(data[5])
                Posting_Retrieved.append(data[6])
                
            count += 1
        


url_secod = "https://unjoblist.org/results.php?kw=&org%5B%5D=All+organisation+on+UN+Job+List%3A&dts=&ics1=&ics2=&O2=yes&Job=Search"
response1 = requests.get(url_secod)    
soup1 = BeautifulSoup(response1.text, 'html.parser')
job_listings = soup1.find_all('td')
    
here_1 = soup1.select('a[href^="https://unjoblist.org/r/"]')
l_here = len(here_1)
list_here_1 = []
for i in range(l_here):
    list_here_1.append(str(here_1[i])[9:40])

data1 = [td.text.strip() for td in job_listings]
k = int(len(data1))
for i in range(0 , k):
    if (6+i)*6 < k:
        Organisation.append(data1[i * 6])
        Duty_Station.append(data1[i* 6 + 1])
        Level_Grade.append(data1[i*6 + 2])
        Contract_Type.append("--")
        Post_Title.append(data1[i*6 + 3])
        Reference.append(list_here_1[i])
        Closing_Date.append(data1[i*6 + 4])
        Posting_Retrieved.append(data1[5 + 6*i])


url_3 = "https://unjoblist.org/results.php?kw=&org%5B%5D=All+organisation+on+UN+Job+List%3A&dts=&ics1=&ics2=&O1=yes&Job=Search"
response2 = requests.get(url_3)    
soup2 = BeautifulSoup(response2.text, 'html.parser')
job_listings_2 = soup2.find_all('td')
data2 = [td.text.strip() for td in job_listings_2]
here_2 = soup2.select('a[href^="https://unjoblist.org/r/"]')
l_here_2 = len(here_2)
list_here_2 = []
for i in range(l_here):
    list_here_2.append(str(here_2[i])[9:40])
k = int(len(data2))
for i in range(0 , k):
    if (6+i)*6 < k:
        Organisation.append(data2[i * 6])
        Duty_Station.append(data2[i* 6 + 1])
        Level_Grade.append(data2[i*6 + 2])
        Contract_Type.append("--")
        Post_Title.append(data2[i*6 + 3])
        Reference.append(list_here_2[i])
        Closing_Date.append(data2[i*6 + 4])
        Posting_Retrieved.append(data2[5 + 6*i])

voit_details['Organisation'] = Organisation 
voit_details['Duty Station'] =Duty_Station 
voit_details['Level Grade'] = Level_Grade 
voit_details['Contract Type'] = Contract_Type 
voit_details['Post Title'] = Post_Title 
voit_details['Link'] = Reference
voit_details['Closing Date'] = Closing_Date 
voit_details['Posting Retrieved'] = Posting_Retrieved 
df1 = pd.DataFrame(voit_details)
df1.to_csv("ALL_DATA.csv", index=False)

out = len(Organisation)

t , t1 , t2 ,t3 ,t4 , t5 = 0 , 0 ,0 ,0 ,0 , 0
Organisation_1 , Duty_Station_1 , Level_Grade_1 , Contract_Type_1 = [] , [] ,[] ,[] 
Post_Title_1, Reference_1 , Closing_Date_1 , Posting_Retrieved_1 = [] ,[] ,[], []
voit_details_1 = {}
for i in range(0 , out):
    split_data_4 = Post_Title[i].upper().split()
    for key in keywords:
        if key in split_data_4:
            Organisation_1.append(Organisation[i])
            Duty_Station_1.append(Duty_Station[i])
            Level_Grade_1.append(Level_Grade[i])
            Contract_Type_1.append(Contract_Type[i])
            Post_Title_1.append(Post_Title[i])
            Reference_1.append(Reference[i])
            Closing_Date_1.append(Closing_Date[i])
            Posting_Retrieved_1.append(Posting_Retrieved[i])
            if key == 'STATISTICS' or key == 'STATISTICAL':
                t1 = t1 + 1
            elif key == 'INFECTIOUS':
                t2 = t2 + 1
            elif key =='EPIDEMIC':
                t3 = t3 + 1
            elif key =='FINANCE':
                t4 = t4 + 1
            elif key =='ENGINEERING' or key == 'ENGINEER':
                t5 = t5 + 1
            break

list_1 = [ t1 , t2 , t3 , t4 , t5]
list_2 = [ 'STATISTICS', 'INFECTIOUS','EPIDEMIC', 'FINANCE',  'ENGINEER']
voit_details_1['Organisation'] = Organisation_1 
voit_details_1['Duty Station'] =Duty_Station_1 
voit_details_1['Level_Grade'] = Level_Grade_1 
voit_details_1['Contract_Type'] = Contract_Type_1 
voit_details_1['Post_Title'] = Post_Title_1 
voit_details_1['Link'] = Reference_1
voit_details_1['Closing_Date'] = Closing_Date_1 
voit_details_1['Posting_Retrieved'] = Posting_Retrieved_1 
df2 = pd.DataFrame(voit_details_1)
df2.to_csv("projet_final_output.csv", index=False)

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os


def send_email(email_list, csv_file_path):
    text = MIMEMultipart()
    text['From'] = 'marka.ranambinintsoa@aims.ac.rw'
    text['To'] = ', '.join(email_list)
    text['Subject'] = 'Data Science Weeb scraping for Job Updates from GROUP 8'
    
    with open(csv_file_path, 'rb') as f:
        part = MIMEApplication(f.read(), _subtype='csv')
        part.add_header('content-disposition', 'attachment', filename=os.path.basename(csv_file_path))
        text.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('marka.ranambinintsoa@aims.ac.rw', '1234')
    server.sendmail('adiza.sandah@aims.ac.rw', email_list, text.as_string())
    server.sendmail('mariama.jammeh@aims.ac.rw', email_list, text.as_string())
    server.sendmail('miujiza.zirimwabagabo@aims.ac.rw', email_list, text.as_string())
    server.sendmail('miujiza.zirimwabagabo@aims.ac.rw', email_list, text.as_string())
    server.quit()
