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

### To get programs general info

```python linenums="1" hl_lines="1"
iccpro.get_programs_general_info()
```

### To get programs with detailed information

```python linenums="1" hl_lines="1"
iccpro.get_programs_detailed_info()
```
