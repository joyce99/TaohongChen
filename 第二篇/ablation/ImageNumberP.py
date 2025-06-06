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

'''AWA2中挑选图像个数的图'''
# x1=[5,6,7,8,9,10,11,12,13,14,15]
# y1=[60,65,70,75,80,85]
# plt.plot(x1, [64.9,65.6,66.3,68.4,72.5,74.3,74.9,73.8,71.5,69.7,66.3],color=color1,marker='^', markersize=6,label=label1)
# plt.plot(x1, [62.8,63.7,63.9,64.2,69.3,70.2,70.4,69.8,67.5,67.1,63.8],color=color2,marker='s', markersize=6,label=label2)
# plt.plot(x1, [66.2,67.3,68.5,70.6,75.9,81.6,83.7,82.4,78.1,78.5,74.6],color=color3,marker='o', markersize=6,label=label3)
# plt.plot(x1, [64.5,65.5,66.1,67.2,72.5,75.5,76.5,75.6,72.4,72.4,68.8],color=color4,marker='*', markersize=6,label=label4)
# plt.xticks(x1,fontsize=14)
# plt.xlabel("p",fontsize=16)
# plt.yticks(y1,fontsize=14)
# plt.ylabel("Accuracy (%)",fontsize=16)
# plt.legend()
# plt.tight_layout()
# # plt.savefig('Numbers_of_samples_AWA2.eps', format='eps')
# plt.show()

'''CUB中挑选图像个数的图'''
# x1=[5,6,7,8,9,10,11,12,13,14,15]
# y1=[60,65,70,75,80,85]
# plt.plot(x1, [74.5,77.3,80.6,82.7,81.9,81.2,80.3,78.8,76.3,76.4,75.6],color=color1,marker='^', markersize=6,label=label1)
# plt.plot(x1, [65.2,66.8,67.4,68.7,68.4,67.7,67.3,66.1,64.8,63.7,64.0],color=color2,marker='s', markersize=6,label=label2)
# plt.plot(x1, [80.1,78.3,79.6,78.4,78.1,78.2,77.5,75.4,74.3,75.8,76.4],color=color3,marker='o', markersize=6,label=label3)
# plt.plot(x1, [71.9,72.1,73.0,73.2,72.9,72.6,72.0,70.4,69.2,69.2,69.7],color=color4,marker='*', markersize=6,label=label4)
# plt.xticks(x1,fontsize=14)
# plt.xlabel("p",fontsize=16)
# plt.yticks(y1,fontsize=14)
# plt.ylabel("Accuracy (%)",fontsize=16)
# plt.legend()
# plt.tight_layout()
# # plt.savefig('Numbers_of_samples_AWA2.eps', format='eps')
# plt.show()

'''SUN中挑选图像个数的图'''
x1=[5,6,7,8,9,10,11,12,13,14,15]
y1=[35,40,45,50,55,60,65]
plt.plot(x1, [48.9,50.5,54.6,60.4,64.9,67.3,66.4,63.1,62.4,60.7,59.4],color=color1,marker='^', markersize=6,label=label1)
plt.plot(x1, [38.0,41.4,43.8,45.7,50.1,53.5,53.1,50.4,48.7,48.9,47.3],color=color2,marker='s', markersize=6,label=label2)
plt.plot(x1, [46.3,47.8,49.3,50.3,54.2,58.7,58.5,56.8,54.2,55.7,53.4],color=color3,marker='o', markersize=6,label=label3)
plt.plot(x1, [41.7,44.4,46.4,47.9,52.1,56.0,55.7,53.4,51.3,52.1,50.2],color=color4,marker='*', markersize=6,label=label4)
plt.xticks(x1,fontsize=14)
plt.xlabel("p",fontsize=16)
plt.yticks(y1,fontsize=14)
plt.ylabel("Accuracy (%)",fontsize=16)
plt.legend()
plt.tight_layout()
# plt.savefig('Numbers_of_samples_AWA2.eps', format='eps')
plt.show()