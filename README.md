### Make virtual environment using uv
```
uv sync
```
### Install Ipykernel
```
python -m ensurepip --upgrade
```

### Generate app password
```
https://myaccount.google.com/apppasswords
```

### How to run this app
1. Make .env file in the root directory havin sender email and app password.
2. Run following command from the root directory
```
streamlit run app.py
```