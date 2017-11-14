import zipfile
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdate
from matplotlib.backends.backend_pdf import PdfPages

def un_zip(zipfiledir,basedir,zipfilename,figdir):
    #unzip zip file
    zip_file = zipfile.ZipFile(zipfiledir+'.zip')
    if os.path.isdir(zipfiledir):
        pass
    else:
        os.mkdir(zipfiledir)
    
    if os.path.isdir(figdir):
        pass
    else:
        os.mkdir(figdir)
        
    if os.path.isdir(figdir+'/'+zipfilename):
        pass
    else:
        os.mkdir(figdir+'/'+zipfilename)

    for names in zip_file.namelist():
        zip_file.extract(names,zipfiledir)
    zip_file.close()
    

def get_all_file(folder_path):  
    file_list = []  
    if folder_path is None:  
        raise Exception("floder_path is None")  
    for root,dirs,filenames in os.walk(folder_path):  
        for name in filenames:  
            file_list.append(name)  
    return file_list 

def is_file_contain_word(file_list, query_word):  
    for _file in file_list:  
        if query_word in _file and _file[0]!=".":   
            return _file  

file_name=input("Please input the Zip filename: ").upper()
basedir=os.getcwd().split('/Script')[0]
zipfiledir=basedir+'/Data/'+file_name
figdir=basedir+"/"+"Images"
un_zip(zipfiledir,basedir,file_name,figdir)
file_list=get_all_file(zipfiledir)
query_word=["SZ01","SZ02","SZ03","SZ04"]
G=globals()
i=0
for x in query_word:
	i=i+1
	_file=is_file_contain_word(file_list,x)
	path=zipfiledir+'/'+_file
	parser=lambda date:pd.to_datetime(date,format='%a %b %d %H:%M:%S %Z %Y')
	G['sz0'+str(i)+'_data']=pd.read_csv(path,skiprows=[0],header=None,index_col=0,parse_dates=True,date_parser=parser,na_values='-')
#主机温度图
fig1,ax1 = plt.subplots(figsize=(16,4))
ax1.plot_date(sz01_data.index.tolist(),sz01_data[1],'.-',ms=3,linewidth=1,label='Cz13-A')
ax1.plot_date(sz02_data.index.tolist(),sz02_data[1],'.-',ms=3,linewidth=1,label='Cz13-B')
ax1.plot_date(sz03_data.index.tolist(),sz03_data[1],'.-',ms=3,linewidth=1,label='Cz13-C')
ax1.plot_date(sz04_data.index.tolist(),sz04_data[1],'.-',ms=3,linewidth=1,label='Cz13-D')

ax1.xaxis.set_tick_params(rotation=90, labelsize=6,length=2,width=2)
plt.subplots_adjust(bottom=0.3)
plt.yticks(range(0, 30, 2))
plt.ylim(0,30)
plt.legend(bbox_to_anchor=(1.005, 1), loc=2, borderaxespad=0.)
plt.xlim(min(sz01_data.index.tolist()),max(sz01_data.index.tolist()))
ax1.xaxis.set_major_locator(mdate.HourLocator(interval=3))
ax1.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d %H:%M'))
plt.xlabel('Time (Hour)')
plt.ylabel('Temperature (°C)')
plt.title('Mainframe Temperature')
plt.grid(True)
plt.savefig(figdir+'/'+file_name+"/Temperature.png")
#主机Power图
fig2,ax2 = plt.subplots(figsize=(16,4))
ax2.plot_date(sz01_data.index.tolist(),sz01_data[3],'.-',ms=3,linewidth=1,label='Cz13-A')
ax2.plot_date(sz02_data.index.tolist(),sz02_data[3],'.-',ms=3,linewidth=1,label='Cz13-B')
ax2.plot_date(sz03_data.index.tolist(),sz03_data[3],'.-',ms=3,linewidth=1,label='Cz13-C')
ax2.plot_date(sz04_data.index.tolist(),sz04_data[3],'.-',ms=3,linewidth=1,label='Cz13-D')
plt.legend(bbox_to_anchor=(1.005, 1), loc=2, borderaxespad=0.)
ax2.xaxis.set_tick_params(rotation=90, labelsize=6,length=2,width=2)
plt.subplots_adjust(bottom=0.3)
plt.yticks(range(0, 30, 2))
plt.ylim(0,30)
plt.xlim(min(sz01_data.index.tolist()),max(sz01_data.index.tolist()))
ax2.xaxis.set_major_locator(mdate.HourLocator(interval=3))
ax2.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d %H:%M'))
plt.xlabel('Time (Hour)')
plt.ylabel('Power (KW)')
plt.title('Mainframe Power')
plt.grid(True)
plt.savefig(figdir+'/'+file_name+"/Power.png")
#主机CP utilization图
fig3,ax3 = plt.subplots(figsize=(16,4))
ax3.plot_date(sz01_data.index.tolist(),sz01_data[5],'.-',ms=3,linewidth=1,label='Cz13-A')
ax3.plot_date(sz02_data.index.tolist(),sz02_data[5],'.-',ms=3,linewidth=1,label='Cz13-B')
ax3.plot_date(sz03_data.index.tolist(),sz03_data[5],'.-',ms=3,linewidth=1,label='Cz13-C')
ax3.plot_date(sz04_data.index.tolist(),sz04_data[5],'.-',ms=3,linewidth=1,label='Cz13-D')
plt.legend(bbox_to_anchor=(1.005, 1), loc=2, borderaxespad=0.)
ax3.xaxis.set_tick_params(rotation=90, labelsize=6,length=2,width=2)
plt.subplots_adjust(bottom=0.3)
plt.yticks(range(0, 110, 10))
plt.ylim(0,100)
plt.xlim(min(sz01_data.index.tolist()),max(sz01_data.index.tolist()))
ax3.xaxis.set_major_locator(mdate.HourLocator(interval=3))
ax3.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d %H:%M'))
plt.xlabel('Time (Hour)')
plt.ylabel('CPU utlization (%)')

plt.title('Mainframe CPU utiliaztion')
plt.grid(True)

plt.savefig(figdir+'/'+file_name+"/CPU_utlization.png")
plt.show()

