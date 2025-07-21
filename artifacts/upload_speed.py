import os
import random
import wandb
import time
import argparse

def create_random_file(filename, size_gb):
    # Check if file already exists
    if os.path.exists(filename):
        print(f"File {filename} already exists, skipping creation.")
        return os.path.abspath(filename)
    
    size_bytes = size_gb * 1024 * 1024 * 1024  # Convert GB to bytes
    chunk_size = 1024 * 1024  # 1MB chunks for efficient writing
    
    print(f"Creating {filename} with {size_gb}GB of random data...")
    
    with open(filename, 'wb') as f:
        bytes_written = 0
        while bytes_written < size_bytes:
            # Generate random bytes for the chunk
            remaining = min(chunk_size, size_bytes - bytes_written)
            random_bytes = random.randbytes(remaining)
            f.write(random_bytes)
            bytes_written += remaining
            
            # Progress indicator
            if bytes_written % (100 * 1024 * 1024) == 0:  # Every 100MB
                progress = (bytes_written / size_bytes) * 100
                print(f"Progress: {progress:.1f}% ({bytes_written // (1024*1024*1024)}GB written)")
    
    print(f"Successfully created {filename} ({size_gb}GB)")
    return os.path.abspath(filename)

def upload_file(size_gb, entity, project):
    wandb.login()

    # Create file if not exists
    filename = f"{size_gb}gb.bin"
    file_path = create_random_file(filename, size_gb)
    print(f"File created at: {file_path}")

    # Get file size in bytes for speed calculation
    file_size_bytes = os.path.getsize(file_path)
    file_size_mb = file_size_bytes / (1024 * 1024)  # Convert to MB
    
    print(f"Starting upload of {file_size_mb:.2f} MB...")
    start_time = time.time()

    with wandb.init(entity=entity, project=project, name=f"upload-{filename}") as run:
        artifact = wandb.Artifact(name=filename, type="dataset")
        # Immtuable disable copying to a temp file before upload
        # Skip cache disable copying to cache dir after upload is done
        artifact.add_file(filename, skip_cache=True, policy="immutable")
        artifact.save()
        # Wait until upload is done because save() is async
        artifact.wait()
    
    end_time = time.time()
    upload_time = end_time - start_time
    upload_speed_mbps = file_size_mb / upload_time
    
    print(f"Upload completed! File: {file_size_mb:.2f} MB, Time: {upload_time:.2f}s, Speed: {upload_speed_mbps:.2f} MB/s")

# NOTE: You need to set the following env vars to turn on debug log and unreleased features
# export WANDB_DEBUG=true
# export WANDB_CORE_DEBUG=true
# export WANDB_DISABLE_KEEPALIVE=true
# export WANDB_ENABLE_MULTIPART_HASHING=true
# To find the log, run in wandb folder 
# grep -r --include="*.log" "TimeMs" .
#
# Example command:
# python3 upload_speed.py --size 10 --entity reg-team-2 --project pinglei-wbench-gcs-upload-v20250721-v2
def main():
    parser = argparse.ArgumentParser(description='Create and upload files to wandb with speed measurement')
    parser.add_argument('--size', type=int, required=True, help='File size in GB')
    parser.add_argument('--entity', type=str, required=True, help='Wandb entity name')
    parser.add_argument('--project', type=str, required=True, help='Wandb project name')
    
    args = parser.parse_args()
    
    upload_file(args.size, args.entity, args.project)

if __name__ == "__main__":
    main()

