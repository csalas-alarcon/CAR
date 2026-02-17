python -m venv .venv 
source .venv/bin/activate 

pip install -r requirements.txt

python code/visualize.py

rm -rf .venv