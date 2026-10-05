"""Datos ficticios reproducibles; no representan ventas reales."""
import random
from datetime import date, timedelta
import pandas as pd


def generar_ventas():
    rng = random.Random(42)
    productos = [("Portátil", "Tecnología", 2400000), ("Audífonos", "Tecnología", 180000),
                 ("Silla", "Hogar", 320000), ("Lámpara", "Hogar", 85000),
                 ("Tenis", "Moda", 220000), ("Camiseta", "Moda", 55000)]
    registros = []
    for i in range(1200):
        producto, categoria, precio = rng.choice(productos)
        unidades = rng.randint(1, 5)
        registros.append({"pedido": i + 1, "fecha": date(2025, 1, 1) + timedelta(days=rng.randrange(365)),
                          "producto": producto, "categoria": categoria,
                          "ciudad": rng.choice(["Bogotá", "Medellín", "Cali", "Barranquilla"]),
                          "unidades": unidades, "venta": unidades * precio})
    df = pd.DataFrame(registros)
    df["fecha"] = pd.to_datetime(df["fecha"])
    return df
