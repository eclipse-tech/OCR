import json
import re

# Load the JSON file
with open("output1.json") as f:
    data = json.load(f)

plywood_attributes = {
    "Brand": ["CenturyPly", "GreenPly", "Green", "Century"],
    "Sub-brand": ["Win", "Sainik"],
    "Grade": ["MR", "BWP", "710 BWP", "BWP Club"],
    "Dimension": ["7x4", "8x4"],
    "Thickness": ["4mm", "6mm", "8mm", "9mm", "12mm", "15mm", "16mm", "18mm", "19mm", "25mm"],
    "Quantity": ["mo", "no", "nos", "no's", "bonos", "cono's"]
}

hinge_attributes = {
    "Brand": ["Hettich"],
    "Crank": ["0", "8", "16"],
    "Closure": ["Soft Closure", "Normal Closure", "Push To Open", "Soft", "Normal"],
    "Type": ["Slide on", "Regular"],
    "Degree of opening": ["90", "110", "165"]
}

inner_laminate_attributes = {
    "Type": ["Fabric", "Linen Fabric", "Off White","Off", "White","offwhile","offwhite"]
}

# Iterate over each input string in the "plywood" list
for input_string in data["plywood"]:
    # Initialize all attributes to "NA"
    brand = sub_brand = grade = dimension = thickness = quantity= "NA"
    
    # Search for thickness in the input string
    match = re.search(r"\d+mm", input_string)
    if match:
        thickness = match.group()
        input_string = input_string.replace(thickness, "")  # Remove the thickness from the input string

    # Search for quantity in the input string
        for quantity_word in plywood_attributes["Quantity"]:
            match = re.search(r"\d+"+quantity_word, input_string)
            if match:
                quantity = match.group()
                input_string = input_string.replace(quantity, "")  # Remove the quantity from the input string
                break


    # Iterate over each word in the input string
    for word in input_string.split("-"):
        # Check if the word matches any of the predefined attributes
        if any([brand_word in word for brand_word in plywood_attributes["Brand"]]):
            brand = word
        elif any([sub_brand_word in word for sub_brand_word in plywood_attributes["Sub-brand"]]):
            sub_brand = word
        elif any([grade_word in word for grade_word in plywood_attributes["Grade"]]):
            grade = word
        elif any([dimension_word in word for dimension_word in plywood_attributes["Dimension"]]):
            dimension = re.sub(r'[^0-9x*]', '', word)

    # Print all the attributes for the current input string
    print("Plywood:")
    print("Brand:", brand)
    print("Sub-brand:", sub_brand)
    print("Grade:", grade)
    print("Dimension:", dimension)
    print("Thickness:", thickness)
    print("Quantity:", quantity)
    print()

# Iterate over each input string in the "hinges" list
for input_string in data["Hinges"]:
    # Initialize all attributes to "NA"
    brand = crank = closure = hinge_type = degree_of_opening = "NA"
    
    # Iterate over each word in the input string
    for word in input_string.split("-"):
        # Check if the word matches any of the predefined attributes
        if any([brand_word in word for brand_word in hinge_attributes["Brand"]]):
            brand = word
        elif any([crank_word in word for crank_word in hinge_attributes["Crank"]]):
            if word in ["0", "8", "16"]:
                crank = word
        elif any([closure_word in word for closure_word in hinge_attributes["Closure"]]):
            closure = word
        elif any([type_word in word for type_word in hinge_attributes["Type"]]):
            hinge_type = word
        elif any([degree_word in word for degree_word in hinge_attributes["Degree of opening"]]):
            degree_of_opening = word

# Print all the attributes for the current input string
    print("Hinges:")
    print("Brand:", brand)
    print("Crank:", crank)
    print("Closure:", closure)
    print("Type:", hinge_type)
    print("Degree of opening:", degree_of_opening)
    print()


# Iterate over each input string in the "Inner_Laminate" list
for input_string in data["Inner_Laminate"]:
    # Initialize all attributes to "NA"
    type = "NA"

    # Iterate over each word in the input string
    for word in input_string.split("-"):
        # Check if the word matches any of the predefined attributes
        #if any([type_word in word for type_word in inner_laminate_attributes["Type"]]):
        if any([type_word in word for type_word in inner_laminate_attributes["Type"]]):
            type = [type_word for type_word in inner_laminate_attributes["Type"] if type_word in word][0]  
            #type = word

# Print all the attributes for the current input string
    print("Inner_Laminate:")
    print("Type:", type)
    print()
