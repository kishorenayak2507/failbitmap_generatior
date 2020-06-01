# importing required modules
import xmltodict
import json
import csv
from zipfile import ZipFile
import tkinter as tk
from tkinter import simpledialog
from tkinter import Button
ROOT = tk.Tk()
ROOT.withdraw()
ROOT.geometry('300x100')
ROOT.title('Failure_bitmap')
def export_cvs():
    Export_cvs_file()
def failure_request():
    failure_name = simpledialog.askstring(title="Failure_bitmap", prompt="failure_name:")
    find_failure_byname(failure_name)
def genericid_request():
    Generic_id = simpledialog.askstring(title="Failure_bitmap", prompt="Generic ID")
    find_failure_byID(Generic_id)

# the input dialog
SW_version = simpledialog.askstring(title="Failure_bitmap", prompt="SCP(Software check point):",)
failure_button = Button(ROOT, text='failure_name', Command=failure_request).grid(row=4, column=0)
generic_button = Button(ROOT, text='generic_id', Command=genericid_request).grid(row=8, column=0)
export_cvs_file = Button(ROOT, text='export_failure_bitmap', Command=failure_request).grid(row=12, column=0)
ROOT.mainloop()
# check it out
print("sw_VERSION", SW_version)
# SW_version = '2U3CG000007'
SW_version_file = SW_version+'_SW_VERSION.zip'
# specifying the zip file name
# failure_name = 'Bus_sig_speed_adjust_state'
# Generic_id = '0x261D'
file_name = "D://Phy_learn//zip_file_stored//"+SW_version_file
# opening the zip file in READ mode
def find_failure_byname(name):
    for entry in doc['FailureBits']['FailureBit']:
        if name == entry['FailureBitName']:
            print('word =\t' + entry['FailureBitDynAddress']['FailureBitDynAddressWord'])
            print('Bit =\t' + entry['FailureBitDynAddress']['FailureBitDynAddressBit'])
            print('Generic ID =\t' + entry['FailureBitGenericData']['FailureBitGenericDataID'])
def find_failure_byID(gen_ID):
    for entry in doc['FailureBits']['FailureBit']:
        if gen_ID == entry['FailureBitGenericData']['FailureBitGenericDataID']:
            print('word =\t' + entry['FailureBitDynAddress']['FailureBitDynAddressWord'])
            print('Bit =\t' + entry['FailureBitDynAddress']['FailureBitDynAddressBit'])
            print('Failure Name =\t' + entry['FailureBitName'])
with ZipFile(file_name, 'r') as zip:
    # printing all the contents of the zip file
    # zip.printdir()
    # extracting all the files
    # print('Extracting xml the file now...')
    zip.extract('DOCUMENTATION/'+SW_version+'_dynamic_failure_bit_documentation_customer.xml')
    # print('Done!')
with open('DOCUMENTATION/'+SW_version+'_dynamic_failure_bit_documentation_customer.xml') as fd:
    doc = xmltodict.parse(fd.read())
# full_json_string = json.dumps(doc, indent=4)
# print(full_json_string)
# now we will open a file for writing
def Export_cvs_file():
    Csv_file_name = 'failure_bitmap_' + SW_version
    data_file = open(Csv_file_name + '.csv', 'w', newline='')
    csv_writer = csv.writer(data_file)
    count = 0
    for fail in doc['FailureBits']['FailureBit']:
       if count == 0:
        # Writing headers of CSV file
        Header_fields = ["FailureBitName", "FailureBitDynAddressWord", "FailureBitDynAddressBit", "FailureBitGenericDataID"]
        csv_writer.writerow(Header_fields)
        count += 1
    # Writing data of CSV file
    fail_fields = [fail['FailureBitName'], fail['FailureBitDynAddress']['FailureBitDynAddressWord'], fail['FailureBitDynAddress']['FailureBitDynAddressBit'], fail['FailureBitGenericData']['FailureBitGenericDataID']]
    csv_writer.writerow(fail_fields)
    data_file.close()



