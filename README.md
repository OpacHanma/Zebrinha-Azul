Zebrinha Azul - Sistema de Integração e Análise de Dados de Clima e Tráfego

Descrição
Bem-vindo ao Zebrinha Azul! Esta é uma solução inovadora desenvolvida para integrar, processar e analisar dados de clima e tráfego. Este projeto foi criado como parte de um desafio técnico para a startup Zebrinha Azul, visando otimizar operações logísticas e fornecer relatórios detalhados para nossos clientes.

Funcionalidades
Extração de dados de clima e tráfego de APIs externas.
Limpeza e transformação dos dados para uma análise precisa.
Armazenamento seguro dos dados em um banco de dados SQL.
Visualização interativa e intuitiva dos dados.
Requisitos
Para rodar esta aplicação, você precisará do seguinte:

Python 3.10 ou superior
Bibliotecas: SQLAlchemy, Pandas, Requests, Pytest
Configuração
Siga estes passos para configurar o projeto:

1. Clone o repositório
Primeiro, clone o repositório para o seu ambiente local:

bash
Copiar código
git clone https://github.com/seu-usuario/zebrinha-azul.git
cd zebrinha-azul
2. Crie e ative um ambiente virtual
No Windows, utilize os seguintes comandos:

bash
Copiar código
python -m venv venv
venv\Scripts\activate
3. Instale as dependências
Certifique-se de que você tenha um arquivo requirements.txt com o seguinte conteúdo:

txt
Copiar código
requests
pandas
SQLAlchemy
matplotlib
dash
python-dotenv
Instale as dependências com o comando:

bash
Copiar código
pip install -r requirements.txt
Extração de Dados
O arquivo data_extraction.py contém as funções necessárias para extrair dados das APIs do OpenWeatherMap e do Google Maps Directions.

Uso
Adicione suas chaves de API no arquivo de configuração.
Execute o script para iniciar a extração dos dados:
bash
Copiar código
python data_extraction.py
Limpeza e Transformação
O arquivo data_transformation.py cuida da limpeza e transformação dos dados extraídos.

Funções de Limpeza
clean_weather_data: Limpa e transforma os dados de clima.
clean_traffic_data: Limpa e transforma os dados de tráfego.
Uso
Essas funções são chamadas automaticamente após a extração dos dados em data_extraction.py.

Modelagem de Dados
Definição das Tabelas
O esquema do banco de dados é definido no arquivo data_model.py usando SQLAlchemy. Existem duas tabelas principais:

weather_data: Armazena informações sobre o clima, incluindo localização, temperatura, umidade e data/hora.
traffic_data: Armazena informações sobre o tráfego, incluindo origem, destino, duração em segundos, distância em metros e data/hora.
Carregamento de Dados
O arquivo data_loading.py contém o código para carregar os dados extraídos e transformados nas tabelas do banco de dados. Certifique-se de substituir 'YOUR_WEATHER_API_KEY' e 'YOUR_TRAFFIC_API_KEY' pelas suas próprias chaves de API.

Para carregar os dados no banco de dados, execute:

bash
Copiar código
python data_loading.py
Visualização de Dados
Painel Interativo
O arquivo data_visualization.py utiliza a biblioteca Dash para criar um painel interativo que visualiza os dados de clima e tráfego.

Uso
Certifique-se de que as dependências estejam instaladas:

bash
Copiar código
pip install dash
Execute o script de visualização:

bash
Copiar código
python app.py
Abra o navegador e acesse http://127.0.0.1:8050/ para ver os gráficos.

Visualizações
Clima
Gráfico de linha mostrando a temperatura ao longo do tempo.
Tráfego
Gráfico de dispersão mostrando a relação entre duração e distância.
Essas visualizações permitem explorar os dados coletados de maneira intuitiva e informativa.

Conclusão
Este projeto demonstra como é possível extrair, transformar, carregar e visualizar dados de clima e tráfego utilizando ferramentas modernas e práticas de desenvolvimento. A estrutura modular do código facilita a manutenção e a escalabilidade, atendendo às necessidades específicas da Zebrinha Azul.

