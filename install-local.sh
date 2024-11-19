mkdir -p log
mkdir -p archived/raw
mkdir -p archived/staged
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
export FLASK_APP=webapp/mosef.py
export FLASK_ENV=development
