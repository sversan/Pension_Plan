import numpy as np
from flask import Flask, render_template

app = Flask(__name__)

# Function to calculate pension contributions
def calculate_contributions(start_salary, end_salary, start_year, end_year, start_contrib, end_contrib):
    years = np.arange(start_year, end_year + 1)
    salary = np.linspace(start_salary, end_salary, len(years))
    contrib_rate = np.linspace(start_contrib, end_contrib, len(years))
    
    pension_contrib = salary * contrib_rate / 100
    living_cost = salary - pension_contrib
    saving_investment = living_cost * 0.2  # Assume 20% of living cost is saved/invested
    
    total_pension = pension_contrib.sum()
    total_living = living_cost.sum()
    total_savings = saving_investment.sum()
    
    return years, salary, pension_contrib, living_cost, saving_investment, total_pension, total_living, total_savings

# Parameters
start_salary = 1100
end_salary = 5000
start_year = 1999
end_year = 2025
start_contrib = 49  # Starting contribution percentage
end_contrib = 39    # Final contribution percentage

# Calculate data
years, salary, pension_contrib, living_cost, saving_investment, total_pension, total_living, total_savings = calculate_contributions(
    start_salary, end_salary, start_year, end_year, start_contrib, end_contrib)

# Webpage route to display results
@app.route('/')
def index():
    return render_template('index.html', years=years, salary=salary, pension_contrib=pension_contrib,
                           living_cost=living_cost, saving_investment=saving_investment,
                           total_pension=total_pension, total_living=total_living, total_savings=total_savings)

if __name__ == '__main__':
    app.run(debug=True)
