# BioMod

Aim: Pymol scripts to calculate RMSD per residue from Molecular dynamics simulation data.
Software requirements: Pymol 3.0, python 3.0
Input files: 6 snapshots in pdb format from MD simulation data, at 0ns, 20ns, 40ns, 60ns, 80ns, 100ns. 
Script files: align.py, putty.py, RMSDPR.py
Method:
Md simulation for 100ns -> PDB collected at 0ns, 20ns, 40ns, 60ns, 80ns, 100 ns -> Alignment -> RMSD per residue calculation -> Visualisation.

How to run:
    1. Upload 6 pdb files of snapshots taken from MD simulation data named: mol1, mol2, mol3, mol4, mol5, mol6 in pymol. 
    2. Run align.py script to align the structures.
    3. To calculate RMSD per residue, run the script RMSDPR.
    4. To visualise RMSD per residue, run the script putty.py.
Output:
Data: Alignment scores for each molecule compared with first structure will be given in align.csv. RMSD values for each residue will be given in rmsd_results.csv
Visualization: The function will also modify the visual representation of the target molecule:
    • The target molecule will be displayed as a cartoon.
    • The putty representation will be applied, where the thickness and color of the cartoon will reflect the RMSD values.
    • A color ramp (from minimum to maximum RMSD) will be created to visually represent the variance in RMSD across residues.
Reference: 
    1. https://pymolwiki.org/index.php/RmsdByResidue
    2. https://github.com/tongalumina/rmsdca/blob/master/README.md 
    3. https://www.ks.uiuc.edu/Research/vmd/vmd-1.7.1/ug/node185.html
    4. https://mail.cgl.ucsf.edu/mailman/archives/list/chimera-users@cgl.ucsf.edu/thread/64HSGRAPHIAT4DKIPF4E6NRVWKKFCMET/
    5. https://www.ks.uiuc.edu/Research/vmd/vmd-1.8.2/tutorial/vmd-tutorial-files/rmsd-fullthrottle.tcl  
    6. https://www.ks.uiuc.edu/Training/Tutorials/namd/namd-tutorial-win-html/node15.html#SECTION00061100000000000000
