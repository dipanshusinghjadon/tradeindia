import pandas as pd
import matplotlib.pyplot as plt
import requests


def preprod_url(url):
    # try:
    response = requests.get(url)
    return response
        

df = pd.read_csv(r'/home/user01/Downloads/uniq_access_27april2023.2.csv', header=0, nrows=200000)

code_200 = 0
code_404 = 0

print("URL,STATUS_CODE")

for index, url in enumerate(df['URL'][85000:]):
    url = url.replace("'", "")
    try:
        output = preprod_url(url)
    except Exception:
        print(F"{url},Error")
        continue

    print(f"{url},{output.status_code}")
   


# plt.bar(results.index, results.values)
# plt.xlabel('Result')
# plt.ylabel('Count')
# plt.title('URL Test Results')
# plt.show()

