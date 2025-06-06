import matplotlib.pyplot as plt
import matplotlib
import numpy as np
matplotlib.use('TkAgg')
matplotlib.rcParams['font.family'] = 'Times New Roman'  # 字体名称
# matplotlib.rcParams['text.usetex'] = True
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

'''AWA2中图像语义表示的系数alpha'''
# x1=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
# y1=[60,65,70,75,80]
# plt.plot(x1, [68.4,69.7,70.5,71.7,72.8,74.9,73.4,71.7,69.2,67.4],color=color1,marker='^', markersize=6,label=label1)
# plt.plot(x1, [62.7,63.6,65.1,67.3,69.2,70.4,69.1,67.8,66.7,65.2],color=color2,marker='s', markersize=6,label=label2)
# plt.plot(x1, [69.2,70.4,72.4,75.7,79.4,83.7,81.5,78.5,76.3,74.6],color=color3,marker='o', markersize=6,label=label3)
# plt.plot(x1, [65.8,66.8,68.6,71.3,73.9,76.5,74.8,72.8,71.2,69.6],color=color4,marker='*', markersize=6,label=label4)
# plt.xticks(x1,fontsize=14)
# plt.xlabel(r'$\alpha$',fontsize=16)
# plt.yticks(y1,fontsize=14)
# plt.ylabel("Accuracy (%)",fontsize=16)
# plt.legend()
# plt.tight_layout()
# # plt.savefig('Numbers_of_samples_AWA2.eps', format='eps')
# plt.show()

'''CUB中图像语义表示的系数alpha'''
# x1=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
# y1=[60,65,70,75,80]
# plt.plot(x1, [74.6,75.4,78.7,81.2,82.7,81.3,80.1,78.6,77.9,75.7],color=color1,marker='^', markersize=6,label=label1)
# plt.plot(x1, [63.5,65.7,66.6,67.3,68.7,67.8,66.9,65.7,65.9,64.5],color=color2,marker='s', markersize=6,label=label2)
# plt.plot(x1, [74.8,76.2,76.9,77.6,78.4,78.3,76.3,75.4,75.8,75.6],color=color3,marker='o', markersize=6,label=label3)
# plt.plot(x1, [68.7,70.6,71.4,72.1,73.2,72.7,71.3,70.2,70.5,69.6],color=color4,marker='*', markersize=6,label=label4)
# plt.xticks(x1,fontsize=14)
# plt.xlabel(r'$\alpha$',fontsize=16)
# plt.yticks(y1,fontsize=14)
# plt.ylabel("Accuracy (%)",fontsize=16)
# plt.legend()
# plt.tight_layout()
# # plt.savefig('Numbers_of_samples_AWA2.eps', format='eps')
# plt.show()

'''SUN中图像语义表示的系数alpha'''
x1=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
y1=[45,50,55,60,65]
plt.plot(x1, [62.2,62.8,63.4,64.6,64.7,65.7,65.9,66.7,67.3,67.1],color=color1,marker='^', markersize=6,label=label1)
plt.plot(x1, [46.7,47.2,47.9,48.4,49.1,50.5,51.8,52.4,53.5,52.8],color=color2,marker='s', markersize=6,label=label2)
plt.plot(x1, [58.4,58.9,57.8,57.5,58.2,57.6,56.7,59.4,58.7,58.8],color=color3,marker='o', markersize=6,label=label3)
plt.plot(x1, [51.9,52.4,52.4,52.6,53.3,53.8,54.1,55.7,56.0,55.6],color=color4,marker='*', markersize=6,label=label4)
plt.xticks(x1,fontsize=14)
plt.xlabel(r'$\alpha$',fontsize=16)
plt.yticks(y1,fontsize=14)
plt.ylabel("Accuracy (%)",fontsize=16)
plt.legend()
plt.tight_layout()
# plt.savefig('Numbers_of_samples_AWA2.eps', format='eps')
plt.show()