# Training Instructions

- Create a new python environment using your favourite environment manager (`venv`/`*conda`), installing `tensorflow 1.15.0` at the same time:
    - `conda create --name gpt2-quote python=3.7 tensorflow-gpu=1.15.0`
- Install the other required libraries:
    - `pip3 install pandas gpt-2-simple`
- Download the data from [Google Drive](https://drive.google.com/drive/folders/1Ru6Ple6WLdU-b5ihBl9qc_GoAJiWnjP2?usp=sharing) and place in the `data/` subfolder. You can use the `filtered` dataset and preprocess it or skip straight to training with the preprocessed version
- Preprocess the data:
    - `python preprocess.py`
- Train the model:
    - `python train.py`