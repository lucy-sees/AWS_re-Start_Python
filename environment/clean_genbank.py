import re

def clean_and_split_sequence(input_file):
    """
    Cleans the GenBank-like sequence and splits it into specific parts.
    """

    # Step 1: Clean the sequence
    cleaned_sequence = []
    is_sequence = False

    with open(input_file, 'r') as file:
        for line in file:
            line = line.strip()
            if line.lower().startswith('origin'):
                is_sequence = True
                continue
            if line.startswith('//'):
                break
            if is_sequence:
                # Remove numbers and spaces
                line = re.sub(r'\d+', '', line)
                line = line.replace(' ', '')
                cleaned_sequence.append(line)

    # Combine and lowercase the sequence
    full_sequence = ''.join(cleaned_sequence).lower()

    # Step 2: Verify full sequence length
    full_length = len(full_sequence)
    print(f"✅ Full cleaned sequence length: {full_length} characters.")

    if full_length != 110:
        print("⚠️ Warning: Full sequence is NOT exactly 110 characters. Please check the source file.")
    else:
        print("🎉 Success! Full sequence is exactly 110 characters.")

    # Step 3: Save the cleaned full sequence
    with open("preproinsulin-seq-clean.txt", "w") as file:
        file.write(full_sequence)

    # Step 4: Extract and save the parts
    parts = {
        "lsinsulin-seq-clean.txt": (0, 24),
        "binsulin-seq-clean.txt": (24, 54),
        "cinsulin-seq-clean.txt": (54, 89),
        "ainsulin-seq-clean.txt": (89, 110)
    }

    for filename, (start, end) in parts.items():
        part_sequence = full_sequence[start:end]
        with open(filename, 'w') as file:
            file.write(part_sequence)

        length = len(part_sequence)
        print(f"✅ {filename} saved with {length} characters.")
        # Extra verification
        expected_lengths = {
            "lsinsulin-seq-clean.txt": 24,
            "binsulin-seq-clean.txt": 30,
            "cinsulin-seq-clean.txt": 35,
            "ainsulin-seq-clean.txt": 21
        }
        if length == expected_lengths[filename]:
            print(f"🎉 {filename} length verified!")
        else:
            print(f"⚠️ {filename} length is incorrect. Expected {expected_lengths[filename]} characters.")

if __name__ == "__main__":
    input_file = "sequence.txt"  # Replace with your raw GenBank-like file name
    clean_and_split_sequence(input_file)
