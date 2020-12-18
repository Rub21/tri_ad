<h1 align="center">TRI-AD challenge 👋</h1>

Script to read a file in the cloud or a local file(testing) and return the largest numbers, format file should be `<unique record identifier><white_space><numeric value>`

### 🏠 [Homepage](git@github.com:Rub21/tri_ad.git)

## Install

- Local
  
```sh
git clone clone git@github.com:Rub21/tri_ad.git
cd tri_ad/
python setup.py install
```

- Docker container

```sh
git clone clone git@github.com:Rub21/tri_ad.git
cd tri_ad/
docker-compose build
```
## Usage

```sh
tri_ad --help
```

- Executing the script in local and docker container
  
```sh
# Runing the CLI from docker 
docker run rub21/tri_ad:v1 \
  tri_ad \
    --file_path=https://amp-spacemaps-technical-challenge.s3-ap-northeast-1.amazonaws.com/spacemaps_technical_challenge.txt \
    --large_numbers=20

# Runing the CLI from local
tri_ad \
  --file_path=https://amp-spacemaps-technical-challenge.s3-ap-northeast-1.amazonaws.com/spacemaps_technical_challenge.txt \
  --large_numbers=2

# Runing on docker-compose with default values

docker-compose up

```

By default `docker-compose up` will execute the script with the default values.

- `file_path`: https://amp-spacemaps-technical-challenge.s3-ap-northeast-1.amazonaws.com/spacemaps_technical_challenge.txt
- `large_numbers`:100

## Run tests

```sh
python -m unittest
```

## Author

👤 **Rub21**

* Website: http://rub21.com/
* GitHub: [@Rub21](https://github.com/Rub21)
