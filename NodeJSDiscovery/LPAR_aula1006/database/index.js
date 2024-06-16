import Tarefa from "../models/tarefa.js"
import Usuario from "../models/usuario.js"

export const db = {
    tarefas: [
        new Tarefa(1,"Tarefa 1"),
        new Tarefa(2, "Tarefa 2")
    ],
    usuarios: [
        new Usuario(1,"Nome do user","email@email.com"),
        new Usuario(2,"Nome do user 2", "email2@email.com")
    ]
}

export function getAll(){
    return db.usuarios
}

export function findByKey(key){
    return db.usuarios[key]
}