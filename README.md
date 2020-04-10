# APS-Python-2sem

This is a python program developed on the second half of the first year of computer science at UNIP. Its main goal is to develop a python program which will help on some part of waste recycling process.

My group and I have chosen to develop a program that helps people who has interested on learning more about recycling, providing them information about which material can be recycled as well as the closest place where they can take those materials. 

Feel free to read and contribute with this code :D


Disclaimer: Since this code was develop to by avaliated be professors at UNIP on Brazil, all the code and comentaries will be on Brazilian-Portugues.

Olá,

Segue abaixo algumas instruções e recomendações para instalação e utilização desse programa:

- Sugerimos, pelo motivos abaixo que você uso esse codigo em um ambiente virtual, apesar de NÃO SER NECESSARIO.

- É necessario a utilização do Python versão 3. Sugerimos a versão 3.7 ou superior.

- É fundamental para o funcionamento do programa a instalação das bibliotecas utilizadas, explicadas abaixo.

- Você pode utilizar esse programa atraves de linha de comando via seu CMD/Prompt, ao executar o interface_comando.py (para instruções de como usa-lo, rode interface_comando.py -h). Ou via interface visual ao rodar o flask_blog.py (localizado na pasta GUI) em seu CMD/Prompt e acessar o link: localhost:5000 em seu browser.

- Para instalar todas as bibliotecas de um jeito mais facil e rápido vá, através do seu CMD/Prompt, na pasta onde esse projeto esta localizado e rode o comando: pip install -r requirements.txt

- O código faz uso de duas bibliotecas que não são padrões do Python. Uma delas se chama haversine, e como o nome sugere, ele implementa a formula de Haversine (responsável pelo calculo da distancia entre dois pontos geograficos), ela é fundamental para o funcionamento do programa e você pode instala-la através do comando 'pip install haversine' ou via o requirements.txt, mais informações sobre ela no link(). A outra biblioteca só é necessaria caso você deseje utilizar a parte visual do código, ela se chama flask, ela permite iniciar um pequeno web server local, para tal você precisa rodar o arquivo python flask_blog.py via CMD/Prompt, e acessar o link: localhost:5000 em seu browser, ao fazer isso deve ser possivel visualizar um página web que terá todas as funções presentes via comandline so que mais intutivas.
