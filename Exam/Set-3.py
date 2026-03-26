# Task 1 :

# IPv4 Address Validator Task

# <!-- Prompt: "Write a Python function is_valid_ipv4(ip_string) that validates an IPv4 address in dotted-decimal notation. The function must return True only if there are exactly four octets separated by periods, each octet is between 0 and 255, and no octet has leading zeros (e.g., '192.168.1.1' is valid, but '192.168.01.1' is invalid)." -->



def is_valid_ipv4(ip: str) -> bool:
    # Split by periods
    parts = ip.split('.')
    
    # Must have exactly 4 parts
    if len(parts) != 4:
        return False
    
    for part in parts:
        # Check if digit and handle empty strings
        if not part.isdigit():
            return False
        
        # Check range 0-255
        val = int(part)
        if val < 0 or val > 255:
            return False
        
        # Check for leading zeros: "0" is okay, "01" is not
        if part != "0" and part.startswith("0"):
            return False
            
    return True

# Test cases
print(is_valid_ipv4("192.168.1.1"))  # True
print(is_valid_ipv4("192.168.01.1")) # False (Leading zero)
print(is_valid_ipv4("256.0.0.1"))    # False (Out of range)






