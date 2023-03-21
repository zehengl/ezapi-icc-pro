```python
from icc_pro import ICC_PRO

host = "..."
username = "..."
password = "..."
client_id = "..."
client_secret = "..."

iccpro = ICC_PRO(host, username, password, client_id, client_secret)
```

### To get the user's analog inputs

```python
iccpro.get_analog_inputs_general_info()
```

### To get the user's analog inputs current data

```python
iccpro.get_analog_inputs_current_data()
```

### To get the user's analog inputs historical data

```python
from datetime import datetime


def make_datetime_str(dt):
    return "".join(
        [
            f"{dt.year}",
            f"{dt.month}".zfill(2),
            f"{dt.day}".zfill(2),
            f"{dt.hour}".zfill(2),
            f"{dt.minute}".zfill(2),
            f"{dt.second}".zfill(2),
        ]
    )


fromdatetime = make_datetime_str(datetime(2022, 1, 1))
todatetime = make_datetime_str(datetime(2023, 1, 31, 1, 2, 3))

iccpro.get_analog_inputs_historical_data(
    fromdatetime=fromdatetime, todatetime=todatetime, resolution=3
)
```
