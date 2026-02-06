import requests

url = "http://127.0.0.1:8000/predict"

file_path = "data/test/PNEUMONIA/person100_bacteria_475.jpeg" 

try:
    with open(file_path, "rb") as f:
        files = {"file": f}
        response = requests.post(url, files=files)
        
    print("Status Code:", response.status_code)
    print("Resposta da API:", response.json())
except Exception as e:
    print(f"Erro ao testar a API: {e}")