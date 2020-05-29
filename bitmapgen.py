import csv

scp_version = 'MAB000125'

with open('failure.cvs', 'w', newline='') as fail:
    fieldnames = ['Failurebitmapof' + scp_version]
    DictWriter = csv.DictWriter(fail, fieldnames=fieldnames)

