import numpy as np
import matplotlib.pyplot as plt

def simulate_profit(unit_cost, retail_price, disposal_cost, num_manufactured, 
                    num_simulations=1000, tax_uncertainty=False):
    # List to store profit for each simulation
    profits = [] 
    for i in range(num_simulations):
        # Generate random demand from N(150, 20)
        demand = np.random.normal(150, 20)
        demand = max(0, demand)  
        
        current_disposal_cost = disposal_cost
        if tax_uncertainty:
            additional_tax = np.random.choice([True, False], p=[0.5, 0.5])
            if additional_tax:
                current_disposal_cost = 17.0  # Disposal cost with tax
        
        units_sold = min(demand, num_manufactured)
        # Calculate units unsold
        units_unsold = max(0, num_manufactured - demand)
        revenue = units_sold * retail_price
        manufacturing_cost = num_manufactured * unit_cost
        disposal_cost_total = units_unsold * current_disposal_cost  
        profit = revenue - manufacturing_cost - disposal_cost_total
        profits.append(profit)
    # Calculate statistics
    mean_profit = np.mean(profits)
    std_profit = np.std(profits)
    return mean_profit, std_profit, profits

def find_optimal_quantity(unit_cost, retail_price, disposal_cost, 
                         min_qty=0, max_qty=230, tax_uncertainty=False):
    all_results = {}
    max_profit = float('-inf')
    optimal_qty = 0
    print(f"Testing manufacturing quantities from {min_qty} to {max_qty}...")
    print("-" * 70)
    for qty in range(min_qty, max_qty + 1):
        mean_profit, std_profit, _ = simulate_profit(
            unit_cost, retail_price, disposal_cost, qty, 
            num_simulations=1000, tax_uncertainty=tax_uncertainty
        )
        all_results[qty] = {
            'mean_profit': mean_profit,
            'std_profit': std_profit
        }
        if mean_profit > max_profit:
            max_profit = mean_profit
            optimal_qty = qty
    
    return optimal_qty, max_profit, all_results


# QUESTION 1: Base Case (No Tax Uncertainty)
print("=" * 70)
print("QUESTION 1: OPTIMAL MANUFACTURING QUANTITY (BASE CASE)")
print("=" * 70)

# Parameters
unit_cost = 28.50
retail_price = 150.00
disposal_cost = 8.50

# Find optimal quantity
optimal_qty_q1, max_profit_q1, results_q1 = find_optimal_quantity(
    unit_cost, retail_price, disposal_cost, 
    min_qty=0, max_qty=230, tax_uncertainty=False
)

print(f"\nOptimal Manufacturing Quantity: {optimal_qty_q1} units")
print(f"Expected Profit: ${max_profit_q1:,.2f}")
print(f"Expected Profit Std Dev: ${results_q1[optimal_qty_q1]['std_profit']:,.2f}")

# Show profit for quantities around the optimal
print("\nProfit for quantities near optimal:")
print("-" * 70)
print(f"{'Quantity':<12} {'Mean Profit':<20} {'Std Deviation':<20}")
print("-" * 70)
for qty in range(max(0, optimal_qty_q1 - 5), min(231, optimal_qty_q1 + 6)):
    mean_p = results_q1[qty]['mean_profit']
    std_p = results_q1[qty]['std_profit']
    marker = " <-- OPTIMAL" if qty == optimal_qty_q1 else ""
    print(f"{qty:<12} ${mean_p:<18,.2f} ${std_p:<18,.2f}{marker}")

# BONUS QUESTION: With Tax Uncertainty
print("\n" + "=" * 70)
print("BONUS QUESTION: OPTIMAL QUANTITY WITH TAX UNCERTAINTY")
print("=" * 70)
print("50% chance disposal cost increases from $8.50 to $17.00")
print("-" * 70)

# Find optimal quantity with tax uncertainty
optimal_qty_bonus, max_profit_bonus, results_bonus = find_optimal_quantity(
    unit_cost, retail_price, disposal_cost, 
    min_qty=0, max_qty=230, tax_uncertainty=True
)

print(f"\nOptimal Manufacturing Quantity: {optimal_qty_bonus} units")
print(f"Expected Profit: ${max_profit_bonus:,.2f}")
print(f"Expected Profit Std Dev: ${results_bonus[optimal_qty_bonus]['std_profit']:,.2f}")

# Show profit for quantities around the optimal
print("\nProfit for quantities near optimal:")
print("-" * 70)
print(f"{'Quantity':<12} {'Mean Profit':<20} {'Std Deviation':<20}")
print("-" * 70)
for qty in range(max(0, optimal_qty_bonus - 5), min(231, optimal_qty_bonus + 6)):
    mean_p = results_bonus[qty]['mean_profit']
    std_p = results_bonus[qty]['std_profit']
    marker = " <-- OPTIMAL" if qty == optimal_qty_bonus else ""
    print(f"{qty:<12} ${mean_p:<18,.2f} ${std_p:<18,.2f}{marker}")

# VISUALIZATION
print("\n" + "=" * 70)
print("GENERATING VISUALIZATION...")
print("=" * 70)
# Create visualization comparing both scenarios
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
# Plot 1: Base Case
quantities_q1 = list(results_q1.keys())
profits_q1 = [results_q1[q]['mean_profit'] for q in quantities_q1]
ax1.plot(quantities_q1, profits_q1, 'b-', linewidth=2)
ax1.axvline(x=optimal_qty_q1, color='r', linestyle='--', linewidth=2, 
            label=f'Optimal: {optimal_qty_q1} units')
ax1.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
ax1.set_xlabel('Manufacturing Quantity', fontsize=12)
ax1.set_ylabel('Expected Profit ($)', fontsize=12)
ax1.set_title('Question 1: Base Case\n(No Tax Uncertainty)', fontsize=14, fontweight='bold')
ax1.grid(True, alpha=0.3)
ax1.legend()
# Plot 2: Bonus Case with Tax
quantities_bonus = list(results_bonus.keys())
profits_bonus = [results_bonus[q]['mean_profit'] for q in quantities_bonus]

ax2.plot(quantities_bonus, profits_bonus, 'g-', linewidth=2)
ax2.axvline(x=optimal_qty_bonus, color='r', linestyle='--', linewidth=2, 
            label=f'Optimal: {optimal_qty_bonus} units')
ax2.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
ax2.set_xlabel('Manufacturing Quantity', fontsize=12)
ax2.set_ylabel('Expected Profit ($)', fontsize=12)
ax2.set_title('Bonus Question: With Tax Uncertainty\n(50% chance disposal cost = $17)', 
              fontsize=14, fontweight='bold')
ax2.grid(True, alpha=0.3)
ax2.legend()
plt.tight_layout()
plt.savefig('twoplus_earbuds_analysis.png', dpi=300, bbox_inches='tight')
print("\nVisualization saved as 'twoplus_earbuds_analysis.png'")
# COMPARISON SUMMARY
print("\n" + "=" * 70)
print("COMPARISON SUMMARY")
print("=" * 70)
print(f"{'Scenario':<30} {'Optimal Qty':<15} {'Expected Profit':<20}")
print("-" * 70)
print(f"{'Base Case (Q1)':<30} {optimal_qty_q1:<15} ${max_profit_q1:,.2f}")
print(f"{'With Tax Uncertainty (Bonus)':<30} {optimal_qty_bonus:<15} ${max_profit_bonus:,.2f}")
print(f"{'Difference':<30} {optimal_qty_bonus - optimal_qty_q1:<15} "
      f"${max_profit_bonus - max_profit_q1:,.2f}")
print("=" * 70)