import os
from beautifultable import BeautifulTable

from layout_parser import LayoutParser

# Get Android project path and navigate to it
script_dir = os.getcwd()

cwd = input("Enter android project path: ")
os.chdir(f"{cwd}/app/src/main/res/layout")
dirs = os.listdir()

# Parse all layout files and get individual counters for each file
counters = []

for file_name in dirs:
    lp = LayoutParser(file_path=file_name)
    counters.append(lp.get_counter())

# Calculate final result based on all counters
resultDic = {}

for counterDic in counters:
    for key in counterDic.keys():
        if key in resultDic.keys():
            resultDic[key] += counterDic[key]
        else:
            resultDic[key] = counterDic[key]

# Sort results
sorted_list = sorted(resultDic.items(), key=lambda dic_item: dic_item[1], reverse=True)
# print(sorted_list)

# Create table
table = BeautifulTable()
table.columns.header = ["Name", "Count"]
for item in sorted_list:
    table.rows.append([item[0], item[1]])

# Save table to file
os.chdir(script_dir)
with open("result.txt", mode="w") as result_file:
    result_file.write(str(table))

# Print table
print(table)
print("\n")
print("Check analysis in 'result.txt'")
