# SolSys - Sistema Solar em 3D

SolSys é um visualizador interativo do sistema solar em 3D utilizando `matplotlib` e `customtkinter`. Ele permite observar a posição dos planetas em tempo real, simulando suas coordenadas em um gráfico 3D, com a possibilidade de alternar entre uma lista de planetas e uma visualização 3D do sistema solar.

## Funcionalidades

- **Visualização 3D**: Exibe as posições dos planetas do sistema solar em um espaço tridimensional com coordenadas baseadas em seus valores de ascensão reta (RA) e declinação (DEC).
- **Lista de planetas**: Apresenta uma lista interativa de planetas e exibe informações básicas sobre cada um deles.
- **Visualização alternada**: Permite alternar entre a lista de planetas e a visualização 3D clicando em um botão.

## Tecnologias Utilizadas

- **Python 3.x**: Linguagem de programação.
- **Tkinter e CustomTkinter**: Interface gráfica para o usuário (GUI).
- **Matplotlib**: Biblioteca usada para gerar a visualização gráfica 3D.
- **Numpy**: Utilizado para cálculos matemáticos de posições e ângulos.

## Como Funciona

O programa calcula as posições dos planetas com base em suas coordenadas de ascensão reta (RA) e declinação (DEC), convertendo esses valores em coordenadas cartesianas para visualização em 3D.

### Posição dos planetas

Cada planeta tem uma posição baseada nas coordenadas fornecidas:

- **delta**: Distância do planeta ao Sol (ou centro de referência).
- **RA (Ascensão Reta)**: Representa o ângulo de posição ao longo do equador celeste.
- **DEC (Declinação)**: Representa a inclinação angular ao norte ou ao sul do equador celeste.

As coordenadas são convertidas para o gráfico 3D usando funções trigonométricas fornecidas pelo `numpy`, e a visualização é gerada pela biblioteca `matplotlib`.

### Controles

- **Botão "Exibir Visualização 3D"**: Alterna entre a visualização 3D e a ocultação da mesma.
- **Botão "Listar Planetas"**: Exibe uma lista com todos os planetas e seus dados.
- **Botão "Exibir Dados"**: Mostra propriedades básicas do planeta selecionado na lista.

