def hillClimb(arr, start_index):
    if not arr:
        raise ValueError("arr must not be empty")
    if not (0 <= start_index < len(arr)):
        raise IndexError("start_index out of range")

    current_position = start_index
    
    while True:
        current_value = arr[current_position]
        
        # Check what's to the left and right
        can_go_left = current_position > 0
        can_go_right = current_position < len(arr) - 1
        
        left_value = arr[current_position - 1] if can_go_left else -999999
        right_value = arr[current_position + 1] if can_go_right else -999999
        
        # Find the best direction to move
        # If we can improve by going right, do that first (tie-breaker)
        if can_go_right and right_value >= current_value and right_value >= left_value:
            current_position += 1
        # Otherwise, try going left if it's better
        elif can_go_left and left_value > current_value:
            current_position -= 1
        # If we can't improve in either direction, we've found our peak!
        else:
            return current_position, current_value


# arr = [1,2,3,4,3,2,6,8,4,3]
# start_index = 3

# arr = [1,2,3,4,5,6,7]
# start_index = 2

arr = [6,5,3,10,3,9,4,7,8,1]
start_index = 2

# arr = [3,6,5,4,7,9,6,4,3]
# start_index = 3

# arr = [1,2,3,3,3,4,5]
# start_index = 1

# arr = [1,2,3,3,3,4,5]
# start_index = 3

# arr = [1,2,3,4,3,2,5,6,7,3,1]
# start_index = 5


val, best = hillClimb(arr, start_index)
print(f"Best peak at index {val} with value {best} found.")