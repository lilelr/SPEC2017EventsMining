import os
import pickle
import numpy as np
import pandas as pd
import csv
from sklearn import preprocessing

output_name = "it-65.csv"
output_path = "/Users/yuxiao/Lab/projects/SPEC-CPU2017/508-name-d/namd_r_base.myt-result/"
input_path = "/Users/yuxiao/Lab/projects/SPEC-CPU2017/508-name-d/namd_r_base.myt-result/it-65/"

set_events_name = {}
first_line = 'index'
set_events = open("/Users/yuxiao/Lab/projects/SPEC-CPU2017/资料/sethaswell-e.csv", "r")
# csv_reader = csv.reader(set_events)
# for code,name in csv_reader:
#     print(code,name)
for line in set_events:
    line_items = line.split(',')
    #     print(line_items[1])
    first_line += (',' + line_items[1])
set_events.close()
first_line += (',IPC')

print(first_line)

input_file_name = "namd_r_base.myt_it-65_"
output_file_path = output_path + output_name
output_table = open(output_file_path, 'w')
output_table.write(first_line + '\n')

total = 1
for i in range(1, 60):
    input_file_path = input_path + input_file_name + str(i) + ".csv"
    print(input_file_path)
    input_file = open(input_file_path, 'r')
    ignore = 1
    for temp_line in input_file:
        if ignore <= 2:
            ignore += 1
            continue
        temp_line_items = temp_line.split(',')
        if str(temp_line_items[1]) == '<not counted>':
            break
        else:
            cycles = float(temp_line_items[1])

        temp_line = input_file.readline()
        temp_line_items = temp_line.split(',')
        if str(temp_line_items[1]) == '<not counted>':
            break
        else:
            instructions = float(temp_line_items[1])
        ipc = instructions / cycles

        temp_line = input_file.readline()
        temp_line_items = temp_line.split(',')
        if str(temp_line_items[1]) == '<not counted>':
            break
        else:
            event_1 = temp_line_items[1]

        temp_line = input_file.readline()
        temp_line_items = temp_line.split(',')
        if str(temp_line_items[1]) == '<not counted>':
            break
        else:
            event_2 = temp_line_items[1]

        final_list = []
        for k in range(236):
            final_list.append('0')
        start_index = 4 * i - 3
        final_list[0] = str(total)
        total += 1

        final_list[235] = str(ipc)

        if i == 59:
            data = pd.Series([event_1, event_2])
            scale_data = preprocessing.scale(data)
            #         print(scale_data)
            final_list[start_index] = str(scale_data[0])
            final_list[start_index + 1] = str(scale_data[1])
            join_flag = ','
            final_line = join_flag.join(final_list)
            output_table.write(final_line + '\n')
            continue

        temp_line = input_file.readline()
        temp_line_items = temp_line.split(',')
        if str(temp_line_items[1]) == '<not counted>':
            break
        else:
            event_3 = temp_line_items[1]

        temp_line = input_file.readline()
        temp_line_items = temp_line.split(',')
        if str(temp_line_items[1]) == '<not counted>':
            break
        else:
            event_4 = temp_line_items[1]

        data = pd.Series([event_1, event_2, event_3, event_4])
        try:
            scale_data = preprocessing.scale(data)
        except:
            print("file", i)

        # print(scale_data)
        final_list[start_index] = str(scale_data[0])
        final_list[start_index + 1] = str(scale_data[1])
        final_list[start_index + 2] = str(scale_data[2])
        final_list[start_index + 3] = str(scale_data[3])
        join_flag = ','
        final_line = join_flag.join(final_list)
        output_table.write(final_line + '\n')

output_table.close()
#         print(instructions,cycles,ipc,event_1,event_2,event_3,event_4)
