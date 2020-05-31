# Creating a Csv file
"""


scp_version = 'MAB000125'

with open('failure.csv', 'w', newline='') as fail:
    fieldnames = ['Failurebitmapof' + scp_version]
    DictWriter = csv.DictWriter(fail, fieldnames=fieldnames)
"""
# importing required modules
import xmltodict
import json
import csv
from zipfile import ZipFile
SW_version = '2U3CG000007'
SW_version_file = SW_version+'_SW_VERSION.zip'
# specifying the zip file name
failure_name = 'Bus_sig_speed_adjust_state'
Generic_id = '0x261D'
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
find_failure_byname(failure_name)
find_failure_byID(Generic_id)

# now we will open a file for writing
data_file = open('failure_bitmap.csv', 'w')
csv_writer = csv.writer(data_file)
count = 0
for emp in doc['FailureBits']['FailureBit']:
    if count == 0:
        # Writing headers of CSV file
        header = emp.keys()
        csv_writer.writerow(header)
        count += 1

    # Writing data of CSV file
    csv_writer.writerow(emp.values())

data_file.close()