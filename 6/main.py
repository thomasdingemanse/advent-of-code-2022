part = 2

def is_marker(datastream_buffer, position, marker_length):

    # The upper limit is exclusive.
    last = position + 1

    # The lower limit is inclusive.
    first = last - marker_length

    # Get all unique characters in this section.
    characters = set(datastream_buffer[first : last])

    # If they're all different, it's a marker.
    if len(characters) == marker_length:
        return True
    
    return False

with open("input.txt", "r") as input:
    datastream_buffer = input.read()
    position = 0
    
    # The marker length is different for part 2,
    # that's the only change compared to part 1.
    if part == 1:
        marker_length = 4
    else:
        marker_length = 14
    
    # Check every marker-length range of consecutive characters.
    while position < len(datastream_buffer):
    
        # Skip the first 3 characters because a marker is 4 characters long.
        if position < marker_length - 1:

            position += 1
            continue
        
        # Otherwise, check if it's a marker
        if is_marker(datastream_buffer, position, marker_length):
            
            # The positions are 1-indexed, so add 1 before printing.
            print(position + 1)

            # Skip to the end of the marker.
            position += marker_length
        
        # Slide the window one character forward.
        position += 1
