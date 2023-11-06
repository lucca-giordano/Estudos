import React, {useState, useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import styled from 'styled-components';
import Logo from '../assets/logo.svg';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import axios from 'axios';
import { registerRoute } from '../utils/APIRoutes';

function Register() {
    const navigate = useNavigate();
    const [values, setValues] = useState({
        username: "",
        email: "",
        password: "",
        confirmPassword: "",
    });

    const toastOptions = {
        position: "bottom-right",
        autoClose: 8000,
        pauseOnHover: true,
        draggable: true,
        theme: "dark",
    };

    const handleSubmit = async (event) => {
        event.preventDefault();
        if(handleValidation()){
            const {password, confirmPassword, username, email} = values;
            const {data} = await axios.post(registerRoute,
                {username, 
                email,
                password,
                confirmPassword
            });
            if(data.status===false){
                toast.error(data.msg, toastOptions);
            }
            if(data.status===true){
                localStorage.setItem('chat-app-user', JSON.stringify(data.user));
            }
            navigate("/");
        }
    };

    const handleValidation = () => {
        const {password, confirmPassword, username, email} = values;
        if(password!==confirmPassword){
            toast.error("Senhas não coincidem", toastOptions);
            return false;
        }
        
        else if(username.length < 3){
            toast.error("Nome de usuário deve ter pelo menos 3 caracteres", toastOptions);
            return false;
        }
        else if(password.length < 8){
            toast.error("Sua senha deve ter pelo menos 8 caracteres", toastOptions);
            return false;
        }
        else if(email === ""){
            toast.error("Email inválido", toastOptions);
            return false;
        }
        else{
            return true;
        }
        
    }

    const handleChange = (event) => {
        setValues({...values, [event.target.name]: event.target.value});
    };
  return(
    <>
    <FormContainer>
        <form onSubmit={(event)=>handleSubmit(event)}>
            <div className="brand">
                <img src={Logo} alt="Logo" />
                <h1>Snappy</h1>
            </div>
            <input type="text" placeholder ="Nome de usuário" name="username" onChange={e=>handleChange(e)}/>
            <input type="email" placeholder ="Email" name="email" onChange={e=>handleChange(e)}/>
            <input type="password" placeholder ="Senha" name="password" onChange={e=>handleChange(e)}/>
            <input type="password" placeholder ="Confirme a senha" name="confirmPassword" onChange={e=>handleChange(e)}/>
            <button type="submit">Criar Conta</button>
            <span>
                Já possui uma conta? <Link to="/login">Entre aqui!</Link>
                </span>
        </form>
    </FormContainer>
    <ToastContainer />
    </>
  )
};

const FormContainer = styled.div`
height: 100vh;
width: 100vw;
display: flex;
flex-direction: column;
justify-content: center;
gap: 1rem;
align-items: center;
background-color: #131324;
.brand{
    display: flex;
    align-items: center;
    gap: 1rem;
    justify-content: center;
    img{
        height: 5rem;
    }
    h1{
        color: white;
        text-transform: uppercase;
    }
}
form{
    display: flex;
    flex-direction: column;
    gap: 2rem;
    background-color: #00000076;
    border-radius: 2rem;
    padding: 2rem 5rem;
    input{
        background-color: transparent;
        padding: 1rem;
        border-radius: 0.4rem;
        border: 0.1rem solid #4e0eff;
        color: white;
        widht: 100%;
        font-size: 1rem;
        &:focus{
            border: 0.1rem solid #997af0;
            outline: none;  
        }
    }
    button{
        background-color: #997af0;
        color: white;
        padding: 1rem 2rem;
        border: none;
        font-weight: bold;
        cursor: pointer;
        border-radius: 0.4rem;
        font-size: 1rem;
        text-transform: uppercase;
        transition: 0.3s;
        &:hover{
            background-color: #4e0eff;
        }
    }
    span{
        color: white;
        text-transform: uppercase;
        a{
            color: 4e0e0ff;
            text-transform: none;
            text-decoration: none;
            font-weight: bold;
            &:hover{
                text-decoration: underline;
            }
        }
    }
}
`;

export default Register;