```python
from icc_pro import ICC_PRO

host = "..."
username = "..."
password = "..."
client_id = "..."
client_secret = "..."

iccpro = ICC_PRO(host, username, password, client_id, client_secret)
```

### To get the user's valves run

```python
iccpro.get_valves_general_info()
```

### To get the user's valves info with GIS data

```python
iccpro.get_valves_gis_info()
```

### To get the user's valves status

```python
iccpro.get_valves_status()
```
