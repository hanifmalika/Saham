import streamlit as st
import pandas as pd
import plotly.graph_objects as go

from screener import red_streak
from data_loader import get_stock_data


st.set_page_config(
    page_title="Screener Saham",
    layout="wide",
)

st.title("Screener Saham Indonesia ")

st.write("Mencari saham yang turun berturut turut")

hari = st.selectbox("Pilih jumlah hari berturut turut turun", [1,2, 3, 4, 5])

st.write(f"Filter: {hari} hari")

saham_list = saham_list = [
    "BBCA", "BBRI", "BMRI", "BBNI", "BBTN",
    "TLKM", "EXCL", "ISAT", "MTEL", "FREN",

    "ASII", "AUTO", "UNTR", "IMAS", "SMSM",
    "GJTL", "LPKR", "BSDE", "PWON", "CTRA",

    "ANTM", "INCO", "MDKA", "TINS", "HRUM",
    "ADRO", "PTBA", "ITMG", "INDY", "BUMI",

    "PGAS", "MEDC", "AKRA", "ELSA", "ESSA",
    "BRPT", "TPIA", "CPIN", "JPFA", "MAIN",

    "ICBP", "INDF", "MYOR", "ULTJ", "ROTI",
    "GOOD", "STTP", "AISA", "CLEO", "DLTA",

    "UNVR", "SIDO", "KLBF", "KAEF", "INAF",
    "HEAL", "MIKA", "SILO", "SRAJ", "PRDA",

    "ACES", "AMRT", "ERAA", "MAPI", "RALS",
    "LPPF", "CSAP", "MIDI", "MPPA", "ECII",

    "GOTO", "BUKA", "BELI", "DCII", "NETV",
    "SCMA", "MNCN", "TMAS", "JSMR", "WIKA",

    "WSKT", "PTPP", "ADHI", "TOTL", "WEGE",
    "SMGR", "INTP", "WSBP", "DGIK", "NRCA",

    "ABMM", "BIRD", "CTRA", "BSDE", "PWON",
    "KIJA", "DMAS", "SMRA", "WOOD", "SSIA"
]


hasil = []

if st.button("Cari Saham"):
    with st.spinner("Scanning saham..."):
        for saham in saham_list:
            try:
                if red_streak(saham, hari):
                    hasil.append(saham)
            except Exception:
                pass
df = pd.DataFrame(hasil, columns=["Saham"])
st.dataframe(df,use_container_width=True)

st.divider()

ticker = st.text_input("Masukkan ticker saham (contoh: BBCA)")

if ticker:
    data = get_stock_data(ticker.upper())
    st.write(data.tail())
    
    
if ticker:
    
    data = get_stock_data(
        ticker.upper()
    )

    harga_terakhir = round(
        data["Close"].iloc[-1],
        2
    )

    st.metric(
        "Harga Terakhir",
        harga_terakhir
    )
    
    fig = go.Figure(
        data=[
            go.Candlestick(
                x=data.index,
                open=data["Open"],
                high=data["High"],
                low=data["Low"],
                close=data["Close"],
            )
        ]
    )
    
    st.plotly_chart(
        fig, use_container_width=True
    )
    
    data["MA20"] = data["Close"].rolling(window=20).mean()
    fig.add_scatter(
        x=data.index,
        y=data["MA20"],
        mode="lines",
        name="MA20",
    )
    
    col1,col2,col3 = st.columns(3)
    
    with col1:
        st.metric(
            "Open",
            round(data["Open"].iloc[-1], 2)
        )
    with col2:
        st.metric(
            "High",
            round(data["High"].iloc[-1], 2)
        )
    with col3:
        st.metric(
            "volume",
            int(data["Volume"].iloc[-1])
        )
        
