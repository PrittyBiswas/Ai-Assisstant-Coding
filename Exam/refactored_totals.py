# Refactored Repetitive Code into Reusable Function
# Original repetitive code example (before refactoring):
# prices1 = [2.5, 3.0, 1.75]
# total1 = prices1[0] + prices1[1] + prices1[2]
# print(f'Total for first list: ${total1:.2f}')
#
# prices2 = [5.0, 2.25, 3.5, 4.0]
# total2 = prices2[0] + prices2[1] + prices2[2] + prices2[3]
# print(f'Total for second list: ${total2:.2f}')

def calculate_total(prices):
    """
    Calculate the total sum of a list of prices.
    
    Args:
    prices (list of float): List of item prices.
    
    Returns:
    float: The sum of all prices.
    """
    return sum(prices)

# Example usage with two different lists of item prices
prices1 = [2.5, 3.0, 1.75]
prices2 = [5.0, 2.25, 3.5, 4.0]

total1 = calculate_total(prices1)
total2 = calculate_total(prices2)

print(f'Total for first list ({prices1}): ${total1:.2f}')
print(f'Total for second list ({prices2}): ${total2:.2f}')









