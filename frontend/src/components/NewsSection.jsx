import React from 'react';
import NewsItem from './NewsItem';

function NewsSection() {
  return (
    <section className="news-section">
      <h2>Últimas Notícias e Artigos</h2>
      <div className="news-container">
        <NewsItem 
          title="Edital Publicado: Concurso para Magistratura"
          text="Fique por dentro de todos os detalhes e prazos do novo concurso para Juiz de Direito. Nossos professores já estão preparando materiais exclusivos."
        />
        <NewsItem 
          title="Como organizar sua rotina de estudos?"
          text="O Prof. Dougras Bastos dá dicas valiosas para você montar um cronograma de estudos eficiente e otimizar seu tempo de preparação."
        />
        <NewsItem 
          title="Mudanças na Legislação: O que impacta os concursos?"
          text="Uma análise completa sobre as recentes alterações legislativas e como elas podem ser cobradas nas próximas provas."
        />
      </div>
    </section>
  );
}

export default NewsSection;