from dfp import parse_file
import os, pytest

# pip install pytest in the terminal
# pytest -v dfp_test.py  (runs all the tests)
# pytest -v dfp_test.py::test_02_basic_operation (runs a specific test)


# Test 1: Test parsing a simple CSV file
def test_01_basic_operation():
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

# Test 2: Test if output file size is reasonable
def test_02_export_file_size():
    test_input = "./datafile_5.csv"
    test_output = "./outputfile_test.csv"
    
    # Constants determined from a correctly truncated output of datafile_5.csv
    # Min size (~200 bytes) ensures all 5 records are present.
    MIN_EXPECTED_SIZE = 200 
    # Max size (~270 bytes) ensures the description has been truncated.
    MAX_EXPECTED_SIZE = 270 

    # Ensure test file exists
    assert os.path.exists(test_input), "Test input file should exist"
    
    # Remove output file if it exists
    if os.path.exists(test_output):
        os.remove(test_output)
    
    # Run the parse_file function
    parse_file(test_input, test_output, 30)
    
    # Check if the output file size is reasonable
    export_size = os.path.getsize(test_output)
    
    # A) Check: Output should not be empty and must contain all records (lower bound).
    assert export_size >= MIN_EXPECTED_SIZE, (
        f"Output file size ({export_size} bytes) is too small. "
        f"Expected at least {MIN_EXPECTED_SIZE} bytes. Check if all records were exported."
    )
    
    # B) Check: Output size must be small enough (tighter upper bound) to enforce truncation.
    assert export_size <= MAX_EXPECTED_SIZE, (
        f"Output file size ({export_size} bytes) is too large. "
        f"Expected at most {MAX_EXPECTED_SIZE} bytes. Check for correct description truncation or if the header was included."
    )

# Test 3: Check behaviour when the source file doesn't exist 
def test_03_source_file_exists():
    test_input = "./DOESNOTEXIST.csv"
    test_output = "./outputfile_test.csv"

    # Assert that calling the function with a missing file raises a FileNotFoundError
    with pytest.raises(FileNotFoundError):
        parse_file(test_input, test_output, 30)

    # Check that output file wasn't created (important to ensure no side effects before error)
    assert not os.path.exists(test_output), "Output file should not be created if source doesn't exist"

# Test 4: Verify the correct length of descriptions
def test_04_description_length():
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

# Test 5: Check some processed records at the end of the file
def test_05_check_end_records():
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

# Test 6: Verify processing with a different delimiter (semicolon)
def test_06_different_delimiter():
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

# Test 7: Verify that whitespace is correctly removed (stripped) from datafile_UK.csv
def test_07_whitespace_removal():
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

# Test 8: Ensure truncation doesn't happen if max_description_length is larger than description length
def test_08_no_truncation():
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