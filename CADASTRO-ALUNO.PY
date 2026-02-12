import sqlite3

# 1. Conecta ao banco de dados (se não existir, ele cria)
conexao = sqlite3.connect('escola.db')
cursor = conexao.cursor()

# 2. Cria uma tabela de alunos
cursor.execute('''
    CREATE TABLE IF NOT EXISTS alunos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        nota REAL
    )
''')

# 3. Inserindo um dado para teste
nome_aluno = input("Digite o nome do aluno: ")
nota_aluno = float(input("Digite a nota do aluno: "))

cursor.execute("INSERT INTO alunos (nome, nota) VALUES (?, ?)", (nome_aluno, nota_aluno))

# 4. Salva e fecha
conexao.commit()
print("Dado salvo no SQL com sucesso!")
conexao.close()
