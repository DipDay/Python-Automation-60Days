import requests
import pandas as pd

url = "https://jsonplaceholder.typicode.com/users"
output_path = "E:\\Code\\Python-Automation-60Days\\day34\\users_report.xlsx"

try:
    response = requests.get(url, timeout=15)
    response = requests.get(url)
    response.raise_for_status()
    users = response.json()

    # print(type(users))
    # print(len(users))

    user_data = []

    for user in users:
        user_data.append({
            "Name": user["name"],
            "Email": user["email"],
            "Phone": user["phone"],
            "Website": user["website"],
            "Company": user["company"]["name"]
        })

    df = pd.DataFrame(user_data)

    print(df)

    df.to_excel(output_path, index=False)

except requests.exceptions.HTTPError as e:
    print("HTTP Error:", e)

except requests.exceptions.ConnectionError:
    print("Connection Error!")

except requests.exceptions.Timeout:
    print("Request Timeout!")

except requests.exceptions.RequestException as e:
    print("Request Failed:", e)