from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os
import sqlite3

app = FastAPI(title="RevOps AI - Churn Predictor")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

NOME_BANCO = "revops.db"

def inicializar_banco():
    conn = sqlite3.connect(NOME_BANCO)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS socios_churn (
            id TEXT PRIMARY KEY,
            plano TEXT,
            risco REAL,
            fator_critico TEXT
        )
    ''')
    
    cursor.execute("SELECT COUNT(*) FROM socios_churn")
    if cursor.fetchone()[0] == 0:
        dados_iniciais = [
            ("7741", "Diamante", 0.92, "Ausência nos últimos 4 jogos"),
            ("8820", "Ouro", 0.65, "Queda no consumo da loja oficial"),
            ("9933", "Prata", 0.12, "Alta assiduidade (Sócio Engajado)"),
            ("1024", "Bronze", 0.81, "Inadimplência recente (15 dias)"),
            ("2055", "Ouro", 0.45, "Fim de contrato próximo"),
            ("3190", "Diamante", 0.15, "Upgrade recente de plano"),
            ("4421", "Bronze", 0.88, "Cartão de crédito recusado"),
            ("5532", "Prata", 0.55, "Redução na compra de ingressos extras"),
            ("6698", "Diamante", 0.05, "Presença em 100% dos jogos em casa"),
            ("7712", "Bronze", 0.72, "Nenhum acesso ao app há 60 dias"),
            ("8899", "Ouro", 0.38, "Mudança de endereço (outra cidade)"),
            ("9001", "Prata", 0.79, "Reclamação aberta no SAC pendente")
        ]
        cursor.executemany('''
            INSERT INTO socios_churn (id, plano, risco, fator_critico)
            VALUES (?, ?, ?, ?)
        ''', dados_iniciais)
        conn.commit()
        
    conn.close()

inicializar_banco()

@app.get("/")
async def carregar_dashboard():
    return FileResponse(os.path.join("templates", "index.html"))

@app.get("/api/churn")
async def obter_dados_churn():
    conn = sqlite3.connect(NOME_BANCO)
    conn.row_factory = sqlite3.Row 
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM socios_churn")
    linhas = cursor.fetchall()
    
    dados_formatados = [dict(linha) for linha in linhas]
    
    conn.close()
    return {"status": "sucesso", "dados": dados_formatados}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
