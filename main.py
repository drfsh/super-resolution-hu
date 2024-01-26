# import os
# import matplotlib.pyplot as plt

from data import DATA

# from model.srgan import generator, discriminator
# from train import SrganTrainer, SrganGeneratorTrainer
# import matplotlib.pyplot as plt

print('Dataset preparation: start...')

div2k_train = DATA(subset='test_train', smapls=range(1, 800))
div2k_valid = DATA(subset='test_valid', smapls=range(801, 900))

train_ds = div2k_train.dataset(batch_size=3, random_transform=True)
valid_ds = div2k_valid.dataset(batch_size=3, random_transform=True, repeat_count=1)

# print('Dataset preparation: end')
#
# print('Training: Start')
#
#
# # Create a new generator and init it with pre-trained weights.
# gan_generator = generator()
# gan_generator.load_weights('weights/test/pre_generator.h5')
#
# # Create a training context for the GAN (generator + discriminator).
# gan_trainer = SrganTrainer(generator=gan_generator, discriminator=discriminator())
#
# # Train the GAN with 200,000 steps.
# gan_trainer.train(train_ds, steps=200000)
#
# # Save weights of generator and discriminator.
# gan_trainer.generator.save_weights('weights/test/gan_generator.h5')
# gan_trainer.discriminator.save_weights('weights/test/gan_discriminator.h5')
#
#
# print('Training: End')
