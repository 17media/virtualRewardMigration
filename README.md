# VirtualRewardMigration

## Prerequisite

- python >= 3.10
- Install virtualenv
```shell
python3 -m pip install virtualenv
```
## Env setup
- Go to virtual env
```shell
python3 -m virtualenv ./venv
source ./venv/bin/activate
```
- Install dependencies
```shell
pip install -r requirements.txt
```

## Example
```shell
# 1. create backgroundColor
python main.py -t backgroundColor -a create -e <env> --accessToken=<user_token>

# 2. create TextColor
python main.py -t textColor -a create -e <env> --accessToken=<user_token>

# 3. send reward background color
python main.py -t backgroundColor -a send -e <env> --accessToken=<user_token>

# 4. send reward text color
python main.py -t textColor -a send -e <env> --accessToken=<user_token> 
```