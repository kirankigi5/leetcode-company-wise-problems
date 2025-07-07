#!/usr/bin/env python3
"""
Script to convert Amazon CSV file to Markdown format with additional columns.
"""

import csv
import os

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
    
    # Create the Markdown content
    md_content = "# Amazon LeetCode Problems\n\n"
    md_content += "This document contains Amazon LeetCode problems with tracking for solved status and solutions.\n\n"
    
    # Create the table header
    headers = ["Difficulty", "Title", "Frequency", "Acceptance Rate", "Link", "Topics", "Solved", "Solution"]
    md_content += "| " + " | ".join(headers) + " |\n"
    md_content += "|" + "|".join([" --- " for _ in headers]) + "|\n"
    
    # Add each row
    for row in rows:
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
        
        # Add default values for new columns
        solved = "❌"  # Default to not solved
        solution = ""  # Empty solution link
        
        # Create the row
        md_row = f"| {difficulty} | {title_link} | {frequency} | {acceptance_formatted} | [Link]({link}) | {topics} | {solved} | {solution} |"
        md_content += md_row + "\n"
    
    # Write to markdown file
    with open(md_file_path, 'w', encoding='utf-8') as mdfile:
        mdfile.write(md_content)
    
    print(f"Successfully converted {csv_file_path} to {md_file_path}")
    print(f"Total problems: {len(rows)}")

def main():
    # Define file paths
    csv_file = "/home/kiran-reddy/Documents/job/dsa/leetcode-company-wise-problems/Amazon/5. All.csv"
    md_file = "/home/kiran-reddy/Documents/job/dsa/leetcode-company-wise-problems/Amazon/Amazon_Problems.md"
    
    # Convert the file
    convert_csv_to_md(csv_file, md_file)

if __name__ == "__main__":
    main()
