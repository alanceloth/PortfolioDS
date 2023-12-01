import functions.linkedin_api as lnkd
import yaml
import random
import os

print("Current working directory:", os.getcwd())

# Usar o caminho correto do webdriver e do config.yaml
driver_path = f"{os.getcwd()}\Bot LinkedIn\webdriver\chromedriver.exe"
stream = open(f"{os.getcwd()}\Bot LinkedIn\config.yaml", 'r')

c = yaml.safe_load(stream)
Client_ID = c['Client_ID']
Client_Secret = c['Client_Secret']
email = c['Email']
password = c['Senha']

redirect_uri = 'https://www.linkedin.com/in/alanlanceloth'
state = random.randint(0,100000)

def main():
    code = lnkd.get_code(driver_path, Client_ID, redirect_uri, state, email, password)
    access_token = lnkd.get_access_token_linkedin(Client_ID, Client_Secret, code, redirect_uri)
    sub_id = lnkd.get_sub_id_linkedin(access_token)
    user_id = sub_id
    text = 'Olá, mundo!'
    visibility = 'CONNECTIONS'  # Pode ser 'CONNECTIONS' ou 'PUBLIC'
    media_category = 'ARTICLE'  # Pode ser 'NONE', 'ARTICLE' ou 'IMAGE'
    media_description = 'Teste'
    media_url = 'https://www.linkedin.com/in/alanlanceloth/'
    media_title = 'N/A'

    lnkd.create_linkedin_post(access_token, user_id, text, visibility, media_category, media_description, media_url, media_title)

if __name__ == '__main__':
    main()
