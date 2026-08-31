# DNA Mutation Scanner: A tool to find corrupted or mutated genetic data
# Built using basic Python structures (Lists, Dictionaries, Loops, Functions)

def load_genetic_database():
    # Simulating a small database of healthy reference DNA sequences
    return {
        "Patient_01": "ATCGATCGATCG",
        "Patient_02": "GCTAGCTAGCTA",
        "Patient_03": "TTTGGGCCCAAA"
    }

def scan_for_mutations(sample_dna, reference_dna):
    # If lengths don't match, the data stream might be intercepted or corrupted
    if len(sample_dna) != len(reference_dna):
        return "CRITICAL ERROR: Data length mismatch. Possible tampering."
    
    mutations_detected = 0
    mutation_positions = []
    
    # Using a single loop to compare characters at each position
    for i in range(len(sample_dna)):
        if sample_dna[i] != reference_dna[i]:
            mutations_detected += 1
            mutation_positions.append(i)
            
    # Simple risk threshold logic
    if mutations_detected > 3:
        return f"ALERT: High mutation rate detected ({mutations_detected} flaws at positions {mutation_positions})."
    elif mutations_detected > 0:
        return f"WARNING: Minor variation detected at positions {mutation_positions}."
    
    return "SUCCESS: Data integrity verified. DNA sequence is clean."

# --- Simulating the Execution ---
if __name__ == "__main__":
    db = load_genetic_database()
    
    # Scenario A: Testing a healthy sample
    print("Scanning Patient_01 Sample A...")
    test_sample_A = "ATCGATCGATCG"
    result_A = scan_for_mutations(test_sample_A, db["Patient_01"])
    print(result_A)  
    # Output: Success
    
    print("\n-------------------------\n")
    
    # Scenario B: Testing a mutated/corrupted sample
    print("Scanning Patient_01 Sample B...")
    test_sample_B = "ATTTATTTATCG"  
    # Changed characters at index 1, 2, 5, 6
    result_B = scan_for_mutations(test_sample_B, db["Patient_01"])
    print(result_B)  
    # Output: Alert with positions
