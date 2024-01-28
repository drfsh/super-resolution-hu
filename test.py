import os
import matplotlib.pyplot as plt
import numpy as np

from model.srgan import generator, discriminator
from model import resolve_single
from utils import load_image, plot_sample

weights_dir = 'weights'
weights_file = lambda filename: os.path.join(weights_dir, filename)

gan_generator = generator()

gan_generator.load_weights(weights_file('gan_generator.h5'))


def resolve_and_plot(lr_image_path):
    lr = load_image(lr_image_path)
    lr = np.array(lr)

    lr = lr[:, :, 0:3]

    gan_sr = resolve_single(gan_generator, lr)

    plt.figure(figsize=(20, 20))

    plt.imsave('new-img.png', np.array(gan_sr))

    return np.array(gan_sr)

