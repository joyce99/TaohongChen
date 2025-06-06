import matplotlib.pyplot as plt
import matplotlib
import numpy as np
matplotlib.use('TkAgg')
matplotlib.rcParams['font.family'] = 'Times New Roman'  # 字体名称
# matplotlib.rcParams['font.style'] = 'italic'            # 字体样式（可选）

color1="#449945"
color2="#304f9e"
color3="#740099"
color4="#f23b27"
# 创建一个大图和四个子图
label1= "T1"#'C'+'\u2192'+'D'
label2= "U" #'A'+'\u2192'+'D'
label3= "S"#'B1'+'\u2192'+'B2'
label4= "H"#'Co1'+'\u2192'+'Co2'

'''AWA2中扩展属性个数k'''
x1=[0,5,10,15,20]
y1=[60,65,70,75,80,85]
plt.plot(x1, [70.6,74.9,73.2,73.7,71.6],color=color1,marker='^', markersize=6,label=label1)
plt.plot(x1, [64.8,70.4,68.4,68.9,63.6],color=color2,marker='s', markersize=6,label=label2)
plt.plot(x1, [75.7,83.7,80.5,81.4,78.4],color=color3,marker='o', markersize=6,label=label3)
plt.plot(x1, [69.8,76.5,74.0,74.6,70.2],color=color4,marker='*', markersize=6,label=label4)
plt.xticks(x1,fontsize=14)
plt.xlabel("k",fontsize=16)
plt.yticks(y1,fontsize=14)
plt.ylabel("Accuracy (%)",fontsize=16)
plt.legend()
plt.tight_layout()
# plt.savefig('Numbers_of_samples_AWA2.eps', format='eps')
plt.show()

'''CUB中扩展属性个数k'''
# x1=[0,5,10,15,20]
# y1=[60,65,70,75,80,85]
# plt.plot(x1, [72.3,78.4,82.7,77.5,73.7],color=color1,marker='^', markersize=6,label=label1)
# plt.plot(x1, [61.4,66.3,68.7,64.2,62.7],color=color2,marker='s', markersize=6,label=label2)
# plt.plot(x1, [73.6,77.6,78.4,75.7,74.5],color=color3,marker='o', markersize=6,label=label3)
# plt.plot(x1, [66.9,71.5,73.2,69.5,68.1],color=color4,marker='*', markersize=6,label=label4)
# plt.xticks(x1,fontsize=14)
# plt.xlabel("k",fontsize=16)
# plt.yticks(y1,fontsize=14)
# plt.ylabel("Accuracy (%)",fontsize=16)
# plt.legend()
# plt.tight_layout()
# # plt.savefig('Numbers_of_samples_AWA2.eps', format='eps')
# plt.show()

'''SUN中扩展属性个数k'''
# x1=[0,5,10,15,20]
# y1=[40,45,50,55,60,65]
# plt.plot(x1, [61.4,65.2,67.3,63.6,61.8],color=color1,marker='^', markersize=6,label=label1)
# plt.plot(x1, [45.8,48.7,53.5,50.3,49.1],color=color2,marker='s', markersize=6,label=label2)
# plt.plot(x1, [56.9,57.1,58.7,56.2,55.7],color=color3,marker='o', markersize=6,label=label3)
# plt.plot(x1, [50.8,52.6,56.0,53.1,52.2],color=color4,marker='*', markersize=6,label=label4)
# plt.xticks(x1,fontsize=14)
# plt.xlabel("k",fontsize=16)
# plt.yticks(y1,fontsize=14)
# plt.ylabel("Accuracy (%)",fontsize=16)
# plt.legend()
# plt.tight_layout()
# # plt.savefig('Numbers_of_samples_AWA2.eps', format='eps')
# plt.show()