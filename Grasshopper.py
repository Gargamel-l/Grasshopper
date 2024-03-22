def simple_encrypt_block(block, key):
    # Здесь должна быть реализация шифрования блока, например, симуляция с помощью XOR с ключом
    encrypted_block = bytes([b ^ key for b in block])
    return encrypted_block

def simple_decrypt_block(block, key):
    # Для демонстрации используем ту же операцию, что и для шифрования, т.к. XOR является обратимой операцией
    decrypted_block = bytes([b ^ key for b in block])
    return decrypted_block

def encrypt_ecb(data, key):
    block_size = 16  # Размер блока в байтах
    encrypted_data = bytearray()
    for i in range(0, len(data), block_size):
        block = data[i:i+block_size]
        if len(block) < block_size:
            block += b'\x00' * (block_size - len(block))  # Дополнение блока до полного размера
        encrypted_data += simple_encrypt_block(block, key)
    return bytes(encrypted_data)

def decrypt_ecb(data, key):
    block_size = 16
    decrypted_data = bytearray()
    for i in range(0, len(data), block_size):
        block = data[i:i+block_size]
        decrypted_data += simple_decrypt_block(block, key)
    return bytes(decrypted_data)

# Пример использования
key = 0x0F  # Пример простого ключа для демонстрации
data = b"Hello, World!"
encrypted = encrypt_ecb(data, key)
decrypted = decrypt_ecb(encrypted, key)

print("Исходные данные:", data)
print("Зашифрованные данные:", encrypted)
print("Расшифрованные данные:", decrypted)

