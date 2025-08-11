import React from 'react';

function Sidebar() {
  return (
    <aside id="left-sidebar" className="sidebar">
      <div className="sidebar-content">
        <h3>Menu Rápido</h3>
        <p>Este é um texto de teste para preencher a sidebar. Aqui você pode colocar links rápidos, informações do usuário, ou qualquer outro conteúdo relevante.</p>
        <ul>
          <li><a href="#">Meu Perfil</a></li>
          <li><a href="#">Meus Cursos</a></li>
          <li><a href="#">Configurações</a></li>
          <li><a href="#">Sair</a></li>
        </ul>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam eget sapien sapien.</p>
      </div>
    </aside>
  );
}

export default Sidebar;