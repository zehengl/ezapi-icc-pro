??? note "Create ICC_PRO instance"

    ```python
    from icc_pro import ICC_PRO

    host = "..."
    username = "..."
    password = "..."
    client_id = "..."
    client_secret = "..."

    iccpro = ICC_PRO(host, username, password, client_id, client_secret)
    ```

### To get valves general info

```python linenums="1" hl_lines="1"
iccpro.get_valves_general_info()
```

### To get valves info with GIS data

```python linenums="1" hl_lines="1"
iccpro.get_valves_gis_info()
```

### To get valves status

```python linenums="1" hl_lines="1"
iccpro.get_valves_status()
```
