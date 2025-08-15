# filepath: /prtg-fastapi/src/main.py
from fastapi import FastAPI
import requests
import json

app = FastAPI()

@app.get("/api/v1/prtg-sic")
async def prtg_sic():
    # Lista de IDs
    ids = [4162,6625,6660]

    # Parámetros comunes
    base_url = "https://monitor.sic.gov.co/api/historicdata.json"
    params = {
        "sdate": "2025-07-20-00-00-00",
        "edate": "2025-07-22-00-00-00",
        "avg": "86400",
        "usecaption": "1",
        "username": "TableroBI",
        "passhash": "3170827812"
    }

    # Lista para almacenar todos los resultados
    resultados = []

    for id_val in ids:
        params["id"] = str(id_val)  # reemplaza el ID en los parámetros
        response = requests.get(base_url, params=params)

        if response.status_code == 200:
            try:
                data = response.json()
                resultados.append({"id": id_val, "data": data})
            except json.JSONDecodeError:
                resultados.append({"id": id_val, "error": "Error decodificando JSON"})
        else:
            resultados.append({"id": id_val, "error": f"HTTP {response.status_code}"})

    return resultados
