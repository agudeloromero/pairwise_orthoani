#!/usr/bin/env python3

import os
import sys
import subprocess
import re  # For more robust numeric parsing


def run_orthoani(input_path_q, input_path_r, output_path="output_folder", output_file="orthoani_results.txt"):
    """
    Run OrthoANI for pairwise comparisons of FASTA files and save results in a tab-delimited file.
    Patricia Agudelo-Romero, PhD.

    Args:
        input_path_q (str): Path to a folder or single file for the `-q` parameter.
        input_path_r (str): Path to a folder or single file for the `-r` parameter.
        output_path (str): Folder to save the output file.
        output_file (str): Name of the output file for results.
    """
    # Valid extensions for FASTA files
    valid_extensions = (".fa", ".fasta", ".fna")

    # Ensure output folder exists
    os.makedirs(output_path, exist_ok=True)
    output_file_path = os.path.join(output_path, output_file)

    # Get all FASTA files for -q
    if os.path.isdir(input_path_q):
        fasta_files_q = [os.path.join(input_path_q, f) for f in os.listdir(input_path_q) if f.endswith(valid_extensions)]
    elif os.path.isfile(input_path_q) and input_path_q.endswith(valid_extensions):
        fasta_files_q = [input_path_q]
    else:
        print("Error: Input for -q must be a folder with FASTA files or a single FASTA file.")
        sys.exit(1)

    # Get all FASTA files for -r
    if os.path.isdir(input_path_r):
        fasta_files_r = [os.path.join(input_path_r, f) for f in os.listdir(input_path_r) if f.endswith(valid_extensions)]
    elif os.path.isfile(input_path_r) and input_path_r.endswith(valid_extensions):
        fasta_files_r = [input_path_r]
    else:
        print("Error: Input for -r must be a folder with FASTA files or a single FASTA file.")
        sys.exit(1)

    # Ensure there are files to compare
    if not fasta_files_q or not fasta_files_r:
        print("Error: No valid FASTA files found for comparison.")
        sys.exit(1)

    # Open the output file for writing results
    with open(output_file_path, "w") as out_file:
        # Generate all pairwise comparisons
        for seq1 in fasta_files_q:
            for seq2 in fasta_files_r:
                cmd = ["orthoani", "-q", seq1, "-r", seq2]
                print(f"Running: {' '.join(cmd)}")
                try:
                    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, text=True)
                    raw_output = result.stdout
                    ani_percentage = None

                    # Use regex to extract numeric percentage from output
                    match = re.search(r"(\d+\.\d+)", raw_output)  # Matches floats like 0.0, 58.955
                    if match:
                        ani_percentage = match.group(1)

                    if ani_percentage is not None:
                        # Write result to file
                        out_file.write(f"{os.path.basename(seq1)}\t{os.path.basename(seq2)}\t{ani_percentage}\n")
                        print(f"Result: {os.path.basename(seq1)} vs {os.path.basename(seq2)} -> {ani_percentage}")
                    else:
                        print(f"Warning: No ANI percentage found for {seq1} and {seq2}. Raw output:\n{raw_output}")
                except subprocess.CalledProcessError as e:
                    print(f"Error running OrthoANI for {seq1} and {seq2}: {e.stderr}")


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python script.py <input_path_q> <input_path_r> <output_folder> [output_file]")
        sys.exit(1)

    input_path_q = sys.argv[1]
    input_path_r = sys.argv[2]
    output_path = sys.argv[3]
    output_file = sys.argv[4] if len(sys.argv) > 4 else "orthoani_results.txt"

    run_orthoani(input_path_q, input_path_r, output_path, output_file)
