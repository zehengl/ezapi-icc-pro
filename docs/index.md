<figure markdown>
![Logo](https://cdn0.iconfinder.com/data/icons/smart-farm-line-agriculture-technology/512/Irrigation-512.png){ width="128" }
</figure>

# ezapi-icc-pro

A Python wrapper for ICC PRO RESTful API

## Install

    pip install ezapi-icc-pro

## Usage

```python
from icc_pro import ICC_PRO

host = "..."
username = "..."
password = "..."
client_id = "..."
client_secret = "..."

iccpro = ICC_PRO(host, username, password, client_id, client_secret)
```

See detailed usages at [Endpoints](endpoints/index.md) page.
