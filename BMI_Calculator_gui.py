import csv
import os
from datetime import datetime

def calculate_bmi(weight, height):
    """Calculate BMI given weight (in kg) and height (in meters)."""
    if height <= 0:
        raise ValueError("Height must be greater than 0.")
    return weight / (height ** 2)

def determine_bmi_category(bmi):
    """Determine BMI category based on BMI value."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def save_to_csv(weight, height, bmi, category):
    """Save BMI data to a CSV file."""
    filename = "bmi_data.csv"
    file_exists = os.path.isfile(filename)

    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['Date', 'Weight (kg)', 'Height (m)', 'BMI', 'Category'])
        writer.writerow([datetime.now().strftime('%Y-%m-%d %H:%M:%S'), weight, height, bmi, category])

def main():
    try:
        # Get user input
        weight = float(input("Enter your weight (in kg): "))
        height = float(input("Enter your height (in meters): "))

        # Calculate BMI
        bmi = calculate_bmi(weight, height)
        
        # Determine BMI category
        category = determine_bmi_category(bmi)

        # Save data to CSV
        save_to_csv(weight, height, bmi, category)

        # Display results
        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"Category: {category}")

    except ValueError as e:
        print(f"Error: {e}. Please enter valid numbers.")

if __name__ == "__main__":
    main()
