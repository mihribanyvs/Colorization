# Colorization
## VCS project 
- [ ] Choosing the YUV format of images
- [ ] Creating an encoder and a decoder style

## Encoder
Using a CNN structure, training with the Y and UV scales to create a mapping from Y to UV.
- [ ] Need to create a loss function that can 

## Decoder
Using the CNN learned parameters we can get a probability distribution for colors for each pixel and choose the highest probability for each pixel to color the image. 
