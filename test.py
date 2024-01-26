import os
import matplotlib.pyplot as plt
import numpy as np

from model.srgan import generator, discriminator
from model import resolve_single
from utils import load_image,plot_sample

# Location of model we  ights (needed for demo)
weights_dir = 'weights/srgan'
weights_file = lambda filename: os.path.join(weights_dir, filename)

# pre_generator = generator()
gan_generator = generator()

# pre_generator.load_weights(weights_file('pre_generator.h5'))
gan_generator.load_weights(weights_file('gan_generator.h5'))


def resolve_and_plot(lr_image_path):
    lr = load_image(lr_image_path)
    lr = np.array(lr)

    lr = lr[:, :, 0:3]

    # pre_sr = resolve_single(pre_generator, lr)
    gan_sr = resolve_single(gan_generator, lr)

    plt.figure(figsize=(20, 20))

    # plot_sample(lr,gan_sr)

    plt.imsave('new-img.png', np.array(gan_sr))

    return np.array(gan_sr)
