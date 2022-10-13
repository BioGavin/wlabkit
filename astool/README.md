# astool

🧰 Here are some scripts for processing BGC related files, such as JSON, gbk, etc.



# Scripts

1. Extract SMILES of NPRs/PKs products from the antiSMASH json result file and output a table in tsv format cantaining "locus, region, smiles" information.

```shell
astool ex_smiles -i <json_dir> -o smiles.tsv -t antismash
```

`<json_dir>` could be a directory of a json file, or an txt file containing one json file directory per line.



2. Extract SMILES from the MIBiG json file.

```shell
astool ex_smiles -i <json_dir> -o smiles.tsv -t mibig
```



3. Save CDS sequences in gbk files in fasta file format.

```shell
astool gbk2fasta -i gbk_file -o fasta_file
```



4. Collect target gbk files from antiSMASH result folders.

```shell
collect_gbk_file.py smiles.tsv target_folder
```

`smiles.tsv`: output from `astool ex_smiles -i <json_dir> -o smiles.tsv -t antismash`.

`target_folder`: find the target gbk files and copy to the target folder.



5. download antismash database.

```shell
download_antismash_db.py tsv_file target_path
```

`tsv_file`: downloaded form [antiSMASH database Statistic page](https://antismash-db.secondarymetabolites.org/stats.html).

`target_path`: the path where the downloaded file is saved.



## extractJson

### ex_polymer_from_json.py

Usage:

```bash
ex_polymer_from_json.py json.list polymer.tsv
```

Output TSV:

| json_file    | record_id | region_number | region_type | cc_number | cc_type    | polymer                       |
| ------------ | :-------- | ------------- | ----------- | --------- | ---------- | ----------------------------- |
| GCA0000.json | NC_0129.1 | 1             | NRPS+T1PKS  | 1         | NRPS       | (ile) + (ohmal) + (val - val) |
| GCA0000.json | NC_0129.1 | 1             | NRPS+T1PKS  | 2         | NRPS+T1PKS | (ile) + (ohmal) + (val - val) |

If the json files fail to be processed, these files are saved in a log file.



## extractGBK
