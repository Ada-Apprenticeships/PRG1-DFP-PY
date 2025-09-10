from dfp import parse_file
import os
import pytest

# pip install pytest in the terminal
# pytest -v dfp_test.py  (runs all the tests)
# pytest -v dfp_test.py::test_02_basic_operation (runs a specific test)




# Test 1: Verify the parse_file function is defined
def test_01_parse_function_declared():
    assert callable(parse_file), "The parse_file function should be callable"

# Test 2: Test parsing a simple CSV file
def test_02_basic_operation():
    test_input = "./datafile_5.csv"
    test_output = "./outputfile_test.csv"
    expected_records = 5

    # Ensure test file exists
    assert os.path.exists(test_input), "Test input file should exist"
    
    # Remove output file if it exists
    if os.path.exists(test_output):
        os.remove(test_output)
    
    # Run the parse_file function
    result = parse_file(test_input, test_output, 30)
    assert result == expected_records, f"Expected {expected_records} records to be processed"

    # Check if the output file is created
    assert os.path.exists(test_output), "Output file should be created"

# Test 3: Test if output file size is reasonable
def test_03_export_file_size():
    test_input = "./datafile_5.csv"
    test_output = "./outputfile_test.csv"

    # Ensure test file exists
    assert os.path.exists(test_input), "Test input file should exist"
    
    # Remove output file if it exists
    if os.path.exists(test_output):
        os.remove(test_output)
    
    # Run the parse_file function
    parse_file(test_input, test_output, 30)
    
    # Check if the output file size is reasonable
    original_size = os.path.getsize(test_input)
    export_size = os.path.getsize(test_output)
    
    assert export_size > 0, "Output file should not be empty"
    assert export_size < original_size, "Output file should be smaller than the original file"

# Test 4: Check behaviour when the source file doesn't exist
def test_04_source_file_exists():
    test_input = "./DOESNOTEXIST.csv"
    test_output = "./outputfile_test.csv"
    expected_result = -1

    result = parse_file(test_input, test_output, 30)
    assert result == expected_result, "Function should return -1 when source file doesn't exist"

    # Check that output file wasn't created
    assert not os.path.exists(test_output), "Output file should not be created if source doesn't exist"

# Test 5: Verify the correct length of descriptions
def test_05_description_length():
    test_input = "./datafile_5.csv"
    test_output = "./outputfile_test.csv"
    max_description_length = 30

    # Ensure test file exists
    assert os.path.exists(test_input), "Test input file should exist"
    
    # Remove output file if it exists
    if os.path.exists(test_output):
        os.remove(test_output)
    
    # Run the parse_file function
    parse_file(test_input, test_output, max_description_length)
    
    # Check the description lengths in the output file
    with open(test_output, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    for line in lines:
        description = line.strip().split(",")[3]
        assert len(description) <= max_description_length + 3, "Description should be truncated to the correct length"

# Test 6: Check some processed records at the end of the file
def test_06_check_end_records():
    test_input = "./datafile_EU.csv"
    test_output = "./outputfile_test.csv"
    max_description_length = 30

    # Ensure test file exists
    assert os.path.exists(test_input), "Test input file should exist"
    
    # Remove output file if it exists
    if os.path.exists(test_output):
        os.remove(test_output)
    
    # Run the parse_file function
    parse_file(test_input, test_output, max_description_length)
    
    # Check some records at the end of the output file
    with open(test_output, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    # Check the last 3 records
    for line in lines[-3:]:
        columns = line.strip().split(",")
        assert len(columns) == 4, "Each line should have 4 columns"
        description = columns[3]
        assert len(description) <= max_description_length + 3, "Description should be truncated to the correct length"

# Test 7: Verify processing with a different delimiter (semicolon)
def test_07_different_delimiter():
    test_input = "./datafile_UK.csv"
    test_output = "./outputfile_test.csv"
    max_description_length = 30
    delimiter = ";"

    # Ensure test file exists
    assert os.path.exists(test_input), "Test input file should exist"
    
    # Remove output file if it exists
    if os.path.exists(test_output):
        os.remove(test_output)
    
    # Run the parse_file function with a semicolon delimiter
    parse_file(test_input, test_output, max_description_length, delimiter)
    
    # Check the description lengths in the output file
    with open(test_output, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    for line in lines:
        description = line.strip().split(delimiter)[3]
        assert len(description) <= max_description_length + 3, "Description should be truncated to the correct length"

# Test 8: Verify that whitespace is correctly removed (stripped) from datafile_UK.csv
def test_08_whitespace_removal():
    test_input = "./datafile_UK.csv"
    test_output = "./outputfile_test.csv"
    max_description_length = 30
    delimiter = ";"

    # Ensure test file exists
    assert os.path.exists(test_input), "Test input file should exist"
    
    # Remove output file if it exists
    if os.path.exists(test_output):
        os.remove(test_output)
    
    # Run the parse_file function with a semicolon delimiter
    parse_file(test_input, test_output, max_description_length, delimiter)
    
    # Check that whitespace is removed in the output file
    with open(test_output, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    for line in lines:
        columns = line.strip().split(",")
        for column in columns:
            assert column == column.strip(), "Whitespace should be removed from each column"

# Test 9: Ensure truncation doesn't happen if max_description_length is larger than description length
def test_09_no_truncation():
    test_input = "./datafile_EU.csv"
    test_output = "./outputfile_test.csv"
    max_description_length = 100  # Larger than any description in the file

    # Ensure test file exists
    assert os.path.exists(test_input), "Test input file should exist"
    
    # Remove output file if it exists
    if os.path.exists(test_output):
        os.remove(test_output)
    
    # Run the parse_file function with a large max_description_length
    parse_file(test_input, test_output, max_description_length)
    
    # Check that no descriptions are truncated in the output file
    with open(test_output, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    for line in lines:
        columns = line.strip().split(",")
        description = columns[3]
        original_description = next(row.split(",")[2] for row in open(test_input, "r", encoding="utf-8").readlines() if row.startswith(columns[0]))
        assert description == original_description, "Description should not be truncated if max_description_length is larger than description length"

@pytest.fixture(autouse=True)
def cleanup_files():
    """Cleanup files after each test."""
    yield
    for file in ["./outputfile_test.csv"]:
        if os.path.exists(file):
            os.remove(file)