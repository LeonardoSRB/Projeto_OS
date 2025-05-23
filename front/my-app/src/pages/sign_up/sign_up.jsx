import React, { useState } from 'react';
import axios from 'axios';
import "sign_up.css";
import { useNavigate } from 'react-router-dom'
import "./sign_up.css"

const Register = () => {
    const [usuario, setUsuario] = useState('');
    const[email, setEmail] = useState('');
    const [senha, setSenha] = useState('');
    const [mensagem, setMensagem] = useState('');
    const navigate = useNavigate()

    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            const response = await axios.post('http://127.0.0.1:8000/api/create_user/', 
                {
                    username: usuario,
                    email: email,
                    password: senha
                }
            );

            console.log('Usuário criado com sucesso:', response.data);
            setMensagem('Usuário criado com sucesso!')
        } catch (error) {
            console.error('Erro ao criar usuário:', error);
            setMensagem('Erro ao criar usuário, tente novamente.')
        }
    };
    return(
        <div className='container_sign_up'>
            <form className='form' onSubmit={handleSubmit}>
                <div>
                    <p>Usuário:</p>
                    <input
                    type='user'
                    value={usuario}
                    onChange={(e) => setUsuario(e.target.value)}
                    required
                    placeholder='Insira um nome de usuário'/>
                </div>
                <div>
                    <p>Email:</p>
                    <input
                    type='email'
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    required
                    placeholder='Insira o seu email'/>
                </div>
                <div>
                    <p>Senha:</p>
                    <input
                    type='password'
                    value={senha}
                    onChange={(e) => setSenha(e.target.value)}
                    required
                    placeholder='Insira uma senha'/>
                </div>
                <button className='btn' type='submit' onClick={navigate('/login')}>Cadastrar</button>
            </form>
            {mensagem && <p>{mensagem}</p>}
        </div>
    );
};

export default Register