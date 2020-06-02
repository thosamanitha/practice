import matplotlib.pyplot as plt
import numpy as m
import requests
from bs4 import BeautifulSoup

with open("covid19.html") as fp:
	html_soup=BeautifulSoup(fp)
table_containers=html_soup.table.tbody.find_all('tr')


print("\n")


s_no=[]
names=[]
indian_confirmed_cases=[]
cured=[]
death=[]
active=[]

c=0

 
for container in table_containers:

	
	if c<35:
	
		name=container.find_all('td')	
		s_no.append(name[0].text)
		names.append(name[1].text)
		active.append(name[2].text)
		cured.append(name[3].text)
		indian_confirmed_cases.append(name[-1].text)
		death.append(name[-2].text)
		c=c+1
		
		

print("-"*124)
print()
print("| {:^10} | {:<35} | {:^20} | {:^10} | {:^20} | {:^10} |".format("S.No","States","Active cases","Cured","Confirmed cases","Deaths"))
print()
print("-"*124)
for i in range(0,len(s_no)):
        data="| {:^10} | {:<35} | {:^20} | {:^10} | {:^20} | {:^10} |".format(s_no[i],names[i],active[i].strip(),cured[i].strip(),indian_confirmed_cases[i],death[i].strip())
        print(data)
print("-"*124)

print("\n")
	


names=["AP", "Delhi", "Haryana", "Karnataka", "Kerala", "  Maharastra","Odisha","Punjab ","Rajasthan","Tamil\nNadu","Telangana"]
value=[3171, 14465, 1305, 2283, 963, 54758, 1517, 2106, 7536, 17728,1991]

def pie_chart():

	plt.pie(value,labels=names, autopct='%1.0f%%', startangle=90)
	plt.title('States & Confirmed Cases',color='blue',weight='bold')
	plt.legend()
	plt.axis('equal')
	plt.show()


def bar_graph():

	names_bar=["AP", "Delhi", "Haryana", "Karnataka", "Kerala", "  Maharastra","Odisha","Punjab ","Rajasthan","Tamil\nNadu","Telangana","J&K","UP","UK","West\nBengal","Gujarat"]
	value_bar=[3171, 14465, 1305, 2283, 963, 54758, 1517, 2106, 7536, 17728, 1991, 1759,  6548, 401, 4009,14821]
	plt.title('States & Confirmed Cases',color='blue',weight='bold')
	plt.xlabel('Names of States',color='purple',weight='bold')
	plt.ylabel('Confirmed Cases',color='purple',weight='bold')
	plt.barh(names_bar,value_bar)
	plt.show()



def comparison_graph():

	n_groups = 16
	cured=(2009,7223,1305,2283,542,16954,733,1918,4171,9342,1284,833,3698,64,1486,7139)
	deaths=(57,288,17,44,6,1792,7,40,170,127,57,24,170,4,283,915)

	fig, ax = plt.subplots()
	index = m.arange(n_groups)
	bar_width = 0.35
	opacity = 0.8

	rects1 = plt.bar(index, cured, bar_width,
	alpha=opacity,
	color='orange',label='Cured cases')

	rects2 = plt.bar(index + bar_width, deaths, bar_width,
	alpha=opacity,
	color='g',label='Deaths')
	plt.title('Cured cases and Deaths',color='blue',weight='bold')
	
	plt.xticks(index + bar_width, ('AP','Delhi','Haryana','Karnataka','kerala','Maharastra','Odisha','Punjab','Rajastan','Tamil\nnadu','Telangana','J&K','Ladakh','UP','UK','WB'))
	plt.xlabel('Names of States',color='purple',weight='bold')
	plt.ylabel('Cured cases and Deaths',color='purple',weight='bold')
	plt.tight_layout()
	plt.legend()
	plt.show(rects1)
	plt.show(rects2)

pie_chart()
bar_graph()
comparison_graph()

