# pairwise_orthoani

This is a Python script that calculates the Average Nucleotide Identity by Orthology (OrthoANI) (Lee et al., 2016).

If you need to download FASTA files from NCBI, you can retrieve them using the GenBank ID reference with this [script](https://github.com/agudeloromero/Download_fasta_NCBI/blob/main/script/download_ncbi_fasta.py). Detailed instructions are available in the [Download_fasta_NCBI](https://github.com/agudeloromero/Download_fasta_NCBI).

https://github.com/agudeloromero/Download_fasta_NCBI

**Reference**

Imchang Lee, Yeong Ouk Kim, Sang-Cheol Park and Jongsik Chun. OrthoANI: An improved algorithm and software for calculating average nucleotide identity (2016). International Journal of Systematic and Evolutionary Microbiology. doi:10.1099/ijsem.0.000760. PMID:26585518.

---

**Requirements**

This Python script uses the OrthoANI CLI tool. To install it in your environment, run: 
```
pip install orthoani
```
For more details, refer to the [OrthoANI CLI documentation](https://pypi.org/project/orthoani/).

---

**Setup**

Download the script from [here](https://github.com/agudeloromero/pairwise_orthoani/blob/main/script/orthoani_CLI.py) and grant execuation permissions:
```
chmod +x orthoani_CLI.py
```

---

**Usage Example**

Run the script with:
```
python orthoani_CLI.py <input_path_reference> <input_path_query> <output_folder> [output_file]
```

Example Command:
```
python orthoani_CLI.py /dir/fasta_reference/ /dir/fasta_query/ /dir/orthoani_output orthoani_results.txt
```

Example Input Directories:
<input_path_reference>:
```
ls /dir/fasta_reference
NC_029066.1.fasta
NC_002484.2.fasta
NC_030929.1.fasta
```

<input_path_query>
```
ls /dir/fasta_query
vContig1
```

---

**Output:**

The results will be saved in the specified output folder (e.g., orthoani_output) as a tab-delimited text file with three columns: reference, query, and ANI percentage.

Example Output:
```
cat /dir/orthoani_output/orthoani_results.txt
NC_029066.1.fasta       vContig1.fasta     0.0
NC_002484.2.fasta       vContig1.fasta     58.955
NC_030929.1.fasta       vContig1.fasta     0.0
```
