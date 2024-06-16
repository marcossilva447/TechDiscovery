import express from "express"
import { getAll, findByKey } from "./database/index.js"

const app = express()
const port = 3000
app.use(express.json())

app.get('/tarefas',(req,res) =>{
    const tarefas = getAll('tarefas')
    res.json(tarefas)
})

app.get('/usuarios',(req,res)=>{
    const usuarios = getAll('usuarios')
    res.json(usuarios)
})

app.get('/primeira-tarefa',(req,res)=>{
    const tarefa = findByKey(0)
    res.json(tarefa)
})

app.listen(port, () => {
    console.log(`Servidor executando em 
    http://localhost:${port}`)
})