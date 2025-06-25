def remove_duplicates(input_list):
    unique_list = list(set(input_list))
    return unique_list

# Example usage:
original_list = [10, 20, 20, 20, 30, 40, 40]
result_list = remove_duplicates(original_list)

print("Original List:", original_list)
print("List without Duplicates:", result_list)


