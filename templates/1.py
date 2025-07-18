import csv

# Function to read the CSV file and return its contents as a list of dictionaries
def read_csv_file(file_path):
    data = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

# Function to generate HTML content for displaying CSV data
def generate_html(csv_data):
    html_content = '<table border="1">'
    # Add table header
    html_content += '<tr><th>Place</th><th>Ratings</th><th>Ideal Duration</th><th>Best Time to Visit</th><th>Image</th><th>City Description</th></tr>'
    # Add table rows
    for row in csv_data:
        html_content += f'<tr><td>{row["Place"]}</td><td>{row["Ratings"]}</td><td>{row["Ideal_duration"]}</td><td>{row["Best_time_to_visit"]}</td><td>{row["Image"]}</td><td>{row["City_desc"]}</td></tr>'
    html_content += '</table>'
    return html_content

# Path to your CSV file
csv_file_path = 'city_final(4).csv'

# Read the CSV file
csv_data = read_csv_file(csv_file_path)

# Generate HTML content
html_content = generate_html(csv_data)

# Write HTML content to a file
with open('example2.html', 'w') as html_file:
    html_file.write(html_content)

print("HTML file generated successfully.")
