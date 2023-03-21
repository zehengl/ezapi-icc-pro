```python
from icc_pro import ICC_PRO

host = "..."
username = "..."
password = "..."
client_id = "..."
client_secret = "..."

iccpro = ICC_PRO(host, username, password, client_id, client_secret)
```

### To get the user's virtual meters

```python
iccpro.get_virtual_meters_general_info()
```
