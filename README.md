# WLabKit
**This is a toolkit to handle bio-data from WeiBin Lab.**

![WLabKit](https://cdn.jsdelivr.net/gh/BioGavin/Pic/imgWLabKit.png)

Similar data processing tasks occur frequently in my daily work though these tasks are not complicated. To avoid change the code repeatedly, I set up this project for the convenience of laboratory members and others.



# Contents

1. [Installation](#sec_install)</br>

2. [Usage](#sec_use)</br>

   2.1 [Sequence Processing](#sec_seq_proc)</br>

   2.2 [antiSMASH Results Processing](#sec_antiSMASH_proc)</br>

3. [Other Source](#sec_others)</br>
4. [Contact](#sec_contact)</br>



<a name="sec_install"></a>

## Installation

Binary installers for the latest released version are available at the Python Package Index (PyPI).

Before installing wlabkit, I recommend you to use conda to install environment dependencies.
```shell
conda create -n wlabkit python=3.8 numpy biopython pandas beautifulsoup4
```
Then, you can run:
```shell
pip install wlabkit
```



### Latest version: 0.8.0

⚠️***Attention:  Only the latest version has all the functions*** 



<a name="sec_use"></a>

## Help

Get help information, you can run:
```shell
wlabkit -h
```

If you want to get help information of subcommand, you can run:
```shell
wlabkit [subcommand] -h
```



## Subcommands

Subcommands are as follows. You can run the following command, and the relevant files are in the `test_data` folder.



<a name="sec_seq_proc"></a>

### Sequence Processing

- ***getseq***

get target sequences from a header list.

examples:
```shell
wlabkit getseq -i search.fasta -l header.txt -o target.fasta
```



- ***getseq2***

get target sequences by keyword in header.

examples:

```shell
wlabkit getseq2 -i search.fasta -l keyword.txt -o target.fasta
```



- ***getseqheader***

get seq header for each fasta file.

examples:

```bash
wlabkit getseqheader -i fasta.list -o header.tsv
```

tsv output example:

| file_name     | header                            |
| ------------- | --------------------------------- |
| bin.112.fasta | NODE_1_length_45501_cov_35.865578 |
| bin.112.fasta | NODE_2_length_30738_cov_29.303865 |



- ***gbk2fasta***

convert one or more gbk files to specified fasta files.

examples:

```shell
# convert a gbk file to a fasta file
wlabkit gbk2fasta -i region001.gbk -o region001.fasta
```

```shell
# convert multiple gbk files to a fasta file
wlabkit gbk2fasta -i gbk -o gbk.fasta -m

# convert multiple gbk files to corresponding fasta files
wlabkit gbk2fasta -i gbk -o fasta  # fasta is an existing folder path
```



- ***ex_cds***


extract CDS sequences from bgk files to specified fasta files


examples:

```shell
# extract CDS from a gbk file and save to a fasta file
wlabkit ex_cds -i region001.gbk -o region001.fasta
```

```shell
# extract CDS from multiple gbk files and save to a fasta file
wlabkit ex_cds -i gbk -o cds.fasta -m

# extract CDS multiple gbk files and save to corresponding fasta files
wlabkit ex_cds -i gbk -o cds  # cds is an existing folder path
```



- ***exsl_seq***


extract specified length sequences in fasta

examples:

```shell
# extract specified length from a fasta file
# The parameters 'l' and 'r' are the left and right values of a closed interval, respectively.
# 0 <= len(seq) <= 100
wlabkit exsl_seq -i search.fasta -l 0 -r 100 -o length0-100.fasta
```

```shell
# extract specified length from multiple fasta files and save to a fasta file
wlabkit exsl_seq -i fasta -l 0 -r 100 -o length0-100.fasta -m

# extract specified length from multiple fasta files and save to corresponding fasta files
wlabkit exsl_seq -i fasta -l 0 -r 100 -o slseq  # slseq is an existing folder path
```



<a name="sec_antiSMASH_proc"></a>

### antiSMASH Results Processing


- ***antismash_getdir***

get gbk file dir of target BGC type from an antiSMASH result folder.

examples:

```shell
# analyse only one antiSMASH result folder
wlabkit antismash_getdir -i GCF_000466165.1.zip -t 'lassopeptide'
```

```shell
# analyse multiple antiSMASH result folders
for f in `ls *.zip`; do wlabkit antismash_getdir -i $f -t target.list >> target.txt; done
```



- ***antismash_exstructure***

parse antiSMASH index.html file to extract NRPS/PKS products.

examples:

```shell
# parse a html file from one antiSMASH result folder
wlabkit antismash_exstructure -i index.html -o structures.tsv
```

```shell
# parse html files from multi mantiSMASH result folders
# index_html.list contains the paths of index.html
find antiSMASH -name 'index.html' > index_html.list
wlabkit antismash_exstructure -l index_html.list -o structures.tsv
```



<a name="sec_others"></a>

## Other Resource

- [tasks folder](/tasks) holds some code tasks that are useful but not suitable for writing to the command line.

- [plots folder](plots) holds some sample code for plotting.



<a name="sec_contact"></a>

## Contact

If you have any problems, don't hesitate to contact me. <gavinchou64@gmail.com>

