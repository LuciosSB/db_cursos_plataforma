import React from 'react';

function Header() {
  return (
    <header className="main-header">
      <div className="header-container">
        <div className="logo">
          <a href="#">DB Cursos e Concursos</a>
        </div>
        <nav className="main-nav">
          <ul>
            <li><a href="#">Início</a></li>
            <li className="dropdown">
              <a href="#">Institucional</a>
              <ul className="dropdown-menu">
                <li><a href="#">Nossa História</a></li>
                <li><a href="#">Corpo Docente</a></li>
                <li><a href="#">Contato</a></li>
              </ul>
            </li>
            <li><a href="#">Notícias</a></li>
            <li><a href="#">Portal do Aluno</a></li>
          </ul>
        </nav>
        <div className="header-action">
          <a href="#" className="cta-button">FAZER MATRÍCULA</a>
        </div>
      </div>
    </header>
  );
}

export default Header;