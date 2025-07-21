sudo add-apt-repository -y ppa:longsleep/golang-backports
sudo apt update
sudo apt install -y golang-go python3-pip python3.12-venv
go version

# Get branch and remote, use defaults if files don't exist
WANDB_BRANCH="pinglei/mulitpart-parallel-hash-0721"
WANDB_REMOTE="https://github.com/wandb/wandb.git"

# Clone specific branch
git clone --single-branch --branch "$WANDB_BRANCH" "$WANDB_REMOTE" wandbsrc

python3 -m venv .venv
source .venv/bin/activate
pip install -U nox uv

WANDB_BUILD_SKIP_GPU_STATS=true uv pip install -e ./wandbsrc

# Copy paste the following before running the script
export WANDB_DEBUG=true
export WANDB_CORE_DEBUG=true
export WANDB_DISABLE_KEEPALIVE=true
export WANDB_ENABLE_MULTIPART_HASHING=true