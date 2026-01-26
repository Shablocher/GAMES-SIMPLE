# 🚀 Space War: Ultimate Hero Edition

![Versão](https://img.shields.io/badge/version-2.0.0-blueviolet)
![Tecnologias](https://img.shields.io/badge/tech-HTML5%20|%20JS%20|%20CSS3-informational)
![Estilo](https://img.shields.io/badge/style-Neon%20Retro-ff00ff)

**Space War** é um jogo de combate espacial frenético rodando diretamente no navegador. Com uma estética *Neon Retro*, o jogador deve sobreviver a hordas de inimigos, coletar upgrades e derrotar o grande Boss final para se tornar uma lenda estelar.

---

## 🎮 Funcionalidades

-   **Personalização de Piloto:** Insira seu nome antes de iniciar a missão.
-   **Níveis de Dificuldade:** Escolha entre **Fácil**, **Médio** e **Difícil** (afeta velocidade e vida do Boss).
-   **Sistema de Power-ups:**
    * 💚 **(H) Recuperação:** Restaura 30% do escudo da nave.
    * 💛 **(2X) Tiro Duplo:** Dobra o poder de fogo por 8 segundos.
-   **HUD Dinâmico:** Barras de vida em tempo real para o jogador e para o Boss.
-   **Efeitos Visuais:** Fundo estrelado com efeito *Parallax*, trepidação de tela ao sofrer dano e explosões de partículas na vitória.
-   **Áudio Sintetizado:** Efeitos sonoros gerados via *Web Audio API* (sem necessidade de arquivos externos).

---

## 🕹️ Como Jogar

1.  Abra o arquivo `index.html` em qualquer navegador moderno.
2.  Digite seu nome no campo de identificação.
3.  Escolha a dificuldade desejada.
4.  **Controles:**
    * ⬅️ / ➡️ : Move a nave para a esquerda e direita.
    * ⌨️ **Espaço** : Dispara os canhões laser.

---

## 🛠️ Tecnologias Utilizadas

O projeto foi construído puramente com tecnologias web padrão, sem bibliotecas externas:

* **HTML5 Canvas:** Renderização gráfica de alta performance.
* **JavaScript (ES6+):** Lógica do jogo, física de colisão e gerenciamento de partículas.
* **CSS3:** Estilização da interface (HUD e menus) com fontes futuristas.
* **Web Audio API:** Geração de ondas sonoras em tempo real para tiros e explosões.

---

## 📐 Estrutura do Código

Para garantir que o jogo rode sem travamentos, o código utiliza:
-   **Memory Cleanup:** Remoção automática de projéteis e inimigos fora da tela.
-   **Parallax Background:** Múltiplas camadas de estrelas com velocidades diferentes para criar profundidade.
-   **Collision Engine:** Cálculo preciso de hitboxes com margens de segurança.

---

