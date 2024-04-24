file_path = 'datasets/gapminder_1.csv'

# # Read the file
# with open(file_path, 'r') as file:
#     content = file.read()

# # Replace 4 spaces with a comma
# # content = content.replace(',,', ',')
# content = content.replace('Burkina,Faso', 'BurkinaFaso,')

# # Write the modified content back to the file
# with open(file_path, 'w') as file:
#     file.write(content)

# Dictionary of country name replacements
replacements = {
    'Burkina,Faso,': 'Burkina Faso,',
    'Central,African,Republic,': 'Central African Republic,',
    'Congo,Dem.,Rep.,': 'Congo Dem. Rep.,',
    'Congo,Rep.,': 'Congo Rep.,',
    'Costa,Rica,': 'Costa Rica,',
    'Cote,d\'Ivoire,': 'Cote d\'Ivoire,',
    'Czech,Republic,': 'Czech Republic,',
    'Dominican,Republic,': 'Dominican Republic,',
    'El,Salvador,': 'El Salvador,',
    'Equatorial,Guinea,': 'Equatorial Guinea,',
    'Hong,Kong,China,': 'Hong Kong China,',
    'Korea,Dem.,Rep.,': 'Korea Dem. Rep.,',
    'Korea,Rep.,': 'Korea Rep.,',
    'New,Zealand,': 'New Zealand,',
    'Puerto,Rico,': 'Puerto Rico,',
    'Sao,Tome,and,Principe,': 'Sao Tome and Principe,',
    'Saudi,Arabia,': 'Saudi Arabia,',
    'Sierra,Leone,': 'Sierra Leone,',
    'Slovak,Republic,': 'Slovak Republic,',
    'South,Africa,': 'South Africa,',
    'Sri,Lanka,': 'Sri Lanka,',
    'Trinidad,and,Tobago,': 'Trinidad and Tobago,',
    'United,Kingdom,': 'United Kingdom,',
    'United,States,': 'United States,',
    'West,Bank,and,Gaza,': 'West Bank and Gaza,',
    'Yemen,Rep.,': 'Yemen Rep.,'
}

# Read the file
with open(file_path, 'r') as file:
    content = file.read()

# Perform replacements
for old, new in replacements.items():
    content = content.replace(old, new)

# Write the modified content back to the file
with open(file_path, 'w') as file:
    file.write(content)

