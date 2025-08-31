import subprocess
import sys
import os
import time

def display_banner():
    
    text_to_display = "strattatat"

    print("\n" + "="*50)
    print(" Displaying script banner...".center(50))
    print("="*50 + "\n")

    # Check if figlet is available
    try:
        subprocess.run(["figlet", "-v"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        figlet_available = True
    except (subprocess.CalledProcessError, FileNotFoundError):
        figlet_available = False
        print("Warning: figlet not found. Skipping figlet display.", file=sys.stderr)

    # Check if toilet is available
    try:
        subprocess.run(["toilet", "-v"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        toilet_available = True
    except (subprocess.CalledProcessError, FileNotFoundError):
        toilet_available = False
        print("Warning: toilet not found. Skipping toilet display.", file=sys.stderr)

    if figlet_available and toilet_available:
        try:
                       
            
            print("--- TOILET (Rainbow Metal) ---")
            subprocess.run(["toilet", "--gay", "-F", "metal", "-t", text_to_display], check=True)
            time.sleep(0.5) # Pause for effect

            
            print("\n--- FIGLET (Standard) + TOILET (Blue) ---")
            figlet_output = subprocess.check_output(["figlet", "-f", "standard", text_to_display], text=True)
            # Pipe figlet output to toilet for coloring
            subprocess.run(["toilet", "--color", "blue", "-t"], input=figlet_output, text=True, check=True)
            time.sleep(0.5)

           
            print("\n--- TOILET (Block Font, White on Red) ---")
            subprocess.run(["toilet", "-f", "block", "--bg=red", "--fg=white", "-t", text_to_display], check=True)
            
        except subprocess.CalledProcessError as e:
            print(f"Error executing figlet/toilet: {e}", file=sys.stderr)
        except Exception as e:
            print(f"An unexpected error occurred during banner display: {e}", file=sys.stderr)
    elif figlet_available:
        print("\n--- FIGLET (Standard) ---")
        try:
            subprocess.run(["figlet", "-f", "standard", text_to_display], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error executing figlet: {e}", file=sys.stderr)
    elif toilet_available:
        print("\n--- TO

import webbrowser
import urllib.parse
import time

def construct_google_dork():
    """
    Guides the user through constructing a Google Dork query.
    """
    dork_parts = []
    print("Let's construct your Google Dork query!")
    print("Answer the following questions to build your search.")
    print("-" * 50)

    # Site search
    site = input("Search within a specific site or domain? (e.g., example.com, gov) (Leave blank to skip): ").strip()
    if site:
        dork_parts.append(f"site:{site}")

    # File type search
    filetype = input("Search for a specific file type? (e.g., pdf, docx, xls, txt) (Leave blank to skip): ").strip()
    if filetype:
        dork_parts.append(f"filetype:{filetype}")

    # Inurl search
    inurl = input("Search for specific text in the URL? (e.g., admin, login, backup) (Leave blank to skip): ").strip()
    if inurl:
        dork_parts.append(f"inurl:{inurl}")

    # Intitle search
    intitle = input("Search for specific text in the title of the page? (e.g., 'index of', 'passwords') (Leave blank to skip): ").strip()
    if intitle:
        dork_parts.append(f"intitle:\"{intitle}\"") # Using quotes for multi-word titles

    # Intext search
    intext = input("Search for specific text within the page body? (e.g., 'confidential', 'email addresses') (Leave blank to skip): ").strip()
    if intext:
        dork_parts.append(f"intext:\"{intext}\"") # Using quotes for multi-word text

    # Exact phrase search
    exact_phrase = input("Search for an exact phrase? (e.g., 'private key') (Leave blank to skip): ").strip()
    if exact_phrase:
        dork_parts.append(f"\"{exact_phrase}\"")

    # Words to include (AND operator implied)
    include_words = input("Enter keywords to *include* (space-separated, e.g., 'user list', 'vulnerable server') (Leave blank to skip): ").strip()
    if include_words:
        # Split by space and add each as a separate part, implicitly ANDed by Google
        dork_parts.extend(include_words.split())

    # Words to exclude (-)
    exclude_words = input("Enter keywords to *exclude* (space-separated, e.g., 'public', 'demo') (Leave blank to skip): ").strip()
    if exclude_words:
        for word in exclude_words.split():
            dork_parts.append(f"-{word}")
            
    # Other advanced operators (e.g., cache:, related:, AROUND(), etc.) - Optional advanced input
    # This gives the user flexibility to add anything not covered
    other_operators = input("Any other specific Google Dork operators or keywords you want to add? (e.g., cache:example.com, 'password' AROUND(5) 'file') (Leave blank to skip): ").strip()
    if other_operators:
        dork_parts.append(other_operators)


    print("-" * 50)
    
    if not dork_parts:
        print("No dork components were entered. The resulting query will be empty.")
        return ""

    final_dork = " ".join(dork_parts).strip()
    return final_dork

def main():
    """
    Main function to run the Dork construction and search process.
    """
    print("Google Dork Assistant v1.0")
    print("This tool helps you build advanced Google search queries (Dorks).")
    print("=" * 60)

    constructed_dork = construct_google_dork()

    if constructed_dork:
        print("\n" + "=" * 60)
        print("Your Constructed Google Dork:")
        print(f"\n   >>> {constructed_dork} <<<\n")
        print("=" * 60)

        search_choice = input("Do you want to perform this search in Google now? (yes/no): ").strip().lower()

        if search_choice == 'yes':
            print("\nOpening Google search results in your default web browser...")
            search_url = f"https://www.google.com/search?q={urllib.parse.quote_plus(constructed_dork)}"
            try:
                webbrowser.open_new_tab(search_url)
                print("Search initiated. Please check your browser.")
            except webbrowser.Error as e:
                print(f"Error opening browser: {e}")
                print(f"You can manually search by copying this URL: {search_url}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                print(f"You can manually search by copying this URL: {search_url}")
        else:
            print("\nSearch not performed. You can copy the dork and use it manually.")
    else:
        print("No dork was constructed.")

    print("\nThank you for using the Google Dork Assistant!")

if __name__ == "__main__":
    main()
