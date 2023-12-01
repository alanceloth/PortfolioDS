import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from urllib.parse import urlparse, parse_qs
import json
import os


def get_code(driver_path, Client_ID, redirect_uri, state, email, password):

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)

    try:
        # Construção da URL de autorização do LinkedIn
        url_oauth = 'https://www.linkedin.com/oauth/v2/authorization?'
        params_oauth = {
            'response_type': 'code',
            'client_id': Client_ID,
            'redirect_uri': redirect_uri,
            'state': state,
            'scope': "profile email openid w_member_social"
        }
        driver.get(url_oauth + '&'.join(f'{k}={v}' for k, v in params_oauth.items()))

        # Captura de tela após abrir a página de autorização
        driver.save_screenshot('../Bot LinkedIn/screenshots/screenshot_open.png')

        # Preenchimento do campo de nome de usuário e senha
        username_field = driver.find_element(By.ID, 'username')
        password_field = driver.find_element(By.ID, 'password')
        username_field.send_keys(email)
        password_field.send_keys(password)

        # Captura de tela após preencher os campos
        driver.save_screenshot('../Bot LinkedIn/screenshots/screenshot_filled.png')

        # Clique no botão "Sign in"
        sign_in_button = driver.find_element(By.XPATH, "//button[@aria-label='Sign in']")
        sign_in_button.click()

        # Espera implícita para carregar a próxima página
        driver.implicitly_wait(3)

        # Captura de tela após o login
        driver.save_screenshot('../Bot LinkedIn/screenshots/screenshot_login.png')

        # Análise da URL atual para obter o código
        parsed_url = urlparse(driver.current_url)
        query_params = parse_qs(parsed_url.query)
        code = query_params.get('code', [''])[0]

        return code

    finally:
        # Encerramento do driver
        driver.quit()

def get_access_token_linkedin(Client_ID, Client_Secret, code, redirect_uri):
    url = 'https://www.linkedin.com/oauth/v2/accessToken'
    params = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': redirect_uri,
        'client_id': Client_ID,
        'client_secret': Client_Secret
    }
    response = requests.post(url, data=params)

    if response.status_code == 200:
        access_token = response.json().get('access_token')
        return access_token
    else:
        print(f'Error: {response.status_code} - {response.text}')
        return None
    

def get_sub_id_linkedin(access_token):
    url = 'https://api.linkedin.com/v2/userinfo'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Connection': 'Keep-Alive',
        'Content-Type': 'application/json',
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = json.loads(response.content)
        sub_value = data.get("sub")
        return sub_value
    else:
        print(f'Erro: {response.status_code} - {response.text}')
        return None
    

def create_linkedin_post(access_token, user_id, text, visibility, media_category, media_description, media_url, media_title):
    """
    Cria um post no LinkedIn com base nos parâmetros fornecidos.

    Args:
        access_token (str): Token de acesso do LinkedIn.
        user_id (str): ID do perfil do usuário no LinkedIn.
        text (str): Texto do post.
        visibility (str): Visibilidade do post ('CONNECTIONS' ou 'PUBLIC').
        media_category (str): Categoria de mídia para o post ('NONE', 'ARTICLE' ou 'IMAGE').
        media_description (str): Descrição da mídia (opcional).
        media_url (str): URL da mídia (opcional).
        media_title (str): Título da mídia (opcional).

    Returns:
        None
    """
    api_url = 'https://api.linkedin.com/v2/ugcPosts'

    headers = {
        'Authorization': f'Bearer {access_token}',
        'Connection': 'Keep-Alive',
        'Content-Type': 'application/json',
    }
    if media_category == 'IMAGE':
        post_body = {
            'author': f'urn:li:person:{user_id}',
            'lifecycleState': 'PUBLISHED',
            'specificContent': {
                'com.linkedin.ugc.ShareContent': {
                    'shareCommentary': {
                        'text': f'{text}',
                    },
                    'shareMediaCategory': media_category,
                    "media": [
                {
                    "status": "READY",
                    "description": {
                        "text": media_description
                    },
                    "media": media_url,
                    "title": {
                        "text": media_title
                            }
                        }
                    ],
                },
            },
            'visibility': {
                'com.linkedin.ugc.MemberNetworkVisibility': visibility,
            },
        }
    elif media_category == 'ARTICLE':
        post_body = {
            'author': f'urn:li:person:{user_id}',
            'lifecycleState': 'PUBLISHED',
            'specificContent': {
                'com.linkedin.ugc.ShareContent': {
                    'shareCommentary': {
                        'text': f'{text}',
                    },
                    'shareMediaCategory': media_category,
                    'media': [
                        {
                            'status': 'READY',
                            'description': {
                                'text': media_description,
                            },
                            'originalUrl': media_url,
                        },
                    ],
                },
            },
            'visibility': {
                'com.linkedin.ugc.MemberNetworkVisibility': visibility,
            },
        }

    response = requests.post(api_url, headers=headers, json=post_body)
    if response.status_code == 201:
        print('Post criado com sucesso!')
    else:
        print(f'Falha na criação do post - Código de status {response.status_code}: {response.text}')


