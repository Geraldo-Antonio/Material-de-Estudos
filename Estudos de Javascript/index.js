// Imprimir no console
console.log("Olá, mundo!");

// Váriaveis
let textoNome = "Geraldo";
let idade = 17;
let concorda = false;

// Objetos
let pessoa = {
    nome: "Marcos",
    idade: 18,
    altura: 1.72
};
console.log(pessoa.nome);

// Funções
function alterarNome(nome){
    pessoa.nome = nome;
}

alterarNome("Carlos");
console.log(pessoa.nome);

// Arrays
let lista = [true, "texto", 25];
console.log(lista[2])

// Função com retorno
function multiplicarPorDois(numero){
    return numero*2
}
console.log(multiplicarPorDois(25))