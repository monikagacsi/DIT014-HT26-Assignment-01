def validate_reference(reference):
    prefix = "HFL"
    reference = reference.strip().upper()
    # split user input by '-' and removes white spaces
    reference_parts = []
    for i in reference.split('-'):
        reference_parts.append(i.strip()) 

    # check if there are 3 parts, add prefix (HFL) is it's missing
    if len(reference_parts) == 2:
        reference_parts.insert(0, prefix)
    if len(reference_parts) != 3:
        return None
        
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


def calculate_delivery_quote(distance, weight, service_code):
    if service_code == "S":
        service_multiplier = 1.00
    elif service_code == "X":
        service_multiplier = 1.25
    elif service_code == "P":
        service_multiplier = 1.60
    else:
        return None  # Or raise an error rather than silently defaulting to "S"
    
    subtotal = 45.00 + (distance * 6.50) + (weight * 4.00)
    final_price = subtotal * service_multiplier
    return final_price


def consolidate_parcel_labels(parcels):
    raw_parcels = parcels.split(",")
    clean_parcel_list = []
    
    for parcel in raw_parcels:
        clean_parcel = parcel.strip().upper()
        if clean_parcel and clean_parcel not in clean_parcel_list:
            clean_parcel_list.append(clean_parcel)
            
    return clean_parcel_list

def check_van_capacity(van_capacity, parcel_weights):
    remaining_capacity = van_capacity
    accepted_rejected_status = []
    for parcel_weight in parcel_weights:
        if parcel_weight <= remaining_capacity:
            accepted_rejected_status.append(True)
            remaining_capacity = remaining_capacity - parcel_weight
        else:
            accepted_rejected_status.append(False)
    return accepted_rejected_status #an array of Trues and Falses    

    #Validation float input >=0
def non_negative_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            print ("Error - Value must be greater than zero or 0.")
        except ValueError:
            print ("Error - Value must be greater than zero or 0.")

            #Validation integer input >=0:
def non_negative_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
            print("Error - Value must be an integer greater than zero or 0. ")
        except ValueError:
            print("Error - Value must be an integer greater than zero or 0. ")

            #Validation input >0
def positive_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            print("Error - Value must be greater than zero. ")
        except ValueError:
            print("Error - Value must be greater than zero. ")

def classify_service_performance(promised_minutes, actual_minutes, damaged_parcels):
    delay = actual_minutes - promised_minutes
    print(f"Delay: {delay:.0f} minutes")
    if damaged_parcels > 0:
        return "SERVICE FAILURE"
    elif delay <= 0:
        return "ON TIME"
    elif delay <= 15:
        return "MINOR DELAY"
    else:
        return "MAJOR DELAY"
    
def produce_weekly_report (deliveries, daily_target):
    days_of_week = ["Monday","Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    total = 0
    days_meeting_target = 0
    highest_val = deliveries[0]
    highest_day = days_of_week[0]
    lowest_val = deliveries[0]
    lowest_day = days_of_week[0]

    for i in range(len(deliveries)):
        val = deliveries[i]
        total += val

        if val >= daily_target:
            days_meeting_target += 1

        if val >= highest_val:
            highest_val = val
            highest_day = days_of_week[i]


        if val <= lowest_val:
            lowest_val = val
            lowest_day = days_of_week[i]

    average = total/len(deliveries)
    
    return [
        total,
        average,
        highest_day,
        highest_val,
        lowest_day,
        lowest_val,
        days_meeting_target
        ]

def main():
    console_menu = (f'''
    {"Harborflow Dispatch Console".upper()}
    1. Close console
    2. Validate booking reference
    3. Calculate delivery quote
    4. Consolidate parcel labels
    5. Check van capacity
    6. Classify service performance
    7. Produce weekly dispatch report 
    8. Compare service scenarios''')

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
            processed_reference = validate_reference(reference)
            if processed_reference:
                print(f'Valid reference: {processed_reference}')
            else:
                print("Invalid booking reference.")

        elif selected_service == 3:
            # Calculate a delivery quote
            distance = positive_input("Distance (km): ")
            weight = positive_input("Weight (kg): ")

            while True:
                service_code = input("Service code: ").strip().upper()
                if service_code in ["S", "X", "P"]:
                    break
                print("Error: Service code must be S, X or P.")

            quote = calculate_delivery_quote(distance, weight, service_code)
            print(f"Delivery quote: {quote:.2f} SEK")

            
        elif selected_service == 4:
            #Consolidate parcel labels
            parcels_input = input("Scanned labels: ")
            unique_labels = consolidate_parcel_labels(parcels_input)
            
            print("Unique load list:")
            for idx in range(len(unique_labels)):
                print(f"{idx + 1}. {unique_labels[idx]}")
            print(f"Total unique parcels: {len(unique_labels)}")
 

        elif selected_service == 5:
            #Check van capacity
            van_capacity = positive_input("Van capacity (kg): ")

            # Input validation loop for parcel weights
            while True:
                raw_weights = input("Parcel weights (kg): ")

                clean_text = raw_weights.replace(",", " ")
                weight_strings = clean_text.split()
                parcel_weights = []
                
                has_error = False

                # Typecasting to float with error checking
                for weight_str in weight_strings:
                    try:
                        parcel_weights.append(float(weight_str))
                    except ValueError:
                        has_error = True
                        break  

                #All values converted successfully and list is not empty
                if not has_error and len(parcel_weights) > 0:
                    break  
                else:
                    print("Invalid input. All parcel weights must be numeric values. Please try again.")

            output = check_van_capacity(van_capacity,parcel_weights)

            accepted_amount = 0
            loaded_weight = 0.0

            for i in range(len(output)):
                parcel_number = i + 1
                weight = parcel_weights[i]
                status = output[i]

                if status: #true
                    print(f"Parcel {parcel_number}: ACCEPTED")
                    accepted_amount += 1
                    loaded_weight += weight
                else:
                    print(f"Parcel {parcel_number}: REJECTED")

            remaining_capacity = van_capacity - loaded_weight

            print(f"Accepted parcels: {accepted_amount}")
            print(f"Loaded weight: {loaded_weight:.2f} kg")
            print(f"Remaining capacity: {remaining_capacity:.2f} kg")


        elif selected_service == 6:
        #Classify service performance
            promised_minutes = non_negative_float("Promised minutes: ")
            actual_minutes = non_negative_float("Actual minutes: ")
            damaged_parcels = non_negative_integer("Damaged parcels: ")
            print(f"Service status: {classify_service_performance(promised_minutes, actual_minutes, damaged_parcels)}")


        elif selected_service == 7:
            #Produce the weekly dispatch report          
            target_daily = non_negative_integer("Enter daily target: ")

           #validate Deliveries (Loops until exactly 7 values are given)
            while True:
                raw_deliveries = input("Completed deliveries: ")
                clean_text = raw_deliveries.replace(",", " ")
                deliveries_strings = clean_text.split()

                # Check if the user entered exactly 7 values
                if len(deliveries_strings) != 7:
                    print(f"Error: Expected 7 values, but got {len(deliveries_strings)}. Try again.")
                    continue  # Jumps back to the top of the deliveries loop

                #convert strings to integers with safety check
                try:
                    deliveries_numeric = []
                    for i in range(len(deliveries_strings)):
                        n = int(deliveries_strings[i])
                        deliveries_numeric.append(n)
                    
                    #if everything succeeded, break out of the loop
                    break
                except ValueError:
                    print("Error: All values must be whole numbers. Try again.")

            report = produce_weekly_report(deliveries_numeric, target_daily)
            print("Weekly dispatch report")
            print(f"Total deliveries: {report[0]}")
            print(f"Average per day: {report[1]:.2f}")
            print(f"Highest day: {report[2]} ({report[3]})")
            print(f"Lowest day: {report[4]} ({report[5]})")
            print(f"Days meeting target: {report[6]}")

        
        elif selected_service == 8:
            #Compare delivery scenarios
            distance = positive_input("Distance (km): ") #distance shouldnt be 0
            weight = positive_input("Weight (kg): ")
            service_codes = ["S", "X", "P"]
            service_names = ["Standard", "Express", "Priority"]
            
            print("Service comparison")
       
            highest_price = -1
            cheapest_service = ""
            lowest_price = None
            most_expensive_service = ""

            for i in range(len(service_codes)):
                code = service_codes[i]
                name = service_names [i]

                quote = calculate_delivery_quote(distance, weight, code) 
                print(f"{name}: {quote:.2f} SEK")

                if lowest_price is None or quote < lowest_price:
                    lowest_price = quote
                    cheapest_service = name
                if quote > highest_price:
                    highest_price = quote
                    most_expensive_service = name

            print(f"Cheapest service: {cheapest_service}")
            print(f"Most expensive service: {most_expensive_service}")
        else:
            print("Invalid input. Please select a service from the menu.")


if __name__ == "__main__":
    main()