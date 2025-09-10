# Task 2 - Data File Parser

**Scenario:**
You are developing an application for a travel agency that wants to display a concise list of package holidays on its mobile app. To achieve this, you need to process a CSV file containing detailed holiday information and generate a new CSV file with trimmed descriptions and re-ordered columns.

**Task:**
1. Create a function named `parse_file` that accepts the following parameters:
   * `input_file_path`: The path to the UTF-8 encoded input CSV file (e.g. `datafile_5.csv`).
   * `output_file_path`: The path to the output CSV file where the processed data should be written (UTF-8 encoding).
   * `max_description_length`: The maximum length of a description in the output file.
   * `delimiter`: The delimiter used in the CSV file (default: ",").

2. The function should perform the following actions:
   * Check if the input file exists. If not, return -1.
   * Check if an output file already exists. If it does, delete it.
   * Read the CSV file at `input_file_path` using the specified `delimiter`.
   * For each holiday package, extract the `holiday_id`, `destination`, `description` and `price`.
   * Trim whitespace from the `destination` and `description` 
   * Truncate the `description` to `max_description_length` characters, adding an ellipsis (...) to the end if it was truncated.
   * Re-order the columns to be: `holiday_id`, `price`, `destination`, and truncated `description`.
   * Write the processed data to a new CSV file at `output_file_path` using the specified `delimiter`.

3. The function should return the total number of holidays processed.

**Example Function Calls:**
```python
parse_file('./datafile_5.csv', './simplified_5.csv', 30)  # Returns 5
parse_file('./datafile_EU.csv', './simplified_EU.csv', 30)  # Returns 100
parse_file('./datafile_UK.csv', './simplified_UK.csv', 25, ';')  # Returns 50
parse_file('./missing_file.csv', './simplified_catalogue.csv', 30)  # Returns -1
```

**Exemplar Output File format for datafile_5.csv**

```
576,600,Paris,Explore the Eiffel Tower and t...
187,500,Rome,Wander through the Colosseum a...
895,400,Barcelona,Discover the Sagrada Familia a...
739,450,Amsterdam,Cruise the canals and visit th...
942,350,Lisbon,Ride the iconic Tram 28 and sa...
```

## Additional Considerations:

* Use no additional libraries or modules other than Python's standard library.
* Your function should ignore (do not export) any header information (the first row).
* The problem can be decomposed into smaller single-responsibility functions if you wish.
* Your final version should demonstrate evidence of being refactored; please note, refactoring is not bug-fixing - essentially it is reducing complexity and simplifying your codebase such that it is as efficient, readable, structured and as manageable as possible.