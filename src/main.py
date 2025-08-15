# filepath: /prtg-fastapi/src/main.py
from fastapi import FastAPI
import requests
import json

app = FastAPI()

@app.get("/api/v1/prtg-sic")
async def prtg_sic():
    # Lista de IDs
    ids = [97097, 93334, 93349, 93231, 93212, 102140, 102133, 93337, 93352, 93230,
            93211, 93229, 93210, 93336, 93351, 93335, 93350, 93228, 93209, 93227,
            93208, 93241, 93207, 93226, 93206, 93339, 93354, 93225, 93205, 93224,
            93204, 100540, 100541, 93223, 93203, 93222, 93202, 93362, 93359, 93221,
            93201, 93341, 93356, 93343, 93358, 100033, 100038, 100028, 100035, 100037,
            100030, 100034, 100032, 100029, 100043, 100027, 100039, 100042, 100040,
            100026, 100036, 100041, 100217, 100545, 100531, 100544, 97801, 97800,
            100533, 100532, 98595, 93346, 93360, 93347, 93361, 4162, 6625, 6660, 6753,
            17972, 18820, 22932, 23075, 29326, 29516, 29643, 34005, 34204, 41695,
            44197, 44199, 51858, 82003, 82052, 82103, 82401, 82565, 82616, 85041,
            86793, 86815, 94561, 96000, 96362, 96374, 96908, 96922, 96957, 96958,
            96960, 96962, 96967, 97050, 97132, 97804, 98394, 98437, 102182, 93220,
            93199, 1002, 1001, 1003, 93333, 93348, 93219, 93198, 93218, 93197, 93217,
            93196, 93338, 93353, 93340, 93355, 93216, 93195, 93215, 93194, 101607,
            101616, 93214, 93193, 93213, 93192, 93342, 93357]

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
