import json

# Carrega os personagens
with open(r"C:\Users\João Vitor\Desktop\Python\Super_Trunfo\baralho.json", "r", encoding="utf-8") as f:
    personagens = json.load(f)

# Função de normalização para 60–100 (evita valores baixos demais e não passa de 100)
def normalizar(valor, minimo, maximo, novo_min=50, novo_max=100):
    if maximo == minimo:
        return round((novo_min + novo_max) / 2)
    return round(((valor - minimo) / (maximo - minimo)) * (novo_max - novo_min) + novo_min)

# Encontra mínimo e máximo para cada atributo
minimos = {
    "forca": min(p["forca"] for p in personagens),
    "inteligencia": min(p["inteligencia"] for p in personagens),
    "influencia": min(p["influencia"] for p in personagens)
}
maximos = {
    "forca": max(p["forca"] for p in personagens),
    "inteligencia": max(p["inteligencia"] for p in personagens),
    "influencia": max(p["influencia"] for p in personagens)
}

# Aplica a normalização em todos os personagens
ajustados = []
for p in personagens:
    novo = p.copy()
    novo["forca"] = normalizar(p["forca"], minimos["forca"], maximos["forca"])
    novo["inteligencia"] = normalizar(p["inteligencia"], minimos["inteligencia"], maximos["inteligencia"])
    novo["influencia"] = normalizar(p["influencia"], minimos["influencia"], maximos["influencia"])
    ajustados.append(novo)

# Salva em um novo arquivo
with open("personagens_normalizados.json", "w", encoding="utf-8") as f:
    json.dump(ajustados, f, ensure_ascii=False, indent=2)

print("Atributos normalizados para faixa 60–100, mantendo equilíbrio e sem ultrapassar o limite.")
