#IP_address_solver.py

# copilot will write the code for this file
def is_valid_segment(segment):
    # Check if the segment is a valid IP address segment
    if len(segment) == 0 or len(segment) > 3:
        return False
    if segment[0] == '0' and len(segment) > 1:  # No leading zeros allowed
        return False
    if not segment.isdigit() or int(segment) < 0 or int(segment) > 255:
        return False
    return True 

# still in progress
