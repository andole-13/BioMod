#Written by Sowmya Andole 26-09-2024
#Inspired by Yufeng Tong 2020-01-29
#and VMD scipts


# load library
from pymol import cmd

# main function
@cmd.extend
def calculate_rmsd_multiple_pdbs(reference, *frames):
    """
    Calculate RMSD for each residue across multiple PDB files.
    
    USAGE: calculate_rmsd_multiple_pdbs reference_frame, frame1, frame2, ...
    """
    
    # Select the reference model
    cmd.delete("ref_model")
    cmd.create("ref_model", reference + " and polymer")

    outputText = ""
    csvHeadline = "frame,residue,rmsd\n"

    for frame in frames:
        cmd.delete("target_model")
        cmd.create("target_model", frame + " and polymer")

        # Calculate RMSD for Cα atoms
        rmsd_values = []
        ref_calpha = cmd.get_model("ref_model and name CA")
        target_calpha = cmd.get_model("target_model and name CA")
        
        for ref_res in ref_calpha.atom:
            res_id = ref_res.resi
            if res_id in [atom.resi for atom in target_calpha.atom]:
                # Find corresponding Cα in the target
                tgt_res = [atom for atom in target_calpha.atom if atom.resi == res_id][0]
                rmsd_value = cmd.rms_cur(
                    "ref_model and resi " + str(ref_res.resi) + " and name CA",
                    "target_model and resi " + str(tgt_res.resi) + " and name CA"
                )
                rmsd_values.append((res_id, rmsd_value))

        # Save the results
        for res_id, rmsd in rmsd_values:
            outputText += f"{frame},{res_id},{rmsd:.3f}\n"

    print(outputText)
    
    # Save to CSV
    with open("rmsd_results.csv", "w") as f:
        f.write(csvHeadline)
        f.write(outputText)
        
    print("RMSD results saved to rmsd_results.csv")

# Example of how to call the function
calculate_rmsd_multiple_pdbs("mol1", "mol2", "mol3", "mol4", "mol5", "mol6")
