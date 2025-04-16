# Setting up wandb on Colab

Using official release:

```bash
!pip install wandb
```

Build from source:

```bash
# Install Go
!add-apt-repository -y ppa:longsleep/golang-backports
!apt update
!apt install -y golang-go
!go version

# NOTE: Change to your own fork/branch
!git clone --single-branch --branch pinglei/artifact-download-py-parallel-v0 https://github.com/pingleiwandb/wandb.git
!pip install -U nox uv
%cd wandb
# Skip Rust, install system wide in edit mode
!WANDB_BUILD_SKIP_GPU_STATS=true uv pip install -e . --system --prerelease allow
```

Test it's working

```python
import wandb

wandb.login()
```

