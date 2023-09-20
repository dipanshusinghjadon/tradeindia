import streamlit as st
import pandas as pd
import time,csv
import requests as rt
# from PIL import Image

# image = Image.open('icon.jpg')

# st.image(image)

def check_urls(uploaded_file):
    df = pd.read_csv(uploaded_file)
    urls =df['URL'].tolist()
    ln= len(urls)
    name = f"tested_{uploaded_file.name}"
    prg = st.progress(0)
    with open(f'./tested/{name}', 'w', newline='') as file:
        with st.empty():
            for index,url in enumerate(urls):

                res = rt.get(url)
                status = res.status_code

                writer = csv.writer(file)
                writer.writerow([url,status])

                cent= (index/ln)
                prg.progress(cent)
            prg.progress(100)
            time.sleep(0.5)
            prg.empty()
            # st.write('Testing Completed')

    with open(f'./tested/{name}') as f:
        st.download_button('Download CSV', f, file_name=f'{name}')

def main():
    st.title("Taesther")
    uploaded_file = st.file_uploader("Choose a File")

    if st.button("Run"):
        check_urls(uploaded_file)

if __name__ == '__main__':
    main()