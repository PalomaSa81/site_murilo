import streamlit as st
import webbrowser

st.set_page_config(layout="wide")

def create_whatsapp_button(button_text="Entre em contato", icon="whatsapp", key=None):
  whatsapp_link = "https://api.whatsapp.com/send?phone=+5521967519219&text=Olá,%20quero%2ar%20entrar%20em%20contato!"
  if not key:
      key = f"whatsapp_button_{button_text}"  # Gerar key automaticamente se não for fornecida
  return st.button(button_text, on_click=lambda: webbrowser.open_new_tab(whatsapp_link), type="primary", key=key)

instagram_link = "https://www.instagram.com"
maps_link = "www.google.com.br/maps/place/Pra%C3%A7a+Arariboia/@-22.8940208,-43.1271628,17z/data=!3m1!4b1!4m6!3m5!1s0x9983c51bb87373:0xdfc89cabc774c121!8m2!3d-22.8940258!4d-43.1245879!16s%2Fg%2F113qblvp1?entry=ttu&g_ep=EgoyMDI0MTAxNi4wIKXMDSoASAFQAw%3D%3D"
email = "nomesobrenome@email.com"
col1, col2 = st.columns([1, 3])

# Adicionando conteúdo à primeira coluna
with col1:
    st.image("foto_perfil.png", width=275)
   # create_whatsapp_button("Enviar mensagem", key="duvidas_whatsapp")
    #if st.button("Consultório"):
        # webbrowser.open_new_tab(maps_link)
   # if st.button("Instagram"):
        # webbrowser.open_new_tab(instagram_link)

with col2:
    st.title('Nutricionista Murilo Sobrenome')
    #st.write('Este é o conteúdo da segunda coluna.')
    tab1, tab2, tab3 = st.tabs(["Sobre", "Serviços", "Contato"])

with tab1:
    st.header("Sou apaixonado por ajudar pessoas a alcançarem seus objetivos de saúde e bem-estar.")
    st.write("""   Acredito que uma alimentação equilibrada e personalizada é a chave para uma vida mais saudável e feliz.
Com tantos anos de experiência, me dedico a criar planos alimentares que se adaptam ao seu estilo de vida e necessidades individuais. 
Através de uma abordagem humanizada e científica, auxilio meus pacientes a:""")

    st.write("""Perder peso de forma saudável e sustentável;
          Ganhar massa muscular e melhorar o desempenho físico;
          Controlar doenças crônicas como diabetes e hipertensão;
          Aumentar a energia e o bem-estar geral.""")
             
    st.write("Se você busca uma transformação duradoura e está pronto para investir na sua saúde, me chame no WhatsApp e agende sua consulta!")

   # create_whatsapp_button("Entrar em contato pelo WhatsApp", key="Entrar em contato")   

with tab2:
    st.header("Consultoria Nutricional Individualizada: Desenvolva um plano alimentar personalizado para alcançar seus objetivos de forma saudável e sustentável.")
    st.write(""" 
             
1. Acompanhamento Nutricional Online:             
Tenha acesso a um profissional de nutrição por meio de consultas online, com acompanhamento personalizado e prático.                        
2. Planos Alimentares Específicos:       
Receba um plano alimentar adequado para suas necessidades, como perda de peso, ganho de massa muscular, controle de doenças crônicas ou alimentação vegetariana.             
3. Análise de Exames:              
Entenda seus exames e como eles se relacionam com sua saúde e alimentação.             
4. Orientação Nutricional para Atletas:             
Melhore seu desempenho esportivo com uma alimentação adequada e personalizada.             
5. Palestras e Workshops:              
Participe de eventos e aprenda mais sobre alimentação saudável e nutrição.""")
    #create_whatsapp_button("Entrar em contato pelo WhatsApp", key="fale já")
with tab3:
    st.header("Me ligue ou envie uma mensagem para o número:")
    st.write("Telefone: 21912345678 (WhatsApp)")
    #create_whatsapp_button("Entrar em contato pelo WhatsApp", key="fale agora")

    st.header("Se preferir envie um e-mail para:")
    st.write("nomesobrenome@email.com")
    #st.text(email)
    #if st.button("Enviar e-mail agora"):
         #webbrowser.open_new_tab(email)

    st.header("Atendo presencialmente no endereço:")
    st.write("Rua tal, número tal/complemento tal Bairro tal. Cidade Tal. Referência tal.")
    #if st.button("Veja nossa localização"):
         #webbrowser.open_new_tab(maps_link)

    st.header("Me siga no Instagram")

    #if st.button("Acesse nosso Instagram"):
         #webbrowser.open_new_tab(instagram_link)

    






