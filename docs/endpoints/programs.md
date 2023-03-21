```python
from icc_pro import ICC_PRO

host = "..."
username = "..."
password = "..."
client_id = "..."
client_secret = "..."

iccpro = ICC_PRO(host, username, password, client_id, client_secret)
```

### To get the user's programs

```python
iccpro.get_programs_general_info()
```

### To get the user's programs with detailed information

```python
iccpro.get_programs_detailed_info()
```
