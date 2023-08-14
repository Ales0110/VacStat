import requests
from datetime import datetime
from openpyxl import load_workbook

time = datetime.now().date()

url_devops = 'https://api.rabota.by/vacancies?per_page=100&text=DevOps&area=1002&area=2237&show_region=true'
url_sysadm = 'https://api.rabota.by/vacancies?per_page=100&text=Системный%20администратор&area=1002&area=2237&show_region=true'

devops_str = requests.get(url_devops).json()
sysadm_str = requests.get(url_sysadm).json()

devops = devops_str['found']
sysadm = sysadm_str['found']

print('Количество вакансий DevOps на', time, ":", str(devops))
print('Количество вакансий Системный администратор на', time, ":", str(sysadm))

fn = 'Стата.xlsx'
wb = load_workbook(fn)
ws = wb['data']
ws.append([time,devops,sysadm])
wb.save(fn)
wb.close()