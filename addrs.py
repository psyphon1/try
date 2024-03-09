import secrets
import base58

def generate_address():
    # Generate 32 bytes (256 bits) random data
    random_data = secrets.token_bytes(32)
    
    # Convert the random data to base58 format
    address = base58.b58encode(random_data).decode('utf-8')
    
    return address

def main():
    num_addresses = int(input("Enter the number of addresses to generate: "))
    
    addresses = []
    for _ in range(num_addresses):
        address = generate_address()
        # Ensure the address starts with '1'
        if address[0] != '1':
            address = '1' + address[1:]
        addresses.append(address)
    
    # Save addresses to file
    with open('data.txt', 'w') as file:
        for address in addresses:
            file.write(address + '\n')
    
    print(f"{num_addresses} addresses generated and saved to data.txt")

if __name__ == "__main__":
    main()
