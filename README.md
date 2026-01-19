# UCS654-assignment1-102303367-
Author: Sargun Kaur

Introduction

TOPSIS (Technique for Order Preference by Similarity to Ideal Solution) is a Multi-Criteria Decision Making (MCDM) method used to rank alternatives based on their distance from an ideal best and ideal worst solution. The best alternative is the one that is closest to the ideal best and farthest from the ideal worst.

This project provides:
1. A command-line Python program
2. A reusable Python package uploaded to PyPI
3. A web-based application that emails results

Objectives

1. Implement the TOPSIS algorithm correctly in Python
2. Validate user inputs and handle errors gracefully
3. Provide result ranking in tabular and graphical format
4. Allow users to access TOPSIS via CLI, package, and web service

TOPSIS Methodology
m alternatives
n criteria
Decision matrix: X=[xij]
Weight vector: W=[w1,w2,...,wn]
Impact vector:I=[+,-,+,....]

Step 1: Construct Decision Matrix

The input CSV file must contain:
First column → Alternative names
Remaining columns → Numeric criteria values

Step 2: Normalize the Decision Matrix

Step 3: Weighted Normalized Matrix
Each normalized value is multiplied by its corresponding weight: vij= rij * wij

Step 4: Determine Ideal Best and Ideal Worst

Step 5: Calculate Separation Measures

Step 6: Calculate TOPSIS Score
Higher score = better alternative

Step 7: Rank Alternatives

Input Format

CSV file with at least 3 columns
First column → Alternative names
Remaining columns → Numeric values only
Weights → Comma-separated values
Impacts → + or -, comma-separated

The output CSV file contains:

Column	                          Description
Original columns	                Input data
Topsis Score	                  Performance score
Rank	                            Final ranking

Result Graph Explanation

A bar chart is generated using TOPSIS scores:
X-axis: Alternatives
Y-axis: TOPSIS Scores
The tallest bar indicates the best alternative, making comparison simple and intuitive.

Command Line Usage
python topsis.py data.csv "1,1,1,2" "+,+,-,+" result.csv

Web Application Usage

1.Upload CSV file
2.Enter weights (comma-separated)
3.Enter impacts (+ or -)
5.4.Enter email address
6.Submit the form

✔ Result CSV file is emailed to the user automatically


