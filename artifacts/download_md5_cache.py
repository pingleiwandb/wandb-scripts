# Test scripts for https://github.com/wandb/wandb/pull/10157 where we are keep checksum file
# git checkout fix/artifact-download-performance
# source .venv/bin/activate
# pip install ux nox
# uv pip install -e ~/go/src/github.com/wandb/wandb
import wandb

def download_file():
    api = wandb.Api()
    artifact = api.artifact("reg-team-2/pinglei-wbench-gcs-upload-v20250721-v1/1gb:v0")
    artifact.download()

# python3 download_md5_cache.py
if __name__ == "__main__":
    download_file()

"""
(.venv) $ src/github.com/pingleiwandb/wandb-scripts/artifacts python3 download_md5_cache.py
wandb: Currently logged in as: pinglei (reg-team-2) to https://api.wandb.ai. Use `wandb login --relogin` to force relogin
wandb: Downloading large artifact 1gb:v0, 968.00MB. 1 files...
wandb:   1 of 1 files downloaded.
Done. 0:0:16.4 (59.0MB/s)
(.venv) $ src/github.com/pingleiwandb/wandb-scripts/artifacts python3 download_md5_cache.py
wandb: Currently logged in as: pinglei (reg-team-2) to https://api.wandb.ai. Use `wandb login --relogin` to force relogin
wandb: WARNING A graphql request initiated by the public wandb API timed out (timeout=19 sec). Create a new API with an integer timeout larger than 19, e.g., `api = wandb.Api(timeout=29)` to increase the graphql timeout.
wandb: Downloading large artifact 1gb:v0, 968.00MB. 1 files...
wandb:   1 of 1 files downloaded.
Done. 0:0:0.3 (2978.3MB/s)
(.venv) $ src/github.com/pingleiwandb/wandb-scripts/artifacts python3 download_md5_cache.py
wandb: Currently logged in as: pinglei (reg-team-2) to https://api.wandb.ai. Use `wandb login --relogin` to force relogin
wandb: Downloading large artifact 1gb:v0, 968.00MB. 1 files...
wandb:   1 of 1 files downloaded.
Done. 0:0:0.3 (3368.9MB/s)

(.venv) $ src/github.com/pingleiwandb/wandb-scripts/artifacts tree .
.
├── 1gb.bin
├── a.txt
├── artifacts
│   └── 1gb:v0
│       ├── 1gb.bin
│       └── 1gb.bin.wbchecksum
├── download_md5_cache.py
"""