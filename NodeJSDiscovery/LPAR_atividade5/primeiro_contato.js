/* Objetivo: Receber o nome de uma pessoa e exibir uma mensagem de boas-vindas*/
const prompt = require('prompt-sync')()

const name = prompt('Digite o nome de uma pessoa ')

console.log(`Olha, ${name} é um nome muito bonito!`)

/* Saída esperada: Olha, [nome] é um nome muito bonito! */

/*Utilizando o padrão "import" do ES6, o código ficaria assim:

import PromptSync from 'prompt-sync'

const prompt = PromptSync()

const name = prompt('Digite o nome de uma pessoa ')

console.log(`Olha, ${name} é um nome muito bonito!`)
*/
