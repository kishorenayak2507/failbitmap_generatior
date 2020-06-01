# importing required modules
import xmltodict
import json
import csv
from zipfile import ZipFile
# Backend file for zip extraction , failure search and csvexport
# check it out
# print("sw_VERSION", sw_version)
# SW_version = '2U3CG000007'

# specifying the zip file name
# failure_name = 'Bus_sig_speed_adjust_state'
# Generic_id = '0x261D'
# opening the zip file in READ mode
def find_failure_byname(name, sname):
    extract_file_inlocation(sname)
    with open('DOCUMENTATION/' + sname + '_dynamic_failure_bit_documentation_customer.xml') as fd:
        doc = xmltodict.parse(fd.read())
    for entry in doc['FailureBits']['FailureBit']:
        if name == entry['FailureBitName']:
            return 'True', entry['FailureBitDynAddress']['FailureBitDynAddressWord'], entry['FailureBitDynAddress']['FailureBitDynAddressBit'], entry['FailureBitGenericData']['FailureBitGenericDataID']
            # print('word =\t' + entry['FailureBitDynAddress']['FailureBitDynAddressWord'])
            # print('Bit =\t' + entry['FailureBitDynAddress']['FailureBitDynAddressBit'])
            # print('Generic ID =\t' + entry['FailureBitGenericData']['FailureBitGenericDataID'])


def find_failure_byID(gen_ID,swname):
    extract_file_inlocation(swname)
    with open('DOCUMENTATION/' + swname + '_dynamic_failure_bit_documentation_customer.xml') as fd:
        doc = xmltodict.parse(fd.read())
        # print(doc['FailureBits']['FailureBit'][0])
    for entry in doc['FailureBits']['FailureBit']:
        # print(entry['FailureBitGenericData']['FailureBitGenericDataID'])
        if gen_ID == entry['FailureBitGenericData']['FailureBitGenericDataID']:
            return 'True', entry['FailureBitName'], entry['FailureBitDynAddress']['FailureBitDynAddressWord'], entry['FailureBitDynAddress']['FailureBitDynAddressBit']
            # print('word =\t' + entry['FailureBitDynAddress']['FailureBitDynAddressWord'])
            # print('Bit =\t' + entry['FailureBitDynAddress']['FailureBitDynAddressBit'])
            # print('Failure Name =\t' + entry['FailureBitName'])

def extract_file_inlocation(sversion):
    SW_version_file = sversion + '_SW_VERSION.zip'
    file_name = "D://Phy_learn//zip_file_stored//" + SW_version_file
    with ZipFile(file_name, 'r') as zip:
        zip.extract('DOCUMENTATION/' + sversion + '_dynamic_failure_bit_documentation_customer.xml')
    # printing all the contents of the zip file
    # zip.printdir()
    # extracting all the files
    # print('Extracting xml the file now...')
    # print('Done!')
# full_json_string = json.dumps(doc, indent=4)
# print(full_json_string)
# now we will open a file for writing
def Export_csv_file(sversion):
    extract_file_inlocation(sversion)
    with open('DOCUMENTATION/' + sversion+ '_dynamic_failure_bit_documentation_customer.xml') as fd:
        doc = xmltodict.parse(fd.read())
    Csv_file_name = 'failure_bitmap_' + sversion
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




