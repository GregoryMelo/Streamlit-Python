import streamlit as st
def jedi():
    name = st.text_input("Nome do Jedi:")
    age = st.number_input("Idade do Jedi:", value=0, step=1, min_value=0,  max_value=1500)
    return name, age
st.title("Jedi App")
st.subheader("Por favor, informe seus dados abaixo:")
# Pede o nome e a idade do Jedi usando a função jedi
name, age = jedi()
# Cria uma lista suspensa com as categorias de Jedi
st.write("Selecione a categoria de jedi que você pertence:")
category = st.selectbox("Categoria de Jedi", ("Padawan", "Cavaleiro", "Mestre"))
# Cria um botão para enviar os dados
submit = st.button("Enviar dados")
# Se o botão for pressionado, exibe uma mensagem de confirmação
if submit:
    st.write("Seus dados foram enviados!")
    # Exibe uma mensagem com os dados do Jedi
    st.write("O Jedi", name, "da categoria", category, "tem", age, "anos.")
# Exibe uma imagem de um Jedi na página
st.image("rey.png", width=200)