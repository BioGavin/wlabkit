# astool

🧰 Here are some scripts for processing BGC related files, such as JSON, GBK, etc.



# Scripts

## astool

### ex_smiles

- Extract SMILES of NPRs/PKs products from the antiSMASH json result file and output a table in tsv format cantaining "locus, region, smiles" information.

```shell
astool ex_smiles -i <json_dir> -o smiles.tsv -t antismash
```

`<json_dir>` could be a directory of a json file, or an txt file containing one json file directory per line.

smiles.tsv:

| file_path                                     | record_id       | region_id | smiles                                                       |
| --------------------------------------------- | --------------- | --------- | ------------------------------------------------------------ |
| antiSMASH/GCF_002968995.1_ASM296899v1_genomic | NZ_PUWT01000126 | 1         | NC([*])C(=O)O                                                |
| antiSMASH/GCF_002968995.1_ASM296899v1_genomic | NZ_PUWT01000020 | 1         | CC(O)CC(=O)NC(CC(=O)N)C(=O)CC(O)NC(CC(=O)N)C(=O)NC(CCC(=O)O)C(=O)CC(O)C(=O)O |
| antiSMASH/GCF_002968995.1_ASM296899v1_genomic | NZ_PUWT01000021 | 1         | NC([*])C(=O)NC([*])C(=O)NC([*])C(=O)O                        |
| antiSMASH/GCF_002968995.1_ASM296899v1_genomic | NZ_PUWT01000023 | 2         | NC(CS)C(=O)CC(O)NC(CS)C(=O)O                                 |

- Extract SMILES from the MIBiG json file.

```shell
astool ex_smiles -i <json_dir> -o smiles.tsv -t mibig
```



### cds_len

- Count the length of cds sequences in gbk files

```bash
astool cds_len -i gbk.list -o output.tsv
```

output.tsv:

| record_id     | locus_tag     | length |
| ------------- | ------------- | ------ |
| NZ_CP030840.1 | ACPOL_RS15070 | 147    |
| NZ_CP030840.1 | ACPOL_RS15075 | 329    |
| NZ_CP030840.1 | ACPOL_RS15080 | 80     |



### cdsfromgbk2fasta

- Save CDS sequences in gbk files in fasta format.

```shell
astool cdsfromgbk2fasta -i gbk_file -o fasta_file
```





## extractJson

### ex_polymer_from_json.py

Applicable: `antiSMASH` `?MIBiG`

Usage:

```bash
ex_polymer_from_json.py json.list output.tsv
```

Output TSV:

| json_file    | record_id | region_number | region_type | cc_number | cc_type    | polymer                       |
| ------------ | :-------- | ------------- | ----------- | --------- | ---------- | ----------------------------- |
| GCA0000.json | NC_0129.1 | 1             | NRPS+T1PKS  | 1         | NRPS       | (ile) + (ohmal) + (val - val) |
| GCA0000.json | NC_0129.1 | 1             | NRPS+T1PKS  | 2         | NRPS+T1PKS | (ile) + (ohmal) + (val - val) |

If the json files fail to be processed, these files are saved in a log file.



### ex_knownclusterblast_from_json.py

Applicable: `antiSMASH` `MIBiG`

Usage:

```bash
ex_knownclusterblast_from_json.py json_dir_list.txt knownclusterblast_hits_number_output.tsv knownclusterblast_hits_detail_output.tsv
```

knownclusterblast_hits_number_output.tsv:

| file_name                               | record_id   | region_number | total_hits |
| --------------------------------------- | ----------- | ------------- | ---------- |
| GCF_000196475.1_ASM19647v1_genomic.json | NC_012962.1 | 1             | 0          |
| GCF_000196475.1_ASM19647v1_genomic.json | NC_012962.1 | 2             | 0          |
| GCF_000196475.1_ASM19647v1_genomic.json | NC_012962.1 | 3             | 0          |
| GCF_000196475.1_ASM19647v1_genomic.json | NC_012962.1 | 4             | 15         |
| GCF_000196475.1_ASM19647v1_genomic.json | NC_012962.1 | 5             | 3          |

knownclusterblast_hits_detail_output.tsv:

| file_name                               | record_id   | region_number | MIBiG_accession | MIBiG_description | MIBiG_cluster_type | blast_score | MIBiG_similarity_precise_proportion | MIBiG_similarity_rough_proportion |
| --------------------------------------- | ----------- | ------------- | --------------- | ----------------- | ------------------ | ----------- | ----------------------------------- | --------------------------------- |
| GCF_000196475.1_ASM19647v1_genomic.json | NC_012962.1 | 4             | BGC0000460      | vulnibactin       | NRP                | 1854        | 12.5                                | 12                                |
| GCF_000196475.1_ASM19647v1_genomic.json | NC_012962.1 | 4             | BGC0000451      | turnerbactin      | NRP                | 1199        | 23.0769231                          | 23                                |
| GCF_000196475.1_ASM19647v1_genomic.json | NC_012962.1 | 4             | BGC0000294      | acinetobactin     | NRP                | 1261        | 13.0434783                          | 13                                |
| GCF_000196475.1_ASM19647v1_genomic.json | NC_012962.1 | 4             | BGC0001502      | amonabactin P 750 | NRP                | 1245        | 42.8571429                          | 42                                |
| GCF_000196475.1_ASM19647v1_genomic.json | NC_012962.1 | 4             | BGC0000368      | streptobactin     | NRP                | 942         | 17.6470588                          | 17                                |



## extractGBK

### ex_ripp_from_gbk.py

Applicable: `antiSMASH` `?MIBiG`

Usage:

```bash
ex_ripp_from_gbk.py gbk.list output.tsv
```

output.tsv:

| gbk_file                                                     | gbk_name                 | leader_seq                     | core_seq                            |
| ------------------------------------------------------------ | ------------------------ | ------------------------------ | ----------------------------------- |
| antiSMASH/GCA_000147815.3_ASM14781v3_genomic/CP002994.1.region002.gbk | CP002994.1.region002.gbk | MSMNPEAATTQVDVDFTLDVRVIEAGLPVR | DLLRDTSDNCGSSCSGTACTSFVGDPA         |
| antiSMASH/GCA_000147815.3_ASM14781v3_genomic/CP002994.1.region037.gbk | CP002994.1.region037.gbk | MSTEAKNWKEAESTTSPAG            | AGFGELSLAELREDQSAHAPLSSGWVCTLTTECGC |
| antiSMASH/GCA_000147815.3_ASM14781v3_genomic/CP002994.1.region037.gbk | CP002994.1.region037.gbk | VRELPRGCRADCGHVLQPTVRGG        | DQGCYRAATC                          |

### ex_completeness_from_gbk.py

Applicable: `antiSMASH` `MIBiG`

Usage:

```bash
ex_completeness_from_gbk.py gbk.list output.tsv
```

output.tsv:

| gbk_name                  | region_completeness |
| ------------------------- | ------------------- |
| NC_012962.1.region004.gbk | FALSE               |
| NC_012962.1.region008.gbk | FALSE               |



### stats_domain_in_nrps_pks.py

Applicable: `antiSMASH` `MIBiG`

Usage:

```bash
stats_domain_in_nrps_pks.py gbk.list output.tsv
```

output.tsv:

| gbk_name                 | ACP  | ACPS | AMP-binding | Aminotran_1_2 | Aminotran_3 | Aminotran_4 | Aminotran_5 |
| ------------------------ | ---- | ---- | ----------- | ------------- | ----------- | ----------- | ----------- |
| AE009951.2.region001.gbk | 1    | 1    |             |               |             |             |             |
| CP002994.1.region001.gbk |      |      |             |               | 1           |             |             |
| CP002994.1.region003.gbk | 1    |      |             |               |             |             |             |
| CP002994.1.region004.gbk |      |      | 1           |               |             |             |             |

The number of columns in the TSV file depends on the number of Domain types.



### ex_a_domain_from_gbk.py

Applicable: `antiSMASH`

Usage:

```bash
ex_a_domain_from_gbk.py gbk.list output.faa
```

output.faa:

```
>nrpspksdomains_ctg1_871_AMP-binding.1 consensus: thrfromfile: NC_012962.1.region004
KSAIICGERQIAYSELGEYVQKIVNNLHRCGMHKGSVVAICLPRSPEHVMVTIACALLGI
IWVPIDVNSPSERLEYLLTNCHPDLIVNTGELNSDKAITLETLLTSVSENALFSLETLSS
LSHSIDPAYYLYTSGTTGKPKCVVLNNKATSNVIEQTMNKWEVKQDDVFISVTPLHHDMS
VFDLFASLTIGATLVIPEPHEEKDAIHWNRLVSKHKVSIWCSVPAILEMLIACQKGSSLS
SLRLIAQGGDYIKPMVIKEIRTTYPDIRLFSLGGPTETTIWSIWHEITSEDVSLIPYGKP
LPATQYFICNDSHEHCPAFVTGRIYTTGVNLALGYLEGGIVVQKDFVTITTPKGEQLRAF
RTGDQGYYRKDGTIIFASRVNGYVKIR
>nrpspksdomains_ctg1_881_AMP-binding.1 consensus: dhbfromfile: NC_012962.1.region004
DNGKIALICGERQFSYAELNLLVDSLAAALQQRGVKRGQTALVQLGNEAEFYIVFFALLR
LGVVPINAVFSHQRSELCAYADQINPALLIADRNHSLFSDDDFIDELRIRIPSLCHVVLR
GDNDSILDVETLLAQGAGDFVANPTPADEVAFFQLSGGSTGTPKLIPRTHNDYYYSIRAS
AEICQFNAETRYLCALPAAHNFPMSSPGALGAFYCGGQVILAHNPGADCCFPLIQQHRVN
AVALVPPAVSVWLEAIALGGNCDALKSLRLLQVGGARLSESLARRIPKEMGCQLQQVFGM
AEGLVNYTRLDDDEQHIFMTQGRPISPDDEVWVADNDGNPVPHGIAGRLMTQGPYTFRGY
YRSPQHNQQCFDSNGFYCSGDLVIMTPDGYLQVVGREKDQINR
```



### ex_asdomain_number_from_gbk.py

Applicable: `antiSMASH` `MIBiG`

Usage:

```bash
ex_asdomain_number_from_gbk.py gbk.list output.tsv
```

output.tsv:

| filename                 | bgc_type    | bgc_length | number_domain | smiles        |
| ------------------------ | ----------- | ---------- | ------------- | ------------- |
| CP029716.1.region002.gbk | bacteriocin | 11139      | 0             |               |
| CP029716.1.region003.gbk | thiopeptide | 26303      | 1             |               |
| CP029716.1.region001.gbk | siderophore | 14429      | 0             |               |
| CP029716.1.region004.gbk | NRPS        | 52094      | 9             | NC(CO)C(=O)O  |
| CP029716.1.region005.gbk | bacteriocin | 10624      | 0             |               |
| CP029716.1.region006.gbk | arylpolyene | 43591      | 8             |               |
| AE009951.2.region001.gbk | NRPS-like   | 42499      | 3             | NC([*])C(=O)O |



### ex_nrps_monomers_from_gbk.py

Applicable: `antiSMASH` `?MIBiG`

Usage:

```bash
ex_nrps_monomers_from_gbk.py gbk.list output.tsv
```

output.tsv:

| file_name               | locus_tag     | monomers | count |
| ----------------------- | ------------- | -------- | ----- |
| NZ_CP030840.1.region004 | ACPOL_RS11395 | X        | 1     |
| CP002994.1.region032    | ctg1_5994     | pk       | 1     |
| CP002994.1.region032    | ctg1_5995     | mal      | 1     |
| CP002994.1.region032    | ctg1_6003     | X        | 1     |







## Others

### collect_gbk_file.py

Collect target gbk files from antiSMASH result folders.

```shell
collect_gbk_file.py smiles.tsv target_folder
```

`smiles.tsv`: output from `astool ex_smiles -i <json_dir> -o smiles.tsv -t antismash`.

`target_folder`: find the target gbk files and copy to the target folder.



### download_antismash_db.py

download antiSMASH database

```shell
download_antismash_db.py tsv_file target_path
```

`tsv_file`: downloaded form [antiSMASH database Statistic page](https://antismash-db.secondarymetabolites.org/stats.html).

`target_path`: the path where the downloaded file is saved.



### table2fasta.py

Convert sequences stored in tsv or excel files to fasta format.

```bash
# help
table2fasta.py -h

# tsv2fasta
table2fasta.py -i input.tsv -n seq_id -s seq -t tsv -o output.fasta

# excel2fasta
table2fasta.py -i input.xlsx -n seq_id -s seq -t excel -o output.fasta
```



### concat_tsv.py

Combine all tsv files in a folder into one file.

```bash
concat_tsv.py tsv tsv/antismash.cds.len.tsv
```



## shell

### hoge

Copy and rename files based on map.

Usage:

```bash
# help
hoge -h

# usage
hoge map.tsv
```

map.tsv:

| wlabkit/astool/test_data/antiSMASH/GCA_003204095.1_ASM320409v1_genomic/CP029716.1.region002.gbk | seq1.gbk |
| ------------------------------------------------------------ | -------- |
| wlabkit/astool/test_data/antiSMASH/GCA_003204095.1_ASM320409v1_genomic/CP029716.1.region003.gbk | seq2.gbk |
| wlabkit/astool/test_data/antiSMASH/GCA_003204095.1_ASM320409v1_genomic/CP029716.1.region001.gbk | seq3.gbk |