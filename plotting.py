import matplotlib.pyplot as plt
import numpy as np

# Funzione per visualizzare un'immagine da un tensor
def imshow(tensor_img, cmap=None, yuv = False):
    # Converti il tensor da (C, H, W) a (H, W, C) per matplotlib
    
    img = tensor_img.numpy()
    
    if yuv == False:
        img = tensor_img.permute(1, 2, 0).numpy()  # (C, H, W) -> (H, W, C)
        plt.imshow(img)
        plt.axis('off')  # Nasconde gli assi
        plt.show()

    else:
        plt.imshow(img, cmap = cmap)
        plt.axis('off')
        plt.show()
