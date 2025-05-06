import re
import pandas as pd
from collections import OrderedDict
import glob
import os

def parse_sections(filename):
    """Parse sections so each section's content is a single multi-line string."""
    sections = OrderedDict()
    current_section = None
    content_lines = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith("==>>"):
                if current_section is not None:
                    sections[current_section] = '\n'.join(content_lines).strip()
                current_section = re.sub(r'^==>>\s*|\s*\.\.\.$', '', line).strip()
                content_lines = []
            elif current_section:
                content_lines.append(line.rstrip('\n'))
        if current_section is not None:
            sections[current_section] = '\n'.join(content_lines).strip()
    return sections

# Path to your folder with txt files
FOLDER = "."  # Replace with your folder path
OUTPUT_FILE = "combined_report.xlsx"

# Find all txt files in the folder
file_paths = glob.glob(os.path.join(FOLDER, "*.txt"))

# Parse all files and collect all unique section titles
all_sections = set()
parsed_files = []
file_names = []

for file_path in file_paths:
    sections = parse_sections(file_path)
    all_sections.update(sections.keys())
    parsed_files.append(sections)
    file_names.append(os.path.basename(file_path))

# Sort section titles for consistent column order
all_sections = sorted(all_sections)

# Build list of dicts, one per file, filling missing sections with empty string
rows = []
for fname, file_sections in zip(file_names, parsed_files):
    row = {section: file_sections.get(section, "") for section in all_sections}
    row["Filename"] = fname  # Optionally include filename as first column
    rows.append(row)

df = pd.DataFrame(rows)
# Move Filename column to front if desired
cols = ["Filename"] + [c for c in df.columns if c != "Filename"]
df = df[cols]

# Write to Excel with line wrap formatting
with pd.ExcelWriter(OUTPUT_FILE, engine='xlsxwriter') as writer:
    df.to_excel(writer, index=False, sheet_name='Combined')
    worksheet = writer.sheets['Combined']
    workbook = writer.book
    wrap_format = workbook.add_format({'text_wrap': True, 'valign': 'top', 'font_name': 'Consolas', 'font_size': 10})
    for col_num, value in enumerate(df.columns.values):
        worksheet.set_column(col_num, col_num, 60, wrap_format)  # Adjust width as needed
