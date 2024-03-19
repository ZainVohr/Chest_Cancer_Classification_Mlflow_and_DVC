# Chest_Cancer_Classification_Mlflow_and_DVC


## Workflows

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml

# How to run?
### Steps

Clone The repo

```bash
https://github.com/ZainVohr/Chest_Cancer_Classification_Mlflow_and_DVC.git
```

### Step 01 - Create a conda environment after opening the repo

```bash
conda create -n your_environment_name python=3.8 -y
conda activate your_environment_name
```

### Step 02- Install the requirements
```bash
pip install -r requirements.txt
```

### dagshub
[dagshub](https://dagshub.com/)

You will get the credential once you connect your repo to dagshub with add revoke access

Run this to export as env variables:

```bash 
use set instead of export if using windows

export MLFLOW_TRACKING_URI=Your MLFLOW_TRACKING_URI

export MLFLOW_TRACKING_PASSWORD=Your MLFLOW_TRACKING_PASSWORD

export MLFLOW_TRACKING_USERNAME= Your MLFLOW_TRACKING_USERNAME
```

### Data Version control cmd
1. dvc init
2. dvc repro
3. dvc dag

#### About Mlflow and DVC

MLflow

 - Its Production Grade
 - Trace all of your expriements
 - Logging & taging your model


DVC 

 - Its very light weight for POC only
 - light weight expriements tracker
 - It can perform Orchestration (Creating Pipelines)

