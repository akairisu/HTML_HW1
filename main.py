import numpy as np
import os
import random
import math

def PLA(data, target, question_num):
	length_sum = 0

	for times in range(1000):
		random.seed(times)

		w = np.zeros(11)

		correct_count = 0

		while correct_count < 5 * N:
			rand_index = random.randint(0, N - 1)
			in_pro = np.dot(w, data[rand_index])
			if in_pro * target[rand_index] < 0 or \
					(in_pro == 0 and target[rand_index] == 1):
				w = w + target[rand_index] * data[rand_index]
				correct_count = 0
			else:
				correct_count = correct_count + 1

		length = np.sum(np.square(w))
		length_sum += length
	print("Question:", question_num)
	print(length_sum / 1000)


data_file = "./hw1_train.dat"

#input
N = 100
x_list = []
y_list = []

with open(data_file, 'r') as file:
	count = 0
	while True:
		line = file.readline() 
		if not line:
			break
		cur_x = line[:-1].split('\t')
		cur_x_float = [1]
		for i in range(len(cur_x) - 1):
			cur_x_float.append(float(cur_x[i]))
		y_list.append(int(float(cur_x[len(cur_x) - 1])))
		x_list.append(cur_x_float)
		count = count + 1

x_list = np.array(x_list)
#Q13
PLA(x_list, y_list, 13)

#Q14
multi_x_list = x_list * 2

PLA(multi_x_list, y_list, 14)

#Q15
norm_x_list = np.array(x_list)

for i in range(len(x_list)):
	normed = x_list[i] / math.sqrt(np.sum(np.square(x_list[i])))
	norm_x_list[i] = normed

PLA(norm_x_list, y_list, 15)
#Q16
origin_x_list = np.array(x_list)
for i in range(len(origin_x_list)):
	origin_x_list[i][0] = 0

PLA(origin_x_list, y_list, 16)