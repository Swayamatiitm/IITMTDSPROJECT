import pandas as pd

# Load the dataset
file_path = r'C:\Users\dprup\Downloads\dataset_11_3.xlsx'

# Load the "AB Testing" sheet
ab_testing_data = pd.read_excel(file_path, sheet_name='AB Testing')

# Filter data for the treatment group
treatment_group = ab_testing_data[ab_testing_data['Group'] == 'T']

# Count the number of customers who moved from "Medium" to "High"
moved_to_high = treatment_group[
    (treatment_group['Old_eng_segment'] == 'Medium') &
    (treatment_group['New_eng_segment'] == 'High')
].shape[0]

# Count the total number of customers in the treatment group
total_customers_treatment = treatment_group.shape[0]

# Calculate the percentage
percentage_moved = moved_to_high / total_customers_treatment

# Apply standard rounding to 2 decimal places
percentage_moved_rounded = round(percentage_moved, 2)

print("The percentage of customers who moved to 'High' from the 'Medium' engagement segment in the treatment group is:", percentage_moved_rounded)
