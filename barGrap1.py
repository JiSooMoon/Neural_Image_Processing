# #-------------------------------------------------------------- ANN_Accuracy_Plot
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

#DATASET = "mnist_d"
# DATASET = "mnist_f"
# DATASET = "cifar_10"
# DATASET = "cifar_100_f"
# DATASET = "cifar_100_c"

objects = ('mnist_d', 'mnist_f', 'cifar_10', 'cifar_100_f', 'cifar_100_c')
y_pos = np.arange(len(objects))
performance = [95.65,77.69, 47.19,14.24,27.90]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Accuracy')
plt.title('ANN')

plt.show()








#-------------------------------------------------------------- CNN_Accuracy_Plot
# import matplotlib.pyplot as plt; plt.rcdefaults()
# import numpy as np
# import matplotlib.pyplot as plt

# #DATASET = "mnist_d"
# # DATASET = "mnist_f"
# # DATASET = "cifar_10"
# # DATASET = "cifar_100_f"
# # DATASET = "cifar_100_c"

# objects = ('mnist_d', 'mnist_f', 'cifar_10', 'cifar_100_f', 'cifar_100_c')
# y_pos = np.arange(len(objects))
# performance = [99.11,92.34,72.5,38.62,52.3]

# plt.bar(y_pos, performance, align='center', alpha=0.5)
# plt.xticks(y_pos, objects)
# plt.ylabel('Accuracy')
# plt.title('CNN')

# plt.show()