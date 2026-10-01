HARBORFLOW DISPATCH CONSOLE - TEAM README

Run instructions
----------------
Command:
Python version tested: 3.14

Team members and concrete contributions
---------------------------------------
Name: Youyue (Avery)
Contribution:
- Task 6 (Classify service performance )
- Two validation functions(input>0 and input>=0)

Name: Monika
Contribution: 
- implemented task 1 (menu)
- implemented task 2 (booking reference validation)
- implemented task 9  with Olha and Linder


Name: Linder
Contribution:
- Task 3
- Task 4
- Task 9, some code improvements

Name: Olha
Contribution:
- Task 5
- Task 7
- Task 9


Design notes
------------
Main function boundaries:
One function per menu option:
 validate_reference(),
 calculate_delivery_quote(),
 consolidate_parcel_labels(),
 check_van_capacity(),
 classify_service_performance(),
 produce_weekly_report()
The functions compute and return; main() owns the menu loop, input prompts and output formatting

How input validation is organized:
positive_input() and non_negative_input() are reusable loops for numeric prompts
validate_reference() returns None for invalid references
Menu choice, service code, daily target and weekly deliveries are validated with while + try/except in main()

How shared calculations are reused:
calculate_delivery_quote() serves both option 3 and option 8

Known limitations
-----------------
- Classify_service_performance() prints the delay itself, mixing output into a logic function.
- Produce_weekly_report() returns a list, so callers must remember index positions (0 to 6).
- Task 7 completed deliveries accepts negative numbers
- Task 2  Reference booking validation: Validation will show the "Invalid" error message if the user omits the set hfl prefix and starts their input with a special character.
- Task 4  Parcel labels not validated for nonnumeric values.

