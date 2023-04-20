from datetime import datetime

import requests
from bs4 import BeautifulSoup
from flask import Flask, request, jsonify


app = Flask(__name__)


# Endpoint para consultar el valor de la UF para una fecha específica
@app.route("/api/uf", methods=["GET"])
def get_uf_value():
    date_str = request.args.get("date")

    # Verifica que la fecha sea válida y posterior al 01-01-2013
    try:
        if not date_str or date_str < "2013-01-01":
            raise ValueError
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        return jsonify({"error": "Fecha no válida"}), 400

    url = f"https://www.sii.cl/valores_y_fechas/uf/uf{date_str[:4]}.htm"

    # Obtiene los valores de la UF desde el sitio web del SII
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.select_one("#table_export")
    rows = table.select("tr")

    # Busca el valor de la UF correspondiente a la fecha especificada
    for row in rows[1:]:
        header = row.select_one("th").text.strip()

        if header == str(date_obj.day):
            value = (
                row.select("td")[date_obj.month - 1]
                .text.strip()
                .replace(".", "")
                .replace(",", ".")
            )

            try:
                return jsonify({"date": date_str, "value": float(value)}), 200
            except ValueError:
                return jsonify({"error": "Data no disponible"}), 404

    return (
        jsonify(
            {"error": "No se encontró el valor de la UF para la fecha especificada"}
        ),
        404,
    )


if __name__ == "__main__":
    app.run(debug=True)
