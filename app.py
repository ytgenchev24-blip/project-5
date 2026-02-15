import streamlit as st
st.title("Анкета за обратна връзка")
st.write("Моля попълнете полетата по-долу")

st.write("Как се казваш")
name = st.text_input("Въведи първото си име")


if name:
  st.write("Добре дошъл ,", name)

answer = st.radio("Интересен ли ти е предмета Изкуствен интелект ?", ("да"/"не"))
if answer == "да":
  st.write("Супер, продължавай да се развиваш")

else:
  st.write("Няма проблем, всеки има право на избор")

answer = st.number_input("От колко време го изучаваш?")
if answer == 1:
  st.write("Имаш още доста да разбереш")

if answer == 2:
  st.write("Учиш го вече втора година значи вече можеш да правиш базови приложения")

if answer == 3:
  st.write("Ти си напреднал")

if answer == 4:
  st.write("Браво можеш да правиш доста неща")
  










