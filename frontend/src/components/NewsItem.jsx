import React from 'react';

function NewsItem({ title, text }) {
  return (
    <article className="news-item">
      <h3>{title}</h3>
      <p>{text}</p>
      <a href="#" className="read-more">Leia mais</a>
    </article>
  );
}

export default NewsItem;