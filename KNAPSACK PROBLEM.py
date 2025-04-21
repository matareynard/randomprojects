# Function to solve the Fractional Knapsack Problem
def fractionalKnapsack(W, wt, val, n):
    # Create a list of items with their profit-to-weight ratios
    items = [(val[i], wt[i], val[i] / wt[i]) for i in range(n)]
    # Sort items by their ratio in descending order
    items.sort(key=lambda x: x[2], reverse=True)

    max_profit = 0.0  # To store the maximum profit
    for profit, weight, ratio in items:
        if W >= weight:
            # If the entire item can fit in the knapsack, take it
            W -= weight
            max_profit += profit
        else:
            # If only part of the item can fit, take the fraction that fits
            max_profit += profit * (W / weight)
            break

    return max_profit

# Main program to get user input and call fractionalKnapsack function
if __name__ == '__main__':
    # Input number of items
    n = int(input("Enter the number of items: "))

    # Input the profits (values) for each item
    val = []
    print("Enter the profits for each item:")
    for i in range(n):
        val.append(float(input(f"Profit for item {i + 1}: ")))

    # Input the weights for each item
    wt = []
    print("Enter the weights for each item:")
    for i in range(n):
        wt.append(float(input(f"Weight for item {i + 1}: ")))

    # Input the maximum capacity of the knapsack
    W = float(input("Enter the maximum capacity of the knapsack: "))

    # Call the fractionalKnapsack function and print the result
    max_profit = fractionalKnapsack(W, wt, val, n)
    print(f"The maximum profit is: {max_profit:.2f}")
