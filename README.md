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
   * Check if the input file exists. If not, raise a `FileNotFoundError`.
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
parse_file('./missing_file.csv', './simplified_catalogue.csv', 30) # Raises FileNotFoundError
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

* Use no additional libraries other than what has been provided.
* Your function should ignore (do not export) any header information (the first row).
* The problem can be decomposed into smaller single-responsibility functions if you wish.


## Submission Checklist

Prior to actually submitting your final attempt you should ensure you have reviewed and considered the following checklist.


1. Refactored solution.
2. Appropriate Docstring(s).
3. Does your solution follow accepted coding conventions?




## Tasks 1-4 Coding Standards rubric

| Marks | Programming Conventions and Code Quality |
| :---- | :---- |
| **Outstanding (80%+)** | The submitted code represents an **exceptional, highly optimised, and genuinely elegant solution** that demonstrates the student has **gone the extra mile** and exceeded the brief. The implementation utilises **advanced or creative methods** (e.g., highly efficient data structures or advanced Pythonic idioms) which may not have been explicitly taught, showcasing near-professional **software engineering principles**. The solution is perfectly clean, robust, and is structured with **pure functions** and **minimal nesting (ideally max 1 level)**. The response is sophisticated, achieving **conciseness and clarity without sacrificing readability**. |
| **Distinction (70-79%)** | The submitted code is an **outstanding, elegant, and efficient solution**, fully reflecting **industry-standard practice (e.g., PEP 8\)**. The design demonstrates a strong command of software design principles, adhering to **DRY** (Don't Repeat Yourself) and **KISS** (Keep It Small and Simple) while prioritising **readability**. The function structure is highly discrete, following a **'pure functions' paradigm** where appropriate, and **deep nesting is entirely avoided**. A **comprehensive, correctly formatted Docstring** is provided. **Comments are judiciously rare** and strictly informational. |
| **Merit (60-69%)** | Code is **highly competent**, well-structured, and aligns closely with industry best practices. There is **considerable evidence** of applying **DRY and KISS principles**, with functions being discrete and manageable. **Deep nesting is generally avoided**. The primary function includes a **clear and appropriate Docstring**. The solution uses clear naming and consistent formatting. **Comments are used sparingly** to clarify non-obvious logic. |
| **Pass (40-59%)** | Code is **functional and competently organised**, showing a developing understanding of professional conventions. There are areas for **further refinement** in adherence to style guides (e.g., minor inconsistencies in naming or formatting). Logic may be **somewhat repetitive (DRY issues)**, and structural complexity is occasionally present due to **moderate nesting (3+ levels)**. A **Docstring may be incomplete, poorly formatted, or missing**. **Comments may be redundant** or inconsistent. |
| **Fail (\<40%)** | Code requires **substantial work** to improve clarity, maintainability, and structural design. There are **repeated violations of core principles (DRY, KISS)**, and structural complexity is high. This suggests a **need for further development** in professional coding standards. Key elements like a **Docstring are missing**, and the use of comments is unhelpful. |
| **0%** | No attempt |


