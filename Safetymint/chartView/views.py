from calendar import calendar, month, month_abbr
import re
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
import openpyxl

from datetime import datetime



def upload_file_view(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            data_set=handle_uploaded_file(request.FILES['file'])
            
            return render(request,"<h1>OKAY</h1>",{})
            #return render(request,"chart.html",{data_set})
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})



def Month_Name_Using_Date(date):
    d = datetime.strptime(date,'%d-%b-%y')
    Month_name=d.strftime('%b-%y')
    return Month_name

def handle_uploaded_file(file):
    
    wb=openpyxl.load_workbook(file)
    sheet_obj=wb.active
    
    data_dict={}
    rowCount=sheet_obj.max_row
    colCount=sheet_obj.max_column

    for i in range(2,rowCount+1):
        cell_date=datetime.strftime(sh.cell(row=i,column=2).value,"%b-%y")
        cell_type=sh.cell(row=i,column=3).value
        if cell_date not in data_dict:
            data_dict[cell_date]={"Minor":0,"Serious":0,"Critical":0}
        data_dict[cell_date][cell_type]+=1

        

    return data_dict

def chartdisp(li):
    
    return