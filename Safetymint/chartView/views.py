from calendar import calendar, month, month_abbr
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
            
            
            return render(request,"chart.html",)
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})



def Month_Name_Using_Date(date):
    d = datetime.strptime(date,'%d-%b-%y')
    Month_name=d.strftime('%b')
    return Month_name

def handle_uploaded_file(file):
    
    # wb=openpyxl.load_workbook(file)
    # sheet_obj=wb.active
    
    # data_dict={}
    # for i in range(1,13):
    #     data_dict[month_abbr[i%12 ]]={}
    
    # types_of_severity=["Minor","Serious","Critical"]
    
    # for i in data_dict:
    #     for j in types_of_severity:
    #         data_dict[i][j]=0

    # row = sheet_obj.max_row
    # column = sheet_obj.max_column

    # for i in range(2, row + 1): 
    #     d = Month_Name_Using_Date(sheet_obj.cell(row = i, column = 2))
    #     severity = sheet_obj.cell(row = i, column = 3)
    #     data_dict[d][severity]+=1

        

    return

def chartdisp(li):
    
    return