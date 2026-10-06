import pandas as pd
from sodapy import socrata

def casos(limite_registros, nombre_departamento):
    client = socrata.Socrata("www.datos.gov.co", None)
    results = client.get("gt2j-8ykr", limit = limite_registros, departamento_nom = nombre_departamento.upper())
    results_dt = pd.DataFrame.from_records(results)
    return results_dt

