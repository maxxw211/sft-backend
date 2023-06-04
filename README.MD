# sft-backend

## Configuration

### Install depencdencies

```shell
poetry install
```

### Install pre-commit hooks

```shell
poetry run pre-commit install
poetry run pre-commit autoupdate
```

## How to use 

```
After you install all the dependencies, 
you need to write the settings 
and connect data base to the local file . 
You can do this with makefile.
```

## Register user 

```
http://127.0.0.1:<your port>/api/users/register/
method POST
```

## Login user 

```
http://127.0.0.1:<your port>/api/users/login/
method POST
```

## For actions with user you should use this endpoint and methods (GET, POST, PUT, PATCH, DELETE):

```
http://127.0.0.1:<your port>/api/users/
or
http://127.0.0.1:<your port>/api/users/<user id>
```

## For actions with products you should use this endpoint and methods (GET, POST, PUT, PATCH, DELETE):

```
http://127.0.0.1:<your port>/api/products/
or
http://127.0.0.1:<your port>/api/products/<product id>
```

## For actions with organization you should use this endpoint and methods (GET, POST, PUT, PATCH, DELETE):

```
http://127.0.0.1:<your port>/api/organization/
or
http://127.0.0.1:<your port>/api/organization/<organization id>
```

## For actions with credit application you should use this endpoint and methods (GET, POST, PUT, PATCH, DELETE):

```
http://127.0.0.1:<your port>/api/credit_application/
or
http://127.0.0.1:<your port>/api/credit_application/<credit_application id>
```
### You can also use the endpoint to get the organization ID from the credit application 

```
http://127.0.0.1:<your port>/api/credit_application/<credit_application id>/organization_data/
```

## For actions with contracts you should use this endpoint and methods (GET, POST, PUT, PATCH, DELETE):

```
http://127.0.0.1:<your port>/api/contracts/
or
http://127.0.0.1:<your port>/api/contracts/<contract id>
```