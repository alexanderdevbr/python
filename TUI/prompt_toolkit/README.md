python -m venv venv
source ./venv/bin/activate
python -m pip list
python -m pip install -r requirements.txt
python -m pip list
# ./venv/bin/pyinstaller --onefile ./simple_prompt.py
# ls -lh dist/simple_prompt
# python -m pip freeze > requirements.txt
