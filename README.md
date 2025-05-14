Point Distribution:

Working commands :
get_movie() : 4 points
delete_movie() : 4 points
add_movie() : 4 points
get_movies_by_minutes(): 4 points
display_movies_by_minutes() : 4 points
CSE/ISE 337 - Scripting Languages
Problem 2 [20 points] (Utsha)
In this exercise, you'll create a Future Value program that allows you to make two side-by-side
calculations in the same window. When you're done, the GUI should look like this:
Requirements:
● Inputs: Each calculation panel should include the following inputs:
○ Monthly Investment: The fixed amount invested each month
○ Yearly Interest Rate: The annual interest rate.
○ Years: The total number of years the investment will grow.
● Outputs: Each calculation panel should display:
○ Future Value: The total value of the investment at the end of the
given period, including compounded interest.
● Buttons:
○ Each panel must have Clear and Calculate buttons:
■ Clear: Resets all fields in the respective panel.
■ Calculate: Computes the future value based on the provided
inputs for that panel.
○ A separate Exit button to close the application.
○ A separate Clear All button that clears all input values.
● Functionality:
○ Ensure that the computed future value is displayed in a read-only field
to prevent user modification.
○ Input values for each panel should not affect the calculations in the
another panel.
● Error Handling:
○ Display appropriate error messages if the user provides invalid inputs
CSE/ISE 337 - Scripting Languages

(e.g., non-numeric values or negative numbers).
Review the starter code (Problem2.tar) for the application. You will submit your final
code as Problem2.zi
Point Distribution:

The student’s implementation sufficiently resembles the sample shown above. Does
not have to be exact: 5 points
Clear button : 3 points
Clear All button : 3 points
Calculate button : 3 points
Exit button: 3 points
The side-by-side calculators work separately : 3 points
CSE/ISE 337 - Scripting Languages
Problem 3 [25] (Kushal)
Develop a GUI version of the Fuel Efficiency program. When you're done, the
GUI should look like one of the following based on the Measurement Mode:
The program should compute the Miles Per Gallon (MPG) or Liters
Per 100 KM(L/ 100 km) using the formulas:
CSE/ISE 337 - Scripting Languages

or
Requirements:
● Inputs:
○ A distance text field to accept “Miles Driven” or “Kilometers Driven” as
input.
○ A fuel consumption text field to accept “Gallons of Gas Used” or “Liters of
Fuel Used” as input.
○ A toggle/drop-down mode field to select “US(MPG)” or
“Metric(L/ 100 km)”.
● Outputs:
○ A read-only result text field that displays either ( 1 ) the computed
Miles Per Gallon rounded to two decimal places, or ( 2 ) the
computed Liters Per 100 KM rounded to two decimal places,
depending on US mode or Metric mode, respectively.
● Button:
○ A button labeled "Calculate" which computes the MPG or L/ 100 km
based on the provided inputs when clicked.
○ A button labeled “Clear” which clears all input and output fields and
resets them to default (default for Mode will be “US(MPG)”).
● Functionality:
Initial Start of Program + On Changing Modes:
○ The Mode should be set to a default value of “US(MPG)”, with input
and output labels reflecting US mode appropriately, with distance
and fuel inputs being “Miles Driven” and “Gallons of Gas Used” and
output being “Miles Per Gallon”.
○ When the user toggles/changes the mode (to “Metric(L/ 100 km)” for
example), the input and output labels should update to reflect the
CSE/ISE 337 - Scripting Languages

new (Metric) Mode, with distance and fuel inputs being
“Kilometers Driven” and “Liters of Fuel Used” and output being
“Liters Per 100 KM”.
When the "Calculate" button is clicked:
○ The program should read the values entered for the distance and
fuel consumption input fields.
○ It should calculate the MPG or L/ 100 km and display the result in the
read-only output field.
● Error Handling:
○ Ensure the program gracefully handles invalid or empty input values
(e.g., non-numeric input or division by zero).
Review the starter code for the problem, Problem 3 .tar. You will submit the
final code as Problem 3 .zip.
Problem 4 [25 points] (Web Scraping: Extracting
Headlines) (Kushal)
Develop a Python script to scrape the top headlines from the BBC News website
(https://www.bbc.com).
Requirements:
Inputs:
● Use Python's requests library to fetch the content of the webpage.
● Use BeautifulSoup to parse the webpage's HTML.
Outputs:
● Extract and display the following for each headline:
○ The headline text.
○ The corresponding link (absolute URL).
○ The absolute date (metadata for date last updated) [Date format to
display as (with description for each field in parentheses) = Month(string
CSE/ISE 337 - Scripting Languages

with first letter of abbreviated month name capital) day-of-month( 1 - 31 )
year(YYYY)].
○ If the date last updated is displayed relatively (as within
minutes/hours/days), use the current date to figure out the absolute
date the headline was last updated.
○ Otherwise if the date last updated is already displayed absolutely
[following the website’s given format = day-of-month( 1 - 31 )
Month(string with first letter of abbreviated month name capital)
year(YYYY)], simply parse each of these fields and display them using
the format defined in this bullet’s parent bullet for absolute date.
○ The tag (metadata for tag or genre).
● Display the extracted headlines in a clean, numbered format.
Functionality:
Your program should:

Fetch the BBC homepage (https://www.bbc.com).
Extract and display a list of top headlines and their corresponding links, dates
last updated, and tags.
Ensure that links are displayed as complete URLs (e.g., convert relative links to
absolute URLs).
Ensure that the dates last updated are displayed as absolute dates according
to the defined format (e.g, convert relative dates to absolute dates).
Submission Requirements:
Submit the completed scraper_helper.py file with the missing functions
implemented.
Submit the completed scrape_headlines.py file with the logic to fetch,
extract, and display headlines.
CSE/ISE 337 - Scripting Languages
Error Handling:
● Gracefully handle invalid webpage requests (e.g., server errors or
connection issues).
● Ensure the program doesn't crash if no headlines are found.
Review the starter code for this problem, Problem 4 _Starter.zip.
You will submit your solution as Problem 4 .zip.
CSE/ISE 337 - Scripting Languages
