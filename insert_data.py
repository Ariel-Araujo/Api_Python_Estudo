import sqlite3

empregados = [
                {'nome': 'Carlos', 'cargo': 'Analista', 'salario': 5000},
                {'nome': 'Joao', 'cargo': 'Analista', 'salario': 4000},
                {'nome': 'Maria', 'cargo': 'Desenvolvedor', 'salario': 5000},
             ]

conn = sqlite3.connect('enterprise.db')

cursor = conn.cursor()

for empregado in empregados:
    cursor.execute("""
        INSERT INTO empregados (nome, cargo, salario)
        VALUES(?,?,?)
    """, (empregado['nome'], empregado['cargo'], empregado['salario']))

print("Dados inseridos com sucesso!")

conn.commit()
conn.close()