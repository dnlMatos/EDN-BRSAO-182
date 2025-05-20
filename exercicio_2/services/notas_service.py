from models.aluno import Aluno
from utils.validador import validar_nota

def registrar_notas():
    notas = []
    
    while True:
        entrada = input("Digite a nota do aluno (ou 'fim' para encerrar): ").strip().lower()
        
        if entrada == 'fim':
            break
        
        nota = validar_nota(entrada)
        
        if nota is not None:
            aluno = Aluno(nota)
            notas.append(aluno)
    
    if notas:
        media = sum(aluno.nota for aluno in notas) / len(notas)
        print(f"\nMédia da turma: {media:.2f}")
    else:
        print("\nNenhuma nota registrada.")
 