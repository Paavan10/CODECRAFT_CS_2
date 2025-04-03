# Pixel Encryption & Decryption 🔒🖼️  

A Python-based Image Encryption & Decryption tool using pixel manipulation and XOR encryption. This project scrambles image pixels and applies XOR operations for secure image encryption.

## 🚀 Features  
- Encrypts images by scrambling pixels and applying XOR operations  
- Decrypts images using the correct key and reverse permutation  
- Works with any image format supported by OpenCV  
- Simple and effective encryption technique  

## 📷 Example Usage  
```python
# Example Usage
key = 12345  # Encryption key
image_path = "image.png"  # Input image path
encrypted_img, indices = encrypt_image(image_path, key)

# Decrypting the Image
if encrypted_img is not None:
    decrypted_img = decrypt_image("encrypted_image.png", key, indices)
