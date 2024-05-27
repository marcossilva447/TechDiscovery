// criando a classe Estudante

class Estudante{
    constructor(nome, email, RA, curso, disciplinas){
        this.nome = nome
        this.email = email
        this.RA = RA
        this.curso = curso
        this.disciplinas = disciplinas
    }
}

// criando os métodos da classe Estudante

function primeiraDisciplina(){
    disciplinaPrimeira = disciplinas[0]
    return disciplinaPrimeira    
}

function ultimaDisciplina(){
    disciplinaUltima = disciplinas[disciplinas.length - 1]
    return disciplinaUltima
}

function cadastrarEsudante(nome, email, RA, curso, disciplinas){
    return {
        nome,
        email,
        RA,
        curso,
        disciplinas
    }
}

// criando um objeto estudante

const estudante1 = new Estudante('João', 'joaocomj@gmail.com', '123456', 'Engenharia', ['Cálculo', 'Física', 'Química'])

const estudante2 = new Estudante('Maria', 'mariacomh@gmail.com', '654321', 'Medicina', ['Anatomia', 'Fisiologia', 'Bioquímica'])

console.log(estudante1)
console.log(estudante2)
