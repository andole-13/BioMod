#To align pdb structures
#Written by Sowmya Andole 26-09-2024

# Load the necessary library
from pymol import cmd
import csv

# Define a function to align multiple proteins and write results to a CSV file
def align_multiple_proteins():
    # List of protein names
    protein_names = ["mol1", "mol2", "mol3", "mol4", "mol5", "mol6"]
    
    # Set the reference protein
    reference = protein_names[0]

    # Create a list to hold the results
    results = []

    # Align each protein to the first one (mol1)
    for protein in protein_names[1:]:
        print("Aligning {} to {}...".format(protein, reference))
        
        # Perform the alignment and capture the score
        alignment_results = cmd.align(protein, reference)
        
        # The first element is the alignment score (the RMSD)
        alignment_score = alignment_results[0]  # This should be a float
        
        # Print the alignment score
        print("Alignment score for {} to {}: {:.2f}".format(protein, reference, alignment_score))

        # Append the results to the list
        results.append([protein, alignment_score])

    # Write results to a CSV file
    with open('alignment_scores.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Molecule', 'Alignment Score'])  # Write header
        csv_writer.writerows(results)  # Write data

    print("Alignment complete. Results saved to 'alignment_scores.csv'.")

# Run the function
align_multiple_proteins()
