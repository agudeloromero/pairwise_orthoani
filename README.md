# pairwise_orthoani
This is a python script that calculate the Average Nucleotide Identity by Orthology (OrthoANI) (Lee et al., 2016).

In case you need to download the fasta/s from the NCBI, you can can retrieve the FASTA files useing the GenBank ID reference with this (script)[https://github.com/agudeloromero/Download_fasta_NCBI/blob/main/script/download_ncbi_fasta.py], instructions on (Download_fasta_NCBI)[https://github.com/agudeloromero/Download_fasta_NCBI].

https://github.com/agudeloromero/Download_fasta_NCBI

**Reference**
Imchang Lee, Yeong Ouk Kim, Sang-Cheol Park and Jongsik Chun. OrthoANI: An improved algorithm and software for calculating average nucleotide identity (2016). International Journal of Systematic and Evolutionary Microbiology. doi:10.1099/ijsem.0.000760. PMID:26585518.

This Python script uses OrthoANI CLI. First install it in your environment. More instructions (here)[https://pypi.org/project/orthoani/].
```
pip install orthoani
```

**Setup**

Download the script from [here](https://github.com/agudeloromero/pairwise_orthoani/blob/main/script/orthoani_CLI.py) and give it execuation permissions on your machine:
```
chmod +x download_ncbi_fasta.py
```

---

**Usage Example**
```
python orthoani_CLI.py <input_path_reference> <input_path_query> <output_folder> [output_file]
```

**Run script:**
```
python orthoani_CLI.py /dir/fasta_reference/ /dir/fasta_query/ /dir/orthoani_output orthoani_results.txt
```

example: <input_path_reference>
```
ls /dir/fasta_reference
NC_029066.1.fasta
NC_002484.2.fasta
NC_030929.1.fasta
```

example: <input_path_query>
```
ls /dir/fasta_query
vContig1
```

---

**Output:**
Fasta files will be saved in the specified folder (in this case output_folder), with filenames corresponding to the reference IDs.
```
cat /dir/orthoani_output/orthoani_results.txt
NC_029066.1.fasta       vContig1.fasta     0.0
NC_002484.2.fasta       vContig1.fasta     58.955
NC_030929.1.fasta       vContig1.fasta     0.0
```
