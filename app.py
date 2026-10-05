from datetime import date
import pandas as pd
import plotly.express as px
import streamlit as st
from data import generar_ventas

st.set_page_config(page_title="Ventas 360", page_icon="📊", layout="wide")

@st.cache_data
def cargar_datos():
    return generar_ventas()

def cop(valor):
    return "$ " + f"{valor:,.0f}".replace(",", ".")

df = cargar_datos()
st.title("📊 Ventas 360")
st.caption("Dashboard educativo · 1.200 pedidos simulados de 2025 · Valores en pesos colombianos (COP)")
with st.sidebar:
    st.header("Filtros")
    categorias = st.multiselect("Categorías", sorted(df.categoria.unique()), default=sorted(df.categoria.unique()))
    ciudades = st.multiselect("Ciudades", sorted(df.ciudad.unique()), default=sorted(df.ciudad.unique()))
    fechas = st.date_input("Periodo", value=(date(2025, 1, 1), date(2025, 12, 31)),
                          min_value=date(2025, 1, 1), max_value=date(2025, 12, 31))
    st.info("Datos ficticios generados con semilla 42. No representan una empresa real.")
if len(fechas) != 2:
    st.info("Selecciona la fecha inicial y final.")
    st.stop()
inicio, fin = fechas
vista = df[df.categoria.isin(categorias) & df.ciudad.isin(ciudades)
           & df.fecha.between(pd.Timestamp(inicio), pd.Timestamp(fin))].copy()
if vista.empty:
    st.warning("No hay pedidos con estos filtros. Amplía el periodo o selecciona más categorías y ciudades.")
    st.stop()
a, b, c, d = st.columns(4)
a.metric("Ventas totales", cop(vista.venta.sum()))
b.metric("Pedidos", f"{len(vista):,}".replace(",", "."))
c.metric("Unidades", f"{vista.unidades.sum():,}".replace(",", "."))
d.metric("Ticket promedio", cop(vista.venta.mean()))
mensual = vista.assign(mes=vista.fecha.dt.to_period("M").dt.to_timestamp()).groupby("mes", as_index=False).venta.sum()
st.plotly_chart(px.line(mensual, x="mes", y="venta", markers=True, title="Evolución mensual de ventas",
                        labels={"mes": "Mes", "venta": "Ventas (COP)"}), width="stretch")
izquierda, derecha = st.columns(2)
with izquierda:
    productos = vista.groupby("producto", as_index=False).venta.sum().sort_values("venta")
    st.plotly_chart(px.bar(productos, x="venta", y="producto", orientation="h", title="Ventas por producto",
                           labels={"venta": "Ventas (COP)", "producto": "Producto"}), width="stretch")
with derecha:
    grupos = vista.groupby("categoria", as_index=False).venta.sum()
    st.plotly_chart(px.pie(grupos, names="categoria", values="venta", hole=.5, title="Participación por categoría"),
                    width="stretch")
st.subheader("Detalle de pedidos")
st.dataframe(vista.sort_values("fecha"), width="stretch", hide_index=True)
st.download_button("Descargar datos filtrados (CSV)", vista.to_csv(index=False).encode("utf-8-sig"),
                   file_name="ventas_filtradas.csv", mime="text/csv")
