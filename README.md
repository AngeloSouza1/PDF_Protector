# ProtetorPDF

**ProtetorPDF** é um projeto desenvolvido em **Python** utilizando o framework **Flask**. Ele tem como objetivo permitir que usuários registrem o **CPF** diretamente em arquivos PDF selecionados, garantindo personalização e identificação do documento de forma simples e eficiente.

---

## Funcionalidades
- Upload de arquivos PDF.
- Registro do CPF no arquivo PDF enviado.
- Download do arquivo PDF atualizado com o CPF inserido.

---

## Tecnologias Utilizadas
- **Python**: Linguagem principal do projeto.
- **Flask**: Framework web utilizado para construção da aplicação.
- **PyPDF2**: Biblioteca para manipulação de PDFs.
- **HTML/CSS**: Interface básica para interação com o usuário.

---

## Requisitos
Certifique-se de ter os seguintes itens instalados no seu ambiente:
- Python 3.8 ou superior
- Pip (gerenciador de pacotes do Python)

---

## Instalação e Execução
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/protetorpdf.git
   cd protetorpdf
   ```

2. Crie um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate    # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Inicie o servidor local:
   ```bash
   flask run
   ```

5. Acesse a aplicação em: [http://localhost:5000](http://localhost:5000)
Video Demonstrativo


https://github.com/user-attachments/assets/7e5b94c5-04f0-49bb-9b66-68afcfaf0c73


---

## Como Usar
1. Faça o upload de um arquivo PDF.
2. Insira o CPF desejado no campo correspondente.
3. Baixe o arquivo atualizado com o CPF registrado.

---

## Estrutura do Projeto
- **app.py**: Arquivo principal da aplicação Flask.
- **templates/**: Arquivos HTML para as views da aplicação.
- **static/**: Arquivos estáticos como CSS e imagens.

---

## Contribuições
Contribuições são bem-vindas! Para colaborar:
1. Faça um fork do projeto.
2. Crie uma branch para sua feature ou correção:
   ```bash
   git checkout -b minha-feature
   ```
3. Envie suas modificações:
   ```bash
   git commit -m "Minha nova feature"
   git push origin minha-feature
   ```
4. Abra um Pull Request.

---

## Licença
Este projeto está licenciado sob a [MIT License](LICENSE).

---

## Autor
**Angelo Souza**  
[LinkedIn](https://linkedin.com/in/seu-perfil)  
[GitHub](https://github.com/seu-usuario)

