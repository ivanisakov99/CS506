from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation
from tensorflow import keras
from tensorflow.keras import layers
from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation
import random
import numpy as np
from keras.callbacks import LambdaCallback

weights, bias = [], []
get_weights = LambdaCallback(
    on_epoch_end=lambda epoch, logs: weights.append(model.get_weights()[:-1]))
get_bias = LambdaCallback(
    on_epoch_end=lambda epoch, logs: bias.append(model.get_weights()[1]))

X = np.linspace(0, 10, 100)
Y = np.array([3 * x + 1 + random.normalvariate(0, 1) for x in X])

# TODO
epochs = 100
# N = 100
model = keras.models.Sequential()
model.add(layers.Dense(units=1, input_dim=1))
model.compile(loss='mean_squared_error')

weights, bias = [], []
history = model.fit(X,
                    Y,
                    batch_size=1,
                    epochs=200,
                    callbacks=[get_weights, get_bias],
                    verbose=0)

loss = history.history['loss']
weights = np.asarray(weights)[:, 0, 0, 0].tolist()
bias = np.asarray(bias)[:, 0].tolist()

fig = plt.figure()
ax = fig.add_subplot(projection='3d')


def update(num):
    line.set_data(data[:2, :num])
    line.set_3d_properties(data[2, :num])
    return line


data = np.asarray([weights, bias, loss])
line, = ax.plot(data[0, 0:1], data[1, 0:1], data[2, 0:1])

ax.set_xlim3d([min(weights), max(weights)])
ax.set_xlabel('weights')

ax.set_ylim3d([min(bias), max(bias)])
ax.set_ylabel('bias')

ax.set_zlim3d([min(loss), max(loss)])
ax.set_zlabel('loss')

ani = animation.FuncAnimation(fig,
                              update,
                              interval=20,
                              blit=False)

ani.save('2d.gif', writer='pillow')
plt.close()
Image('2d.gif')

# plt.show()