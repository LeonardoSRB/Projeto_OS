import React from "react";
import "./header.css";
import { FaRegCircleUser } from "react-icons/fa6";
export default function header() {
    return (
        <div className="navbar">
            <div className="logo">
                <img src="/assets/logo_senai.png" alt="logo_senai"></img>
            </div>
            <div className="nav">
                <a>Ordem de serviço</a>
                <a>Funcionários</a>
                <FaRegCircleUser />
            </div>
        </div>
    )
}