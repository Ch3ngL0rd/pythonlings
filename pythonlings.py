from rich.console import Console
from rich.table import Table

#       I would get so good at them,
#       that solving a simple binary search
#       feels as easy as writing a for loop
#       - Neetcode on DS/A

# These exercises are meant to be solved daily

# Arrays:
#   Two pointers
#       Valid Palindrome (easy)
#       Container with most water (medium)
#   Stack
#       Valid Parentheses (easy)
#   Binary Search
#       Binary Search (easy)
#   Sliding Window
#       Best time to buy and sell stock (easy)
#       Longest Substring Without Repeating Characters (medium)

# Linked List:
#       Create a linked list class
#       Reverse a linked list (easy)

# Trees:
#       Create a tree class
#       Maximum Depth of Binary Tree (easy)
#       Inorder Traversal (medium)
#       Row level traversal (medium)


# sliding window, prefix sum, binary Search
# Decision Tree: Binary Tree, Backtracking, Dyanmic Programming
# Graphs: DFS, BFS, Adjacency list, adjacnecy matrix
# Hashmap: build an adjacency list
#   Contains Duplicate, top k elements
# Heap:

class Pythonlings:
    class Arrays:
        class TwoPointers:
            # Example:
            #   racecar -> True
            #   race a car -> False
            #   a -> True
            #   ab -> False
            # Return True if the string is a valid palindrome, else return False
            @staticmethod
            def valid_palindrome(string) -> bool:
                # Implement logic to check if a string is a valid palindrome
                pass

            # https://leetcode.com/problems/container-with-most-water/
            # Example:
            #   [1, 2, 3, 4, 5] -> 6 : 3->5 has a width of 2 and height of 3
            #   [1, 8, 6, 2, 5, 4, 8, 3, 7] -> 49 : 2->7 has a width of 7 and height of 7
            # Return the max volume of water that can be contained
            @staticmethod
            def container_with_most_water(array) -> int:
                # Implement logic to find the container with most water
                pass

        class Stack:
            # https://leetcode.com/problems/valid-parentheses/
            # Example:
            #   () -> True
            #   ()[]{} -> True
            #   (] -> False
            #   ([)] -> False
            # Return True if the string has valid parentheses, else return False
            @staticmethod
            def valid_parentheses(string) -> bool:
                # Implement logic to check if a string has valid parentheses
                pass

        class BinarySearch:
            # https://leetcode.com/problems/binary-search/
            # Example:
            #  [-1, 0, 3, 5, 9, 12], 9 -> 4
            #  [-1, 0, 3, 5, 9, 12], 2 -> -1
            # Return the index of the target if it exists, else return -1
            @staticmethod
            def binary_search(array, target) -> int:
                # Implement binary search algorithm
                pass

        class SlidingWindow:
            # https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
            # Example:
            #   [7, 1, 5, 3, 6, 4] -> 5 : buy at 1 and sell at 6
            #   [7, 6, 4, 3, 1] -> 0 : no transaction
            # Return the max profit that can be made by buying and selling stock
            @staticmethod
            def best_time_to_buy_and_sell_stock(array) -> int:
                # Implement logic to find the best time to buy and sell stock
                pass

            # https://leetcode.com/problems/longest-substring-without-repeating-characters/
            # Example:
            #   abcabcbb -> 3 : abc
            #   bbbbb -> 1 : b
            #   pwwkew -> 3 : wke
            # Return the length of the longest substring without repeating characters
            @staticmethod
            def longest_substring_without_repeating_characters(string) -> int:
                # Implement logic to find the longest substring without repeating characters
                pass

    @classmethod
    def test_algorithms(cls):
        # Tests all the algorithms
        results = []
        # Two Pointers
        # Tests for valid palindrone
        results.append(["Two Pointers: Valid Palindrome", "racecar",
                       True, cls.Arrays.TwoPointers.valid_palindrome("racecar")])
        results.append(["Two Pointers: Valid Palindrome", "a",
                       True, cls.Arrays.TwoPointers.valid_palindrome("a")])
        results.append(["Two Pointers: Valid Palindrome", "ab",
                       False, cls.Arrays.TwoPointers.valid_palindrome("ab")])
        results.append(["Two Pointers: Valid Palindrome", "bab",
                       True, cls.Arrays.TwoPointers.valid_palindrome("bab")])
        results.append(["Two Pointers: Valid Palindrome", "",
                       True, cls.Arrays.TwoPointers.valid_palindrome("")])

        # Tests for container with most water
        results.append(["Two Pointers: Container with most water", [
                       1, 2, 3, 4, 5], 6, cls.Arrays.TwoPointers.container_with_most_water([1, 2, 3, 4, 5])])
        results.append(["Two Pointers: Container with most water", [1, 8, 6, 2, 5, 4, 8, 3, 7],
                       49, cls.Arrays.TwoPointers.container_with_most_water([1, 8, 6, 2, 5, 4, 8, 3, 7])])
        results.append(["Two Pointers: Container with most water", [
                       1, 1], 1, cls.Arrays.TwoPointers.container_with_most_water([1, 1])])
        results.append(["Two Pointers: Container with most water", [
                       4, 3, 2, 1, 4], 16, cls.Arrays.TwoPointers.container_with_most_water([4, 3, 2, 1, 4])])

        # Stack
        # Tests for valid parentheses
        results.append(["Stack: Valid Parentheses", "()", True,
                       cls.Arrays.Stack.valid_parentheses("()")])
        results.append(["Stack: Valid Parentheses", "()[]{}",
                       True, cls.Arrays.Stack.valid_parentheses("()[]{}")])
        results.append(["Stack: Valid Parentheses", "(]", False,
                       cls.Arrays.Stack.valid_parentheses("(]")])
        results.append(["Stack: Valid Parentheses", "([)]", False,
                       cls.Arrays.Stack.valid_parentheses("([)]")])
        results.append(["Stack: Valid Parentheses",
                       "{[]}", True, cls.Arrays.Stack.valid_parentheses("{[]}")])
        results.append(["Stack: Valid Parentheses", ")[)]", False,
                       cls.Arrays.Stack.valid_parentheses(")[)]")])

        # Binary Search
        # Tests for binary search
        results.append(["Binary Search: Binary Search", [-1, 0, 3, 5, 9, 12],
                       9, cls.Arrays.BinarySearch.binary_search([-1, 0, 3, 5, 9, 12], 9)])
        results.append(["Binary Search: Binary Search", [-1, 0, 3, 5, 9, 12],
                       2, cls.Arrays.BinarySearch.binary_search([-1, 0, 3, 5, 9, 12], 2)])
        results.append(["Binary Search: Binary Search", [-1, 0, 3, 5, 9, 12],
                       12, cls.Arrays.BinarySearch.binary_search([-1, 0, 3, 5, 9, 12], 12)])
        results.append(["Binary Search: Binary Search", [-1, 0, 3, 5, 9, 12], -1,
                       cls.Arrays.BinarySearch.binary_search([-1, 0, 3, 5, 9, 12], -1)])

        # Sliding Window
        # Tests for best time to buy and sell stock
        results.append(["Sliding Window: Best Time to Buy and Sell Stock", [
                       7, 1, 5, 3, 6, 4], 5, cls.Arrays.SlidingWindow.best_time_to_buy_and_sell_stock([7, 1, 5, 3, 6, 4])])
        results.append(["Sliding Window: Best Time to Buy and Sell Stock", [
                       7, 6, 4, 3, 1], 0, cls.Arrays.SlidingWindow.best_time_to_buy_and_sell_stock([7, 6, 4, 3, 1])])
        results.append(["Sliding Window: Best Time to Buy and Sell Stock", [
                       2, 4, 1], 2, cls.Arrays.SlidingWindow.best_time_to_buy_and_sell_stock([2, 4, 1])])
        results.append(["Sliding Window: Best Time to Buy and Sell Stock", [
                       3, 2, 6, 5, 0, 3], 4, cls.Arrays.SlidingWindow.best_time_to_buy_and_sell_stock([3, 2, 6, 5, 0, 3])])

        # Tests for longest substring without repeating characters
        results.append(["Sliding Window: Longest Substring Without Repeating Characters", "abcabcbb",
                       3, cls.Arrays.SlidingWindow.longest_substring_without_repeating_characters("abcabcbb")])
        results.append(["Sliding Window: Longest Substring Without Repeating Characters", "bbbbb",
                       1, cls.Arrays.SlidingWindow.longest_substring_without_repeating_characters("bbbbb")])
        results.append(["Sliding Window: Longest Substring Without Repeating Characters", "pwwkew",
                       3, cls.Arrays.SlidingWindow.longest_substring_without_repeating_characters("pwwkew")])
        results.append(["Sliding Window: Longest Substring Without Repeating Characters", "",
                       0, cls.Arrays.SlidingWindow.longest_substring_without_repeating_characters("")])
        results.append(["Sliding Window: Longest Substring Without Repeating Characters", " ",
                       1, cls.Arrays.SlidingWindow.longest_substring_without_repeating_characters(" ")])

        cls.print_results(results)

    @staticmethod
    def print_results(results):
        console = Console()
        grouped_results = {}

        # Group results by function name
        for test in results:
            func_name = test[0]
            if func_name not in grouped_results:
                grouped_results[func_name] = []
            grouped_results[func_name].append(test)

        # Define a consistent column width for all tables
        column_width = 20

        # Process and print results
        for func_name, tests in grouped_results.items():
            all_passed = all(test[2] == test[3] for test in tests)

            # Create table for each function
            table = Table(
                title=f"[bold underline]{func_name}[/bold underline]", title_justify="left")
            table.add_column("Input", width=column_width)
            table.add_column("Expected", width=column_width)
            table.add_column("Result", width=column_width)
            table.add_column("Status", width=column_width, justify="right")

            for test in tests:
                status = "[bold green]Passed[/bold green]" if test[2] == test[3] else "[bold red]Failed[/bold red]"
                table.add_row(str(test[1]), str(test[2]), str(test[3]), status)

            if all_passed:
                table.caption = "[bold green]All tests passed! :thumbs_up:[/bold green]"
            else:
                table.caption = "[bold red]Some tests failed[/bold red]"

            console.print(table)


if __name__ == "__main__":
    Pythonlings.test_algorithms()
