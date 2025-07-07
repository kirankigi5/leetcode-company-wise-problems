#!/usr/bin/env python3
"""
Enhanced script to convert all Amazon CSV files to Markdown format with additional columns.
"""

import csv
import os
import glob

def convert_csv_to_md(csv_file_path, md_file_path):
    """
    Convert CSV file to Markdown table format with additional columns.
    
    Args:
        csv_file_path (str): Path to the input CSV file
        md_file_path (str): Path to the output Markdown file
    """
    
    # Read the CSV file
    with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        rows = list(csv_reader)
    
    # Extract filename for title
    filename = os.path.basename(csv_file_path).replace('.csv', '')
    
    # Create the Markdown content
    md_content = f"# Amazon LeetCode Problems - {filename}\n\n"
    md_content += f"This document contains Amazon LeetCode problems from {filename} with tracking for solved status and solutions.\n\n"
    md_content += f"**Total Problems: {len(rows)}**\n\n"
    
    # Create the table header
    headers = ["#", "Difficulty", "Title", "Frequency", "Acceptance Rate", "Topics", "Solved", "Solution"]
    md_content += "| " + " | ".join(headers) + " |\n"
    md_content += "|" + "|".join([" --- " for _ in headers]) + "|\n"
    
    # Add each row
    for idx, row in enumerate(rows, 1):
        # Format the row data
        difficulty = row.get('Difficulty', '')
        title = row.get('Title', '')
        frequency = row.get('Frequency', '')
        acceptance_rate = row.get('Acceptance Rate', '')
        link = row.get('Link', '')
        topics = row.get('Topics', '')
        
        # Create clickable link for the title
        if link:
            title_link = f"[{title}]({link})"
        else:
            title_link = title
        
        # Format acceptance rate as percentage
        try:
            acceptance_float = float(acceptance_rate)
            acceptance_formatted = f"{acceptance_float:.1%}"
        except (ValueError, TypeError):
            acceptance_formatted = acceptance_rate
        
        # Add emoji for difficulty
        difficulty_emoji = {
            'EASY': '🟢',
            'MEDIUM': '🟡', 
            'HARD': '🔴'
        }
        difficulty_display = f"{difficulty_emoji.get(difficulty, '')} {difficulty}"
        
        # Add default values for new columns
        solved = "❌"  # Default to not solved
        solution = ""  # Empty solution link
        
        # Create the row
        md_row = f"| {idx} | {difficulty_display} | {title_link} | {frequency} | {acceptance_formatted} | {topics} | {solved} | {solution} |"
        md_content += md_row + "\n"
    
    # Add footer with instructions
    md_content += "\n---\n\n"
    md_content += "## How to use this document:\n\n"
    md_content += "- ✅ Mark as solved when you complete a problem\n"
    md_content += "- ❌ Default status (not solved)\n" 
    md_content += "- Add solution links in the Solution column\n"
    md_content += "- 🟢 Easy problems\n"
    md_content += "- 🟡 Medium problems\n"
    md_content += "- 🔴 Hard problems\n\n"
    md_content += f"**Generated from:** `{os.path.basename(csv_file_path)}`\n"
    md_content += f"**Last updated:** {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    
    # Write to markdown file
    with open(md_file_path, 'w', encoding='utf-8') as mdfile:
        mdfile.write(md_content)
    
    return len(rows)

def main():
    # Define directory path
    amazon_dir = "/home/kiran-reddy/Documents/job/dsa/leetcode-company-wise-problems/Amazon"
    
    # Find all CSV files in the Amazon directory
    csv_files = glob.glob(os.path.join(amazon_dir, "*.csv"))
    
    print(f"Found {len(csv_files)} CSV files in Amazon directory:")
    
    total_problems = 0
    for csv_file in csv_files:
        # Create markdown filename
        base_name = os.path.basename(csv_file).replace('.csv', '')
        md_file = os.path.join(amazon_dir, f"{base_name}_Problems.md")
        
        # Convert the file
        problem_count = convert_csv_to_md(csv_file, md_file)
        total_problems += problem_count
        
        print(f"✅ Converted {base_name}.csv → {base_name}_Problems.md ({problem_count} problems)")
    
    print(f"\n🎉 Conversion complete! Total problems across all files: {total_problems}")
    print(f"📁 All markdown files saved in: {amazon_dir}")

if __name__ == "__main__":
    main()
