import json

# read input JSON file
with open("output.json", "r") as f:
    input_data = json.load(f)

# process arrays in input data
output_data = {}
for key, arr_list in input_data.items():
    processed_arr_list = []
    for arr in arr_list:
        arr_without_spaces = [s.replace(" ", "") for s in arr]
        processed_arr_list.append(''.join(arr_without_spaces))
    output_data[key] = processed_arr_list

# write output JSON file
with open("output1.json", "w") as f:
    json.dump(output_data, f, indent=4)
