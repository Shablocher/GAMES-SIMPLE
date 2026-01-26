# 🚀 Space War: Boss Strike

Um simulador de combate espacial estilo arcade com foco em progressão, desafios aleatórios e uma batalha final épica. Desenvolvido com **Python** no backend para orquestração e **JavaScript (Canvas API)** no frontend para alto desempenho gráfico.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** [Python 3.x](https://www.python.org/)
* **Servidor Web:** [Flask](https://flask.palletsprojects.com/)
* **Interface:** HTML5 Canvas & CSS3
* **Áudio:** Web Audio API (Sons sintetizados em tempo real via código)

---

## 🎮 Funcionalidades Principais

* **Sistema de Combate:** Nave com disparos laser e tempo de recarga (cooldown) para evitar spam.
* **Inimigos Aleatórios:** Geração infinita de meteoros e monstros espaciais com velocidades dinâmicas.
* **Sistema de Vida e Dano:** Escudo de energia (100%) que diminui ao colidir com inimigos ou ser atingido pelo Boss.
* **Boss Final:** Ativado ao atingir **500 pontos**. O Boss possui:
    * Barra de vida dedicada.
    * Movimentação lateral inteligente.
    * Ataques aleatórios com projéteis vermelhos de alto dano.
* **Efeitos Especiais:** * Sistema de partículas para explosões coloridas.
    * *Screen Shake* (vibração da tela) ao receber dano.
    * Sons de disparos e explosões.
* **Tela de Vitória:** Uma tela final personalizada com som de fanfarra e resumo de score após derrotar o Boss.

## 💡 Dicas de Desenvolvimento (Futuro)
**[ ] Adicionar Power-ups (tiro duplo, escudo extra).**

**[ ] Implementar banco de dados SQLite para salvar o Ranking Global.**

**[ ] Adicionar diferentes níveis de dificuldade.**

**[ ] Trocar os blocos coloridos por Sprites (imagens .png) de naves reais.**
