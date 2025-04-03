import cv2
import numpy as np
import random

def encrypt_image(image_path, key):
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Image not found!")
        return None, None
    
    height, width, _ = image.shape
    
    # Generate random permutation using the key
    np.random.seed(key)
    indices = np.random.permutation(height * width)
    
    # Flatten the image and apply permutation
    flat_image = image.reshape(-1, 3)
    shuffled_image = flat_image[indices]
    
    # Convert key to uint8 range (0-255)
    key = key % 256
    
    # Apply XOR encryption
    encrypted_image = np.bitwise_xor(shuffled_image, key)
    encrypted_image = encrypted_image.reshape(height, width, 3)
    
    cv2.imwrite("encrypted_image.png", encrypted_image)
    return encrypted_image, indices

def decrypt_image(encrypted_image_path, key, indices):
    encrypted_image = cv2.imread(encrypted_image_path)
    if encrypted_image is None:
        print("Error: Encrypted image not found!")
        return None
    
    height, width, _ = encrypted_image.shape
    
    # Convert key to uint8 range
    key = key % 256
    
    # Flatten and reverse XOR operation
    flat_image = encrypted_image.reshape(-1, 3)
    unshuffled_image = np.bitwise_xor(flat_image, key)
    
    # Reverse permutation
    original_image = np.zeros_like(unshuffled_image)
    original_image[indices] = unshuffled_image
    original_image = original_image.reshape(height, width, 3)
    
    cv2.imwrite("decrypted_image.png", original_image)
    return original_image

# Example Usage
key = 12345  # Encryption key
image_path = "image.png"  # Input image path
encrypted_img, indices = encrypt_image(image_path, key)
if encrypted_img is not None:
    decrypted_img = decrypt_image("encrypted_image.png", key, indices)