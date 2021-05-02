def salt_pepper(prob):
    # Extract image dimensions
    row, col = img_gs.shape

    # Declare salt & pepper noise ratio
    s_vs_p = 0.5
    output = np.copy(img_gs)

    # Apply salt noise on each pixel individually
    num_salt = np.ceil(prob * img_gs.size * s_vs_p)
    coords = [np.random.randint(0, i - 1, int(num_salt))
              for i in img_gs.shape]
    output[coords] = 1

    # Apply pepper noise on each pixel individually
    num_pepper = np.ceil(prob * img_gs.size * (1. - s_vs_p))
    coords = [np.random.randint(0, i - 1, int(num_pepper))
              for i in img_gs.shape]
    output[coords] = 0
    cv2_imshow(output)

    return output


# Call salt & pepper function with probability = 0.5
# on the grayscale image of rose
sp_05 = salt_pepper(0.5)

# Store the resultant image as 'sp_05.jpg'
cv2.imwrite('sp_05.jpg', sp_05)
kernel_sharpening = np.array([[-1,-1,-1],
                              [-1, 9,-1],
                              [-1,-1,-1]])

# Applying the sharpening kernel to the grayscale image & displaying it.
print("\n\n--- Effects on S&P Noise Image with Probability 0.5 ---\n\n")

# Applying filter on image with salt & pepper noise
sharpened_img = cv2.filter2D(sp_05, -1, kernel_sharpening)
cv2_imshow(sharpened_img)