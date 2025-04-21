def min_coins(coins, target):
    dp = [float('inf')] * (target + 1)
    dp[0] = 0
    coin_used = [None] * (target + 1)  # To track coins used

    for amount in range(1, target + 1):
        for coin in coins:
            if coin <= amount:
                if dp[amount - coin] + 1 < dp[amount]:
                    dp[amount] = dp[amount - coin] + 1
                    coin_used[amount] = coin  # Track the coin used

    if dp[target] == float('inf'):
        return -1, []  # Impossible to reach target
    
    # Backtrack to find the coins used
    result_coins = []
    while target > 0:
        coin = coin_used[target]
        if coin is None:
            break
        result_coins.append(coin)
        target -= coin

    return dp[len(dp) - 1], result_coins  # Return the minimum count and the coins used

def min_distance_mice_holes(mice, holes):
    mice.sort()
    holes.sort()
    max_distance = 0  # Track the maximum distance any mouse has to travel

    for mouse, hole in zip(mice, holes):
        distance = abs(mouse - hole)
        max_distance = max(max_distance, distance)  # Update max distance if needed

    return max_distance

def display_main_menu():
    print("Please select an option:")
    print("1. Coin Exchange ")
    print("2. Mice and Hole ")
    print("0. Exit")

def main():
    while True:
        display_main_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nCoin Exchange - Minimize Coins")
            coins = list(map(int, input("Enter coin or bill denominations (e.g., 1000 500 20): ").split()))
            target = int(input("Enter the target amount you want to reach: "))
            
            result, result_coins = min_coins(coins, target)
            if result != -1:
                print(f"Minimum coins/bills needed: {result}")
                print(f"Coins used: {result_coins}")
            else:
                print("It is not possible to reach the target with the given denominations.")
        
        elif choice == "2":
            print("\nMice and Hole - Minimize Maximum Distance")
            mice = list(map(int, input("Enter the positions of the mice (e.g., 1 2 3): ").split()))
            holes = list(map(int, input("Enter the positions of the holes (e.g., 4 5 6): ").split()))

            if len(mice) != len(holes):
                print("The number of mice and holes must be equal.")
            else:
                max_distance = min_distance_mice_holes(mice, holes)
                print(f"The minimum possible maximum distance any mouse has to travel is: {max_distance}")

        elif choice == "0":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")
        print()

if __name__ == "__main__":
    main()
