'''
This is how you write csv files
'''

import os
import csv

output_path = os.path.join('.','new.csv')

with open(output_path,'w') as my_file:
    my_writer = csv.writer(my_file)

    my_writer.writerow(['id,''Name','SSN'])
    my_writer.writerow(['1,''Santiago','12345'])
    my_writer.writerow(['2,''Lu','6788'])
    my_writer.writerow(['3,''Mau','91083'])

    