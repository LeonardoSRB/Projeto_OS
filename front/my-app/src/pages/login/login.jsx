import React, {useState} from "react";
import "./login.css"
import axios from 'axios'
import { useNavigate } from 'react-router-dom'

export default function Login() {
    const [user, setUser] = useState('')
    const [password, setPassword] = useState('')
    const navigate = useNavigate()

    const logar = async () => {
        console.log("Usuário: ", user)
        console.log("Senha: ", password)
        
        try {
            const response = await axios.post('http://127.0.0.1:8000/api/token/', 
                {
                    username: user,
                    password: password
                } 

            )
            console.log("Token Login", response.data.access)
            localStorage.setItem('token', response.data.access)
            navigate('/Home')
        } catch (error) {
            console.error(error)
        }
    }

    return(
        <div className="Container_login">
            <section className="section_login">
                <p>Usuário:</p>
                <input 
                placeholder="Insira seu nome de usuário"
                type="text"
                value={user}
                onChange={(e) => { setUser(e.target.value)}}/>
                <p>Senha: </p>
                <input
                placeholder="Insira sua senha"
                type="password"
                value={password}
                onChange={(e) => { setPassword(e.target.value)}}/>

                <button className="btn" onClick={logar}>
                    Entrar
                </button>
            </section>
        </div>
    )
}