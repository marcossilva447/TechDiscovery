const express = require('express')
const app = express()
const port = 3000

app.get('/alunos', (req, res) => {
    const alunos = [
        { RA: '123456', nome: 'João', email: 'joao@fatec.com' },
        { RA: '654321', nome: 'Maria', email: 'maria@fatec.com' },
        { RA: '987654', nome: 'Pedro', email: 'pedro@fatec.com' }
    ]
    res.json(alunos);
})

app.listen(port, () => {
    console.log(`Servidor rodando em http://localhost:${port}`)
    })

app.listen(3000, () => {
    console.log('Servidor iniciado na porta 3000');
});