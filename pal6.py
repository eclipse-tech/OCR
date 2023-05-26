import json
import re

# Define glossary of words to identify plywood related items
glossary_ply = ["ply","puy","plg","plywood", "centuryply", "greenply", "X","green", "century", "win", "sainik", "mr", "bwp", "710 bwp", "bwp club", "7*4", "8*4", "4mm", "6mm", "8mm", "9mm", "12mm", "15mm", "16mm", "18mm", "19mm", "25mm", "*", "pl", "ly", "brand", "thickness", "dimension", "subbrand", "sub"]
glossary_Ilam = ["Off", "white", "fab", "fabric", "linen", "linen fabric", "sheets", "inner", "lam", "laminate", "laminated", "color", "matching color", "meters", "length", "inner laminate", "lamination","OffWhile"]
glossary_hin = ["Hardware", "Hinges", "Hin", "Hinge", "Crank", "Soft", "Normal", "Push To Open", "Push", "Open", "slide on", "slide", "Reg", "Regular", "opening", "Degree", "Degree of Opening", "Soft Closure", "Normal Closure", "Hings"]
glossary_cha = ["Hettich", "Slide", "Quadro", "Telescopic", "Nickel plated", "Nickel", "Zinc", "Zinc plated", "Mild steel", "steel", "stainless steel", "stainless", "Telescopic Slide", "Quadro Slide"]
glossary_Olam = ["Outer", "Virgo", "Tissot", "Herilam", "Stone"]
# Open the JSON file
with open('3.json') as f:
    data = json.load(f)

# Create an empty list to store the arrays that match the glossary
matched_arrays = []
matched_arrays1 = []
matched_arrays2 = []
matched_arrays3 = []
matched_arrays4 = []

#PLYWOOD
# Loop through each array in the JSON file
for row in data["Table"]:
    # Convert the array to a string and check if it matches with the glossary_ply
    row_str = " ".join(row).lower()
    if any(re.search(rf"\b{re.escape(term.lower())}\b", row_str) for term in glossary_ply):
        # Append the array to the list of matched arrays
        matched_arrays.append(row)

#INNER LAMINATE
# Loop through each array in the JSON file
for row in data["Table"]:
    # Convert the array to a string and check if it matches with the glossary_lam
    row_str = " ".join(row).lower()
    if any(re.search(rf"\b{re.escape(term.lower())}\b", row_str)for term in glossary_Ilam):
        # Append the array to the list of matched arrays
        matched_arrays1.append(row)

#HINGES
# Loop through each array in the JSON file
for row in data["Table"]:
    # Convert the array to a string and check if it matches with the glossary_lam
    row_str = " ".join(row).lower()
    if any(re.search(rf"\b{re.escape(term.lower())}\b", row_str) for term in glossary_hin):
        # Append the array to the list of matched arrays
        matched_arrays2.append(row)

#OuterLaminate
# Loop through each array in the JSON file
for row in data["Table"]:
    # Convert the array to a string and check if it matches with the glossary_lam
    row_str = " ".join(row).lower()
    if any(re.search(rf"\b{re.escape(term.lower())}\b", row_str) for term in glossary_Olam):
        # Append the array to the list of matched arrays
        matched_arrays3.append(row)

#channels
# Loop through each array in the JSON file
for row in data["Table"]:
    # Convert the array to a string and check if it matches with the glossary_lam
    row_str = " ".join(row).lower()
    if any(re.search(rf"\b{re.escape(term.lower())}\b", row_str) for term in glossary_cha):
        # Append the array to the list of matched arrays
        matched_arrays4.append(row)

# Create a dictionary with a key "plywood" and the value as the list of matched arrays
output_dict = {"plywood": matched_arrays, "Inner_Laminate": matched_arrays1, "Hinges": matched_arrays2, "Outer_Laminate": matched_arrays3, "Channels": matched_arrays4}

# Write the dictionary to the output.json file
with open('output.json', 'w') as f:
    json.dump(output_dict, f)