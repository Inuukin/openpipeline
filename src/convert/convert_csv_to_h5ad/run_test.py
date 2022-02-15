import subprocess
from os import path
import muon as mu

cmd_pars = [
    "./" + meta["functionality_name"],
    "--input",
    meta["resources_dir"]
    + "pbmc_1k_protein_v3/pbmc_1k_protein_v3_filtered_feature_bc_matrix.csv",
    "--output=output.h5ad",
]
out = subprocess.check_output(cmd_pars).decode("utf-8")

# check if file exists
assert path.exists("output.h5ad"), "No output was created."

# read it with scanpy
data = mu.read_h5ad("output.h5ad")

# check whether gex was found
assert data.mod["rna"].var["feature_types"].unique() == [
    "Gene Expression"
], "Output X should only contain Gene Expression vars."

# check whether ab counts were found
assert "prot" in data.mod, 'Output should contain data.mod["rna"].'

# check whether gene was found
assert (
    "CD3_TotalSeqB" in data.mod["prot"].var_names
), 'Output should contain antibody column "CD3_TotalSeqB".'
