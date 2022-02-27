# WLabKit
**This is a toolkit to handle bio-data from WeiBin Lab.**

![WLabKit](https://cdn.jsdelivr.net/gh/BioGavin/Pic/imgWLabKit.png)

Similar data processing tasks occur frequently in my daily work though these tasks are not complicated. To avoid change the code repeatedly, I set up this project for the convenience of laboratory members and others.



## Installation

Binary installers for the latest released version are available at the Python Package Index (PyPI) and on Conda.

Before installing wlabkit, make sure the dependency packages are installed.
```shell
pip install numpy biopython pandas
```
Then, you can run (At present, only pip installing is allowed):
```shell
conda install wlabkit
```
```shell
pip install wlabkit
```



### Latest version: 0.0.24

⚠️***Attention:  Only the latest version has all the functions*** 



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



- ***getseq***

get target sequences from a header list.

examples:
```shell
wlabkit getseq -i search.fasta -l header.txt -o target.fasta
```




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
wlabkit exsl_seq -i search.fasta -l 0 -r 100 -o length0-100.fasta
```

```shell
# extract specified length from multiple fasta files and save to a fasta file
wlabkit exsl_seq -i fasta -l 0 -r 100 -o length0-100.fasta -m

# extract specified length from multiple fasta files and save to corresponding fasta files
wlabkit exsl_seq -i fasta -l 0 -r 100 -o slseq  # slseq is an existing folder path
```





## Tasks

`tasks` folder holds some code tasks that are useful but not suitable for writing to the command line.

* [parse_xml](tasks/parse_xml): parsing an XML file to extract target information

- [Excel2fasta](tasks/excel2fasta): extracting sequences and information from Excel file to Fasta file



## Contact

If you have any problems, don't hesitate to contact me. <gavinchou64@gmail.com>

