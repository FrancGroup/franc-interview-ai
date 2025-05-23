#!/usr/bin/env python3
"""
Bookstore Client

A client application for interacting with the Bookstore API.
This client is intentionally incomplete and contains TODOs for implementation.
"""
import requests
import json
from tabulate import tabulate
import sys
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Constants
API_BASE_URL = "http://localhost:5000/api"
BOOKS_ENDPOINT = f"{API_BASE_URL}/books"

# Helper functions for formatting output
def print_success(message):
    """Print a success message in green."""
    print(f"{Fore.GREEN}{message}{Style.RESET_ALL}")

def print_error(message):
    """Print an error message in red."""
    print(f"{Fore.RED}Error: {message}{Style.RESET_ALL}")

def print_info(message):
    """Print an info message in blue."""
    print(f"{Fore.BLUE}{message}{Style.RESET_ALL}")

def format_book_table(books):
    """Format a list of books as a table."""
    if not books:
        return "No books found."
    
    # Convert single book to list if needed
    if isinstance(books, dict):
        books = [books]
    
    headers = ["ID", "Title", "Author", "Price", "In Stock"]
    rows = [
        [
            book.get("id", "N/A"),
            book.get("title", "N/A"),
            book.get("author", "N/A"),
            f"${book.get('price', 0):.2f}",
            "Yes" if book.get("in_stock", False) else "No"
        ]
        for book in books
    ]
    
    return tabulate(rows, headers=headers, tablefmt="grid")

# API client functions

def get_all_books():
    """Retrieve all books from the API."""
    try:
        response = requests.get(BOOKS_ENDPOINT)
        response.raise_for_status()
        books = response.json()
        return books
    except requests.exceptions.RequestException as e:
        print_error(f"Failed to retrieve books: {e}")
        return []

def display_all_books():
    """Display all books in a formatted table."""
    print_info("Fetching all books...")
    books = get_all_books()
    print(format_book_table(books))

# TODO: Implement the get_book_by_id function
def get_book_by_id(book_id):
    """
    Retrieve a specific book by ID.
    
    Parameters:
        book_id (str): The ID of the book to retrieve
        
    Returns:
        dict: The book data if found, None otherwise
    """
    # TODO: Implement this function
    # 1. Send a GET request to the appropriate endpoint
    # 2. Handle any errors that might occur
    # 3. Return the book data if successful
    pass

def display_book_details():
    """Display details for a specific book."""
    book_id = input("Enter book ID: ")
    
    # TODO: Implement this functionality
    # 1. Call get_book_by_id function
    # 2. Display the book details or error message
    print_error("This functionality is not implemented yet.")

# TODO: Implement the add_book function
def add_book():
    """
    Add a new book to the bookstore.
    
    Gather book details from the user and send them to the API.
    """
    # TODO: Implement this function
    # 1. Gather book information from the user (title, author, price, in_stock)
    # 2. Validate the inputs
    # 3. Send a POST request to the appropriate endpoint
    # 4. Handle any errors and display appropriate messages
    print_error("This functionality is not implemented yet.")

# TODO: Implement the update_book function
def update_book():
    """
    Update an existing book's information.
    
    Retrieve the current book information and allow the user to modify it.
    """
    # TODO: Implement this function
    # 1. Ask for the book ID to update
    # 2. Fetch the current book information
    # 3. Allow the user to update each field (or keep existing values)
    # 4. Send a PUT request to the appropriate endpoint
    # 5. Handle any errors and display appropriate messages
    print_error("This functionality is not implemented yet.")

# TODO: Implement the delete_book function
def delete_book():
    """
    Delete a book from the bookstore.
    
    Ask for confirmation before deleting.
    """
    # TODO: Implement this function
    # 1. Ask for the book ID to delete
    # 2. Ask for confirmation (y/n)
    # 3. Send a DELETE request to the appropriate endpoint
    # 4. Handle any errors and display appropriate messages
    print_error("This functionality is not implemented yet.")

# TODO: Implement the search_books function
def search_books():
    """
    Search for books by title or author.
    
    Send a search query to the API and display the results.
    """
    # TODO: Implement this function
    # 1. Ask for the search query
    # 2. Validate the query (not empty)
    # 3. Send a GET request to the search endpoint with the query as a parameter
    # 4. Handle any errors and display appropriate messages or search results
    print_error("This functionality is not implemented yet.")

def display_menu():
    """Display the main menu options."""
    print("\n" + "=" * 50)
    print("             BOOKSTORE CLIENT              ")
    print("=" * 50)
    print("1. View All Books")
    print("2. View Book Details")
    print("3. Add New Book")
    print("4. Update Book")
    print("5. Delete Book")
    print("6. Search Books")
    print("7. Exit")
    print("=" * 50)

def main():
    """Main application function."""
    try:
        while True:
            display_menu()
            choice = input("Enter your choice (1-7): ")
            
            if choice == "1":
                display_all_books()
            elif choice == "2":
                display_book_details()
            elif choice == "3":
                add_book()
            elif choice == "4":
                update_book()
            elif choice == "5":
                delete_book()
            elif choice == "6":
                search_books()
            elif choice == "7":
                print_info("Exiting Bookstore Client. Goodbye!")
                break
            else:
                print_error("Invalid choice. Please enter a number between 1 and 7.")
            
            input("\nPress Enter to continue...")
            
    except KeyboardInterrupt:
        print_info("\nApplication terminated by user.")
    except Exception as e:
        print_error(f"An unexpected error occurred: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main()) 