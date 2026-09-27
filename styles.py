def load_css():
    return """
    <style>

    .stApp{
        background:#F5F7FA;
    }

    h1{
        color:#1565C0;
        text-align:center;
        font-weight:bold;
    }

    h2,h3{
        color:#1565C0;
    }

    section[data-testid="stSidebar"]{
        background:#0B1F33;
    }

    section[data-testid="stSidebar"] *{
        color:white;
    }

    .stButton>button{
        width:100%;
        border-radius:12px;
        height:50px;
        font-size:18px;
        font-weight:bold;
        background:#1565C0;
        color:white;
        border:none;
    }

    .stButton>button:hover{
        background:#0D47A1;
    }

    div[data-testid="stMetric"]{
        background:white;
        border-radius:15px;
        padding:15px;
        box-shadow:0 4px 10px rgba(0,0,0,.10);
    }

    textarea{
        border-radius:12px !important;
    }

    </style>
    """