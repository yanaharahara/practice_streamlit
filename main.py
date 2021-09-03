import streamlit as st
import time
st.title('Streamlit 超入門')

st.write('プログレスバーの表示')

'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)


left_column,right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')
#option = st.text_input('趣味教えて')
#condition = st.slider('あなたの今の調子は？',0,100,50)

#'あなたの趣味は',option
#'コンディション:',condition

#if st.checkbox('Show Image'):
#    img = Image.open('visualization.png')
#    st.image(img,caption='Kohei Imanishi',use_column_width=True)

#df = pd.DataFrame(
#    np.random.rand(100,2)/[50,50] + [35.69,139.70],
#    columns=['lat','lon']
#)

#st.table(df.style.highlight_max(axis=0))#dataframeのほうが細かい設定できる
#st.map(df)


"""
# 章
## 節
### 項

```
import streamlit as st
import numpy as np
import pandas as pd
```
"""

##質問で混雑度を聞く
##経度などを用いてmapを作成
##質問の回答によってif文の条件分岐をする

##複数のQ＆Aはexpander
