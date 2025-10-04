import streamlit as st

def hashira():
    name = st.text_input('Escreva o nome de um Hashira: ')
    return name
st.title('Hashira App')

hashiras = [
    'Tomioka', 'Obanai', 'Gyomei', 'Mitsuri', 'Rengoku',
    'Sanemi', 'Shinobu', 'Tokito', 'Uzui', 'Yoriichi'
]

st.write("Escolha um Hashira entre:", ", ".join(hashiras))

st.subheader('Informe o nome do Hashira abaixo:')

name = hashira()
submit = st.button("Enviar dados")

if submit:
    if name == 'Tomioka':
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image('Hashiras/tomioka.png', width=200)
        with col2:
            st.write(f"**{name}, Hashira da água!**")
            st.write(
                "💧 Curiosidade: Tomioka Giyu é conhecido por sua extrema calma e disciplina, "
                "mesmo nas batalhas mais intensas. Ele é incrivelmente leal e protetor com amigos, "
                "mas mantém uma postura séria na maior parte do tempo. Sua técnica de respiração da água "
                "é considerada uma das mais eficientes e elegantes entre os Hashiras."
            )
    elif name == 'Obanai':
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image('Hashiras/obanai.png', width=200)
        with col2:
            st.write(f"**{name}, Hashira da serpente!**")
            st.write(
                "🐍 Curiosidade: Obanai Iguro é extremamente rigoroso e segue um código de conduta muito rígido. "
                "Ele é famoso por sua lealdade inabalável ao Corpo de Caçadores de Demônios e por "
                "manter sempre sua expressão séria, escondendo emoções profundas. Sua espada e técnicas "
                "de respiração da serpente são altamente precisas e letais."
            )
    elif name == 'Gyomei':
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image('Hashiras/gyomei.png', width=200)
        with col2:
            st.write(f"**{name}, Hashira da pedra!**")
            st.write(
                "🪨 Curiosidade: Gyomei Himejima é considerado o Hashira mais forte fisicamente. "
                "Apesar de ser cego, sua percepção aguçada e força descomunal fazem dele um adversário quase imbatível. "
                "Ele possui uma personalidade extremamente compassiva e protetora, especialmente com os novatos."
            )
    elif name == 'Mitsuri':
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image('Hashiras/mitsuri.png', width=200)
        with col2:
            st.write(f"**{name}, Hashira do amor!**")
            st.write(
                "💖 Curiosidade: Mitsuri Kanroji é famosa por sua força surpreendente e agilidade incrível, "
                "que contrasta com sua aparência delicada. Ela é extremamente emocional e demonstra grande empatia "
                "por todos, tornando-a muito querida entre os companheiros. Sua respiração do amor é única e poderosa."
            )
    elif name == 'Rengoku':
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image('Hashiras/rengoku.png', width=200)
        with col2:
            st.write(f"**{name}, Hashira das chamas!**")
            st.write(
                "🔥 Curiosidade: Kyojuro Rengoku é conhecido por seu entusiasmo contagiante e espírito indomável. "
                "Ele valoriza a honra acima de tudo e luta com coragem e determinação, mesmo em situações perigosas. "
                "Sua respiração das chamas combina força bruta e técnicas impressionantes de ataque."
            )
    elif name == 'Sanemi':
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image('Hashiras/sanemi.png', width=200)
        with col2:
            st.write(f"**{name}, Hashira do vento!**")
            st.write(
                "🌪️ Curiosidade: Sanemi Shinazugawa é conhecido por seu temperamento explosivo e personalidade agressiva. "
                "Apesar disso, ele é extremamente protetor com seus companheiros e tem um forte senso de justiça. "
                "Sua respiração do vento permite ataques rápidos e precisos, tornando-o um oponente formidável."
            )
    elif name == 'Shinobu':
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image('Hashiras/shinobu.png', width=200)
        with col2:
            st.write(f"**{name}, Hashira do inseto!**")
            st.write(
                "🦋 Curiosidade: Shinobu Kocho é pequena e delicada, mas extremamente letal. "
                "Ela não possui força suficiente para decapitar demônios, então utiliza venenos altamente eficazes. "
                "Inteligente e estratégica, sempre mantém um sorriso calmo mesmo em situações críticas."
            )
    elif name == 'Tokito':
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image('Hashiras/tokito.png', width=200)
        with col2:
            st.write(f"**{name}, Hashira da névoa!**")
            st.write(
                "🌫️ Curiosidade: Muichiro Tokito é incrivelmente talentoso e prodígio, conseguindo dominar a respiração da névoa "
                "em pouquíssimo tempo. Apesar de jovem e distraído, sua habilidade em batalha é impressionante, "
                "fazendo dele um dos Hashiras mais promissores."
            )
    elif name == 'Uzui':
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image('Hashiras/uzui.png', width=200)
        with col2:
            st.write(f"**{name}, Hashira do som!**")
            st.write(
                "🎶 Curiosidade: Tengen Uzui é extravagante, confiante e adora a vida com intensidade. "
                "Além disso, é extremamente habilidoso em combate, usando técnicas baseadas em sons e movimentos rápidos. "
                "Sua visão estratégica e força física impressionante fazem dele um Hashira único."
            )
    elif name == 'Yoriichi':
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image('Hashiras/yoriichi.gif')
        with col2:
            st.write(f"**{name}, o lendário Hashira!**")
            st.write(
                "⚡ Curiosidade: Yoriichi Tsugikuni é considerado o caçador de demônios mais poderoso que já existiu. "
                "Sua técnica de respiração do sol é a base de todas as outras respirações, e sua habilidade supera qualquer outro Hashira. "
                "Ele é calmo, sábio e extremamente focado, sendo uma lenda viva entre caçadores."
            )
    else:
        st.write("Epa, esse Hashira não existe infelizmente...")
