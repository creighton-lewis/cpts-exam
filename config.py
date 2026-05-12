import os 
import subprocess 
import sys 

os.system(f"wget https://raw.githubusercontent.com/creighton-lewis/Environment-FIles/refs/heads/main/.tmux.conf")
os.system(f"source-file .tmux.conf")
os.system(f"wget https://raw.githubusercontent.com/creighton-lewis/Environment-FIles/refs/heads/main/.zshrc")
os.system(f"source ~/.zshrc")