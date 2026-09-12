"""HarborFlow Assignment 1 starter file.

Replace the TODO sections with your team's implementation. Keep the program
entry point so the file can be run with: python harborflow_app.py
"""

def validate_reference(reference):
    prefix = "HFL"
    reference=reference.strip().upper()
    # split user input by '-' and removes white spaces
    reference_parts=[i.strip() for i in reference.split('-')]


    # check if there are 3 parts, add prefix (HFL) is it's missing
    if len(reference_parts) == 2:
        reference_parts.insert(0, prefix)
    if len(reference_parts) != 3:
        return None
        
    #split input into 3 parts
    part1, part2, part3 = reference_parts

    # check if prefix is correct, part2 only contains characters, part3 only contains integers
    if part1 != prefix:
        return None
    if len(part2) != 3 or not part2.isalpha(): #length is 3, and part2 only has characters
        return None
    if len(part3) != 4 or not part3.isdigit(): #length is 4, and part3 only has digits
        return None
    output = f'{part1}-{part2}-{part3}'
    return output


def main():
    console_menu = (f'''
    {"Harborflow Dispatch Console".upper()}
    1. Close console
    2. Validate booking reference
    3. Calculate delivery quote
    4. Consolidate parcel labels
    5. Check van capacity
    6. Classify service performance
    7. Produce weekly dispatch report ''')

    while True:
        print(console_menu)
        user_input = input("Select service: ")

        try:
            selected_service = int(user_input)
        except ValueError:
            print("Invalid input. Please enter a number from the menu.")
            continue

        if selected_service == 1:
            #Close console
            print("Console closed. Dispatch data remains safe.")
            break
        elif selected_service == 2:
            #Validate booking reference = HFL-CCC-NNNN
            reference = input("Booking reference: ")
            processed_reference=validate_reference(reference)
            if processed_reference:
                print(f'Valid reference:  {processed_reference}')
            else:
                print("Invalid booking reference.")
        elif selected_service == 3:
            #Calculate delivery quote
            pass
        elif selected_service == 4:
            #Consolidate parcel labels
            pass
        elif selected_service == 5:
            #Check van capacity
            pass
        elif selected_service == 6:
            #Classify service performance
            pass
        elif selected_service == 7:
            #Produce weekly dispatch report
            pass
        else:
            print("Invalid input. Please select a service from the menu.")


            '''if __name__ == "__main__":'''
            #main()


main()
