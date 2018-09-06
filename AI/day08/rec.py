import numpy as np
import neurolab as nl
import matplotlib.pyplot as mp
n = 30
x1 = np.cos(np.arange(0, n)) * 1
x2 = np.cos(np.arange(0, n)) * 2
x3 = np.cos(np.arange(0, n)) * 3
x4 = np.cos(np.arange(0, n)) * 4
train_x = np.array(
	[x1, x2, x3, x4]).reshape(-1, 1)
y1 = np.ones(n) * 0
y2 = np.ones(n) * 4
y3 = np.ones(n) * 2
y4 = np.ones(n) * 0
train_y = np.array(
	[y1, y2, y3, y4]).reshape(-1, 1)
model = nl.net.newelm([[-4, 4]], [10, 1],
	[nl.trans.TanSig(), nl.trans.PureLin()])
model.layers[0].initf = nl.init.InitRand(
	[-0.1, 0.1], 'wb')
model.layers[1].initf = nl.init.InitRand(
	[-0.1, 0.1], 'wb')
model.init()
error = model.train(train_x, train_y, epochs=1000,
	show=100, goal=0.01)
pred_train_y = model.sim(train_x)
mp.figure('Train', facecolor='lightgray')
mp.title('RNN', fontsize=20)
mp.xlabel('Time', fontsize=14)
mp.ylabel('Signal', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(train_x, c='hotpink', label='Input')
mp.plot(train_y, c='dodgerblue', label='True')
mp.plot(pred_train_y, c='limegreen', label='Predicted')
mp.legend()
mp.show()
mp.figure('Training Progress',
	facecolor='lightgray')
mp.title('Training Progress', fontsize=20)
mp.xlabel('Epoch', fontsize=14)
mp.ylabel('Error', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(error, c='orangered', label='Error')
mp.legend()
mp.show()
