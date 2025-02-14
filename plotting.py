import matplotlib.pyplot as plt 

def imshow(tensor_img):
    img = tensor_img.numpy()
    img = tensor_img.permute(1, 2, 0).numpy()
    plt.imshow(img)
    plt.axis('off')
    plt.show()