def display_main_menu():
    """Display the main menu options."""
    print("\nSIM 1")
    print("1. Safaricom")
    print("2. M-PESA")
    choice = input("Enter your choice: ")
    return choice

def display_mpesa_menu():
    """Display the M-PESA submenu options."""
    print("\nSIM 1 - M-PESA")
    print("1. Send Money")
    print("2. Withdraw Cash")
    print("3. Buy Airtime")
    print("4. Loans and Savings")
    print("5. Lipa na M-PESA")
    print("6. My Account")
    choice = input("Enter your choice: ")
    return choice

def send_money():
    """Handle the Send Money option."""
    phone_number = input("Enter Phone Number:\n(Digits 0-9, *, #, +)\n10-13 characters: ")
    
    
    if validate_phone_number(phone_number):
        print(f"Sending money to {phone_number}...")
        
        input("Press Enter to return to the M-PESA menu...")
    else:
        print("Invalid phone number. Please try again.")
        send_money()  

def validate_phone_number(phone_number):
    """Validate the phone number format."""
    if len(phone_number) < 10 or len(phone_number) > 13:
        return False
    return all(char.isdigit() or char in ['*', '#', '+'] for char in phone_number)

def main():
    """Main function to run the CLI simulation."""
    while True:
        main_choice = display_main_menu()
        
        if main_choice == '1':
            print("Safaricom selected. (Functionality not implemented yet.)")
            input("Press Enter to return to the main menu...")
        elif main_choice == '2':
            while True:
                mpesa_choice = display_mpesa_menu()
                
                if mpesa_choice == '1':
                    send_money()
                elif mpesa_choice in ['2', '3', '4', '5', '6']:
                    print(f"Option {mpesa_choice} selected. (Functionality not implemented yet.)")
                    input("Press Enter to return to the M-PESA menu...")
                else:
                    print("Invalid choice. Please try again.")
        
        else:
            print("Exiting the program.")
            break

if __name__ == "__main__":
    main()