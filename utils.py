import numpy as np
import matplotlib.pyplot as plt

from PIL import Image


def load_image(path):
    return np.array(Image.open(path))


def plot_sample(lr, sr):

    images = [lr, sr]
    titles = ['LR',  'SR (GAN)']
    positions = [1,2]

    for i, (img, title, pos) in enumerate(zip(images, titles, positions)):
        plt.subplot(1, 2, pos)
        plt.imshow(img)
        plt.title(title)
        plt.xticks([])
        plt.yticks([])
    plt.show()

