#!/bin/bash
#SBATCH --job-name=popsteer
#SBATCH --partition=gpu_a100
#SBATCH --gpus=1
#SBATCH --time=01:00:00
#SBATCH --output=slurm_%j.out

module load 2023
module load Python/3.11.3-GCCcore-12.3.0
source ~/popsteer-env/bin/activate
cd ~/PopSteer2.0

"$@"