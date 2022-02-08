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
Subcommands are as follows. You can run the following command, and the relevant files are in the test folder.

- ***getseq***

get target sequences from a header list.

examples:
```shell
wlabkit getseq -i search.fasta -l header.txt -o target.fasta
```

- ***antismash_getdir***

get gbk file dir of target BGC type from an antiSMASH result folder

examples:

```shell
# analyse only one antiSMASH result folder
wlabkit antismash_getdir -i GCF_000466165.1.zip -t 'lassopeptide'
```

```shell
# analyse multiple antiSMASH result folders
for f in `ls *.zip`; do wlabkit antismash_getdir -i $f -t target.list >> target.txt; done
```


## Contact
If you have any problems, don't hesitate to contact me. <gavinchou64@gmail.com>


