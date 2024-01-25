import pandas as pd
import requests


def get_request(url):
    try:
        headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
                   'Accept-Language': 'en'}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            print(response.text)
            return response.text
        else:
            print(f"Request failed with status code: {response.status_code}")
            return str(response.status_code)
    except Exception as e:
        print(f"An error occurred during the request: {e}")
        return str(e)


with open('ids.txt') as ids:
    ids = ids.readlines()

matriz = []
for mnk_id in ids:
    mnk_id = mnk_id.strip()
    url = f'https://api-zbiory.mnk.pl/api/object/{mnk_id}'
    data = get_request(url)
    payload = [mnk_id, data]
    matriz.append(payload)

columns = ['id', 'data']
df = pd.DataFrame(matriz, columns=columns)
df.to_excel('results_API.xlsx', index=False)
