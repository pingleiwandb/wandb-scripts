import wandb

# python3 -m venv .venv
# source .venv/bin/activate
# pip install wandb
def main():
    # Force to use wandb prod endpoint
    wandb.login(host="https://api.wandb.ai")
    # Entity is team name, NOT org name
    with wandb.init(entity="pinglei-byob-3", project="log-txt", name="txt") as run:
        artifact = wandb.Artifact(name="txt", type="dataset")
        artifact.add_file(local_path="./a.txt")
        artifact.save()

if __name__ == "__main__":
    main()