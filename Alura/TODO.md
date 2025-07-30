# Criar um novo ambiente virtual
python -m venv ./venv

# Criar o ambiente virtual (Mac)
python3 -m venv ./venv

# Ativar o ambiente virtual (Mac/Linux)
source nome_do_ambiente/bin/activate

# Ativar o ambiente virtual (Windows)
.\nome_do_ambiente\Scripts\activate

# Desativar o ambiente virtual
deactivate

# Instalando dependências necessarias
pip install requests
pip freeze > requiriments.txt