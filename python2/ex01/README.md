## Create the virtual environment:

You might need to call deactivate to activate system-wide Python environment
```
deactivate
```

Create virtual environment:
```
python3 -m virtualenv .venv
```

## Activate the virtual environment:

On Windows:
```
.venv\Scripts\activate
```

On macOS and Linux:
```
source .venv/bin/activate
```

## Install dependencies from requirements.txt:

```
pip install -r requirements.txt
```

## Verify the installation:

```
pip list
```

## Deactivate:

```
deactivate
```

## Create requirements.txt:

```
pip freeze > requirements.txt
```