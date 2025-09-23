mkdir -p log
mkdir -p archived/raw
mkdir -p archived/staged
python3 -m venv .venv
source .venv/Scripts/activate
pip install --upgrade pip
python3 -m pip install -r requirements-local.txt
export FLASK_APP=webapp/mosef.py
export FLASK_ENV=development
