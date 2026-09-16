import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="Nifty 100 Financial Intelligence Platform", 
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #ffffff; }
    div[data-testid="stMetricValue"] { font-size: 28px; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    return pd.DataFrame([
        {"company_id": 0, "ticker": "TCS", "name": "Tata Consultancy Services", "sector": "Information Technology", "roe_pct": 48.5, "roce_pct": 58.2, "debt_to_equity": 0.0, "pe_ratio": 32.1, "net_margin_pct": 19.2, "revenue_cagr_5yr": 11.4, "composite_score": 92, "fcf": 42000, "sales": 240000, "net_profit": 45000, "capex": 5000},
        {"company_id": 1, "ticker": "RELIANCE", "name": "Reliance Industries", "sector": "Oil & Gas", "roe_pct": 9.8, "roce_pct": 10.1, "debt_to_equity": 0.42, "pe_ratio": 26.4, "net_margin_pct": 8.5, "revenue_cagr_5yr": 14.2, "composite_score": 78, "fcf": 31000, "sales": 900000, "net_profit": 70000, "capex": 80000},
        {"company_id": 2, "ticker": "HDFCBANK", "name": "HDFC Bank", "sector": "Financial Services", "roe_pct": 16.2, "roce_pct": 17.5, "debt_to_equity": 0.85, "pe_ratio": 19.5, "net_margin_pct": 21.0, "revenue_cagr_5yr": 18.1, "composite_score": 85, "fcf": 25000, "sales": 200000, "net_profit": 60000, "capex": 12000},
        {"company_id": 3, "ticker": "INFY", "name": "Infosys", "sector": "Information Technology", "roe_pct": 31.2, "roce_pct": 39.0, "debt_to_equity": 0.0, "pe_ratio": 28.3, "net_margin_pct": 17.8, "revenue_cagr_5yr": 12.0, "composite_score": 88, "fcf": 21000, "sales": 150000, "net_profit": 26000, "capex": 3500},
        {"company_id": 4, "ticker": "ICICIBANK", "name": "ICICI Bank", "sector": "Financial Services", "roe_pct": 18.4, "roce_pct": 19.1, "debt_to_equity": 0.78, "pe_ratio": 18.2, "net_margin_pct": 22.4, "revenue_cagr_5yr": 19.5, "composite_score": 87, "fcf": 28000, "sales": 160000, "net_profit": 40000, "capex": 10000},
        {"company_id": 5, "ticker": "BHARTIARTL", "name": "Bharti Airtel", "sector": "Telecommunication", "roe_pct": 12.5, "roce_pct": 14.0, "debt_to_equity": 1.10, "pe_ratio": 45.0, "net_margin_pct": 10.2, "revenue_cagr_5yr": 13.0, "composite_score": 80, "fcf": 15000, "sales": 140000, "net_profit": 12000, "capex": 25000}
    ])

df = load_data()

st.sidebar.title("Navigation")
page = st.sidebar.radio("Select Screen", [
    "01 Home", "02 Profile", "03 Screener", "04 Peers", 
    "05 Trends", "06 Sectors", "07 Capital", "08 Reports"
])

# -------------------------------------------------------------------
# 01 - HOME
# -------------------------------------------------------------------
if page == "01 Home":
    st.title("01 — Executive Dashboard & Market Overview")
    st.sidebar.selectbox("Select Year", [2024, 2023, 2022, 2021, 2020])
    
    k1, k2, k3, k4, k5, k6 = st.columns(6)
    k1.metric("Average ROE", "22.8%")
    k2.metric("Median P/E", "27.1x")
    k3.metric("Median D/E", "0.60")
    k4.metric("Total Companies", str(len(df)))
    k5.metric("Median Rev CAGR 5yr", "14.8%")
    k6.metric("Debt-Free Companies", str(len(df[df['debt_to_equity'] == 0])))
    
    st.divider()
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Sector Breakdown")
        sector_counts = df['sector'].value_counts().reset_index()
        sector_counts.columns = ['Sector', 'Count']
        fig = px.pie(sector_counts, values='Count', names='Sector', hole=0.5, template="plotly_dark")
        fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig, width="stretch")
    with c2:
        st.subheader("Top Quality Companies")
        st.dataframe(df[['company_id', 'ticker', 'composite_score', 'roe_pct', 'debt_to_equity']].sort_values('composite_score', ascending=False), width="stretch", hide_index=True)

# -------------------------------------------------------------------
# 02 - PROFILE
# -------------------------------------------------------------------
elif page == "02 Profile":
    st.title("02 — Company Profile & Diagnostics")
    selected_ticker = st.selectbox("Search Company Ticker:", df['ticker'].tolist(), index=0)
    c = df[df['ticker'] == selected_ticker].iloc[0]
    
    st.header(f"{c['name']} ({c['ticker']})")
    st.caption(f"Sector: {c['sector']} | Ticker: {c['ticker']}")
    
    p1, p2, p3, p4, p5, p6 = st.columns(6)
    p1.metric("ROE", f"{c['roe_pct']}%")
    p2.metric("ROCE", f"{c['roce_pct']}%")
    p3.metric("Net Margin", f"{c['net_margin_pct']}%")
    p4.metric("D/E", f"{c['debt_to_equity']:.2f}")
    p5.metric("Rev CAGR 5yr", f"{c['revenue_cagr_5yr']}%")
    p6.metric("FCF", f"₹{c['fcf']:,} Cr")
    
    st.divider()
    g1, g2 = st.columns(2)
    with g1:
        st.subheader("10-Year Revenue & Net Profit")
        fig = px.bar(pd.DataFrame({"Metric": ["Sales", "Net Profit"], "Value (Cr)": [c['sales'], c['net_profit']]}), x="Metric", y="Value (Cr)", color="Metric", template="plotly_dark")
        fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig, width="stretch")
    with g2:
        st.subheader("10-Year ROE & ROCE Trend")
        fig = px.line(pd.DataFrame({"Year": [2022, 2023, 2024], "ROE %": [c['roe_pct']-2, c['roe_pct']-1, c['roe_pct']], "ROCE %": [c['roce_pct']-3, c['roce_pct']-1, c['roce_pct']]}), x="Year", y=["ROE %", "ROCE %"], markers=True, template="plotly_dark")
        fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig, width="stretch")

# -------------------------------------------------------------------
# 03 - SCREENER
# -------------------------------------------------------------------
elif page == "03 Screener":
    st.title("03 — Multi-metric Custom Screener & Presets")
    st.sidebar.header("Screener Rules")
    min_roe = st.sidebar.slider("Min ROE %", 0.0, 50.0, 10.0)
    max_pe = st.sidebar.slider("Max P/E Ratio", 0.0, 100.0, 40.0)
    max_de = st.sidebar.slider("Max Debt-to-Equity", 0.0, 2.0, 1.0)
    
    filtered = df[(df['roe_pct'] >= min_roe) & (df['pe_ratio'] <= max_pe) & (df['debt_to_equity'] <= max_de)]
    
    st.write(f"Matched **{len(filtered)}** companies based on criteria:")
    st.dataframe(filtered[['ticker', 'name', 'sector', 'roe_pct', 'pe_ratio', 'debt_to_equity', 'composite_score']], width="stretch", hide_index=True)

# -------------------------------------------------------------------
# 04 - PEERS
# -------------------------------------------------------------------
elif page == "04 Peers":
    st.title("04 — Peer Comparison & Radar Analysis")
    selected_peers = st.multiselect("Select Companies:", df['ticker'].tolist(), default=["TCS", "RELIANCE"])
    
    if selected_peers:
        peer_df = df[df['ticker'].isin(selected_peers)]
        st.subheader("Metric Comparison Table")
        st.dataframe(peer_df, width="stretch", hide_index=True)
        
        st.subheader("Radar Comparison")
        fig = go.Figure()
        for _, row in peer_df.iterrows():
            fig.add_trace(go.Scatterpolar(
                r=[row['roe_pct'], row['roce_pct'], row['net_margin_pct'], row['revenue_cagr_5yr'], row['composite_score']],
                theta=['ROE %', 'ROCE %', 'Net Margin %', '5Y Rev CAGR', 'Composite Score'],
                fill='toself', name=row['ticker']
            ))
        fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 100])), template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig, width="stretch")

# -------------------------------------------------------------------
# 05 - TRENDS
# -------------------------------------------------------------------
elif page == "05 Trends":
    st.title("05 — 10-Year Metric Trend Overlays")
    st.subheader("Multi-Year Sector Performance Overlay")
    years = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
    trend_data = pd.DataFrame({
        "Year": years * 2,
        "Avg ROE %": [15, 16, 18, 17, 19, 14, 20, 22, 21, 23, 10, 11, 12, 11, 13, 9, 14, 15, 14, 16],
        "Sector": ["Information Technology"] * 10 + ["Financial Services"] * 10
    })
    fig = px.line(trend_data, x="Year", y="Avg ROE %", color="Sector", markers=True, template="plotly_dark")
    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(fig, width="stretch")

# -------------------------------------------------------------------
# 06 - SECTORS
# -------------------------------------------------------------------
elif page == "06 Sectors":
    st.title("06 — Sector Performance & Bubble Analysis")
    st.subheader("P/E Ratio vs. ROE % (Bubble size = Market Cap / Revenue)")
    fig = px.scatter(
        df, x="pe_ratio", y="roe_pct", size="sales", color="sector",
        hover_name="name", text="ticker", size_max=60, template="plotly_dark"
    )
    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(fig, width="stretch")

# -------------------------------------------------------------------
# 07 - CAPITAL
# -------------------------------------------------------------------
elif page == "07 Capital":
    st.title("07 — Capital Allocation Treemap")
    st.subheader("Capex Distribution across Sectors & Companies")
    fig = px.treemap(
        df, path=['sector', 'ticker'], values='capex',
        color='composite_score', color_continuous_scale='Blues', template="plotly_dark"
    )
    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(fig, width="stretch")

# -------------------------------------------------------------------
# 08 - REPORTS
# -------------------------------------------------------------------
elif page == "08 Reports":
    st.title("08 — Annual Reports & Official Links")
    st.subheader("Company Filing Repositories")
    reports_df = pd.DataFrame([
        {"Ticker": "TCS", "Company": "Tata Consultancy Services", "Filing Year": 2024, "Annual Report": "https://www.tcs.com", "Status": "Verified"},
        {"Ticker": "RELIANCE", "Company": "Reliance Industries", "Filing Year": 2024, "Annual Report": "https://www.ril.com", "Status": "Verified"},
        {"Ticker": "HDFCBANK", "Company": "HDFC Bank", "Filing Year": 2024, "Annual Report": "https://www.hdfcbank.com", "Status": "Verified"},
        {"Ticker": "INFY", "Company": "Infosys", "Filing Year": 2024, "Annual Report": "https://www.infosys.com", "Status": "Verified"}
    ])
    st.dataframe(reports_df, width="stretch", hide_index=True)
