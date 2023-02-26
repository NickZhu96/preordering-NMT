#H_sort.py test.result.H test.result.H.split test.result.T.split

import sys
argc=int(len(sys.argv))
f_H = open(sys.argv[1])
f_Hs = open(sys.argv[2])
f_Ts = open(sys.argv[3])

all_data=[]
H_lines = f_H.readlines()
Hs_lines = f_Hs.readlines()
Ts_lines = f_Ts.readlines()
for H_line, Hs_line, Ts_line in zip(H_lines, Hs_lines, Ts_lines):
  line_num = int(H_line.split()[0].split("-")[1])
  cur_data = (line_num, Hs_line, Ts_line)
  all_data.append(cur_data)

all_data.sort(key=lambda x:x[0])
fw_Hs = open(sys.argv[2]+".sort", "w")
fw_Ts = open(sys.argv[3]+".sort", "w")
for sorted_data in all_data:
  fw_Hs.write(sorted_data[1])
  fw_Ts.write(sorted_data[2])

f_H.close()
f_Hs.close()
f_Ts.close()
fw_Hs.close()
fw_Ts.close()
