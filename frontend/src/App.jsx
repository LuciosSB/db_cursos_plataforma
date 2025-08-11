// frontend/src/App.jsx
import React, { useState, useEffect } from 'react';
import Sidebar from './components/Sidebar';
import Header from './components/Header';
import Hero from './components/Hero';
import NewsSection from './components/NewsSection';

function App() {
  const [isSidebarVisible, setSidebarVisible] = useState(false);
  const [apiMessage, setApiMessage] = useState('Carregando mensagem da API...');

  useEffect(() => {
    fetch('http://localhost:5000/')
      .then(response => response.text())
      .then(data => setApiMessage(data))
      .catch(error => {
        console.error('Erro ao buscar dados da API Flask:', error);
        setApiMessage('Falha ao conectar com o backend.');
      });
  }, []);

  useEffect(() => {
    function handleMouseMove(e) {
      const triggerZone = 15; const sidebarWidth = 280;
      if (e.clientX < triggerZone) { setSidebarVisible(true); } 
      else if (e.clientX > sidebarWidth) { setSidebarVisible(false); }
    }
    document.addEventListener('mousemove', handleMouseMove);
    return () => document.removeEventListener('mousemove', handleMouseMove);
  }, []);

  return (
    <div className={isSidebarVisible ? 'sidebar-visible' : ''}>
      <Sidebar />
      <div className="main-content-wrapper">
        <Header />
        <main>
          <Hero />
          <NewsSection />
        </main>
      </div>
    </div>
  );
}

export default App;