#Written by Sowmya Andole
Inspired by Yufeng Tong 2020-01-29
and VMD scipts

# load library
from pymol import cmd

# main function
@cmd.extend
def rmsd_per_residue(refMol, tgtMol):
    """
    Calculate the RMSD for each residue between two protein structures
    and visualize it using putty representation.
    
    USAGE:
      rmsd_per_residue refMol, tgtMol
    """

    # Create temporary objects for reference and target
    cmd.delete("ref_gzt")
    cmd.create("ref_gzt", refMol + " and polymer and not alt B")
    
    cmd.delete("tgt_gzt")
    cmd.create("tgt_gzt", tgtMol + " and polymer and not alt B")

    # Get the alpha carbon atoms
    calpha_ref = cmd.get_model("ref_gzt and name CA")
    calpha_tgt = cmd.get_model("tgt_gzt and name CA")

    # Dictionary to store RMSD values
    rmsd_values = {}
    
    # Loop through residues and calculate RMSD
    for ref_atom in calpha_ref.atom:
        resi = int(ref_atom.resi)
        tgt_atom = cmd.get_model("tgt_gzt and name CA and resi %d" % resi)
        
        if tgt_atom:
            rmsd_value = cmd.rms_cur(
                "ref_gzt and resi %d and name CA" % resi,
                "tgt_gzt and resi %d and name CA" % resi
            )
            rmsd_values[resi] = rmsd_value

    # Set up for putty visualization
    max_rmsd = max(rmsd_values.values())
    min_rmsd = min(rmsd_values.values())

    # Assign B-factors based on RMSD values
    for resi, rmsd in rmsd_values.items():
        cmd.alter("tgt_gzt and resi %d" % resi, "b=%f" % rmsd)

    # Show putty representation
    cmd.show_as("cartoon", "tgt_gzt")
    cmd.cartoon("putty", "tgt_gzt")
    cmd.set("cartoon_putty_scale_min", min_rmsd, "tgt_gzt")
    cmd.set("cartoon_putty_scale_max", max_rmsd, "tgt_gzt")
    cmd.set("cartoon_putty_transform", 0, "tgt_gzt")
    cmd.spectrum("b", "rainbow", "tgt_gzt")

    # Create a ramp for visualization
    cmd.ramp_new("rmsdPuttyScale", "tgt_gzt", [min_rmsd, max_rmsd], "rainbow")
    cmd.recolor()

    # Display RMSD values in the console
    for resi, rmsd in rmsd_values.items():
        print(f"Residue {resi}: RMSD = {rmsd:.3f}")

    # Clean up
    cmd.delete("ref_gzt")
    cmd.delete("tgt_gzt")

# Example usage:
# rmsd_per_residue("mol1", "mol2")
