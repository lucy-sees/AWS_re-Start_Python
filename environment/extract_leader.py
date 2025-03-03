def extract_binsulin_sequence(input_file, output_file):
    """
    Extracts the first 24 amino acids from the cleaned preproinsulin sequence
    and saves them to a new file as binsulin-seq-clean.txt.
    Verifies that the saved sequence has exactly 24 characters.
    """
    # Read the cleaned sequence from the input file
    with open(input_file, 'r') as file:
        sequence = file.read().strip()

    # Extract the first 24 amino acids (positions 0–23)
    binsulin_sequence = sequence[:24]

    # Save the extracted sequence to the output file
    with open(output_file, 'w') as file:
        file.write(binsulin_sequence)

    # Verification
    sequence_length = len(binsulin_sequence)
    print(f"✅ Binsulin sequence saved to '{output_file}'.")
    print(f"✅ Extracted sequence: {binsulin_sequence}")
    print(f"✅ Sequence length: {sequence_length} characters.")

    if sequence_length == 24:
        print("🎉 Success! The sequence has exactly 24 amino acid letters.")
    else:
        print("⚠️ Warning: The extracted sequence length is NOT 24. Please check your source data.")

if __name__ == "__main__":
    input_file = "lsinsulin-seq-clean.txt"      # Your cleaned sequence file
    output_file = "binsulin-seq-clean.txt"          # Output file for the first 24 amino acids
    extract_binsulin_sequence(input_file, output_file)
