#!/bin/bash
#SBATCH --job-name=sasrec_ml1m
#SBATCH --partition=gpu_a100
#SBATCH --gres=gpu:1
#SBATCH --cpus-per-task=16
#SBATCH --time=02:00:00
#SBATCH --output=logs/%x_%j.out
#SBATCH -A scur0949

module load 2023
module load Anaconda3/2023.07-2
source activate popsteer
cd $HOME/PopSteer2.0

python -c "import torch; print('cuda:', torch.cuda.is_available(), torch.cuda.get_device_name(0))"
python run.py --model=SASRec --dataset=ml-1m --config_files=example_config.yaml --train