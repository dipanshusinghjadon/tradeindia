import pandas as pd
import matplotlib.pyplot as plt
import requests


def dev2fe_url(url):
    # try:
    response = requests.get(url)
    return response
        

df = pd.read_csv(r'/home/user01/Downloads/data.csv')
# print(df)

code_200 = 0
code_404 = 0

print("URL,STATUS_CODE")

# for index, url in enumerate(df['URL'][85000:]):
for index, url in enumerate(df['URL']):
    url = url.replace("'", "")
    try:
        output = dev2fe_url(url)
    except Exception:
        print(F"{url},Error")
        continue

    print(f"{url},{output.status_code}")
   


# plt.bar(results.index, results.values)
# plt.xlabel('Result')
# plt.ylabel('Count')
# plt.title('URL Test Results')
# plt.show()

