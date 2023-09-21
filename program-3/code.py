import re

def is_valid_ip_address(ip_address):
    # Regular expression to match an IP address
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    
    # Check if the IP address matches the pattern
    if re.match(pattern, ip_address):
        # Split the IP address into its components
        components = ip_address.split('.')
        
        # Check if each component is between 0 and 255
        for component in components:
            if int(component) < 0 or int(component) > 255:
                return False
        
        # If all components are valid, return True
        return True
    else:
        # If the IP address doesn't match the pattern, return False
        return False

# Test script
assert is_valid_ip_address('192.168.0.1') == True
assert is_valid_ip_address('255.255.255.0') == True
assert is_valid_ip_address('0.0.0.0') == True
assert is_valid_ip_address('256.0.0.0') == False
assert is_valid_ip_address('192.168.0') == False
assert is_valid_ip_address('192.168.0.1.2') == False
assert is_valid_ip_address('192.168.0.-1') == False
assert is_valid_ip_address('192.168.0.256') == False
assert is_valid_ip_address('') == False
