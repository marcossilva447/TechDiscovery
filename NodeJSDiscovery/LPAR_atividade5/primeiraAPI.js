const express = require('express')
const app = express()
const port = 3000

app.get('/', (req, res) => {
    res.send('Olá, mundo!')
    })

app.listen(port, () => {
    console.log(`Servidor rodando em http://localhost:${port}`)
    })

/*podemos atualizar nossa importação, para isso precisamos adicionar um ajuste no packege.json e alterar a forma de carregar o express:

import express from 'express'
const app = express()
const port = 3000

no package.json, adicione o seguinte trecho:
{
    "name": "primeiraAPI",
    "version": "1.0.0",
    "description": "Primeira API com Node.js",
    "main": "primeiraAPI.js",
    "type": "module",}
    */