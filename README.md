# Aurora docker 
Dockerfiles to run [aurora](https://github.com/martflu/aurora) in a docker environment with docker-compose. 
By default the source directory is __not__ mounted as volume, so you'll have to build the aurora dockerfile every time you
change something in the source.

This was done like this, because the dockerfile changes settings files that where (and propably shouldn't) committed to the
version control.

## Setup

- Install [docker](https://docs.docker.com/engine/installation/) and 
[Compose](https://docs.docker.com/compose/install/)

- Clone this repo: `git clone https://github.com/sepal/aurora_docker.git` 

- Go into the cloned repo: `cd aurora_docker`

- Clone the aurora source: 
`git clone https://github.com/martflu/aurora.git aurora/source`

- Create env file for the database in a new dir called config. The file should 
look like this: `POSTGRES_PASSWORD=mysecret` 
Example using pwgen: 
```
# Create the config dir
mkdir config
# Create one password with 20 characters
echo POSTGRES_PASSWORD=`pwgen -n -s -y 20 1` > config/password.env
```

- Bootstrap everything and run it in the background: `docker-compose up -d`

- Setup the database: `docker-compose run aurora python manage.py migrate`

- Collect all static files: 
`docker-compose run aurora python manage.py collectstatic`

- Restart the containers, so that aurora starts using the newly created database 
schema: `docker-compose restart`

- Aurora should now run under the port 8080. If you are using docker-machine 
(Mac Os X & Windows) you might need to get your ip first: `docker-machine ip`.

## Howto?
All commands you would run on you local host or in a vagrant environment can be 
also run in the container. Just prefix them with `docker-compose run aurora `. 
Here are some examples:

Run the tests
- `docker-compose run aurora python manage.py test`

Login into the aurora container
- `docker-compose run aurora bash`
If you need vim or any other tool update the source first: `apt-get update`. 
Now you can install them using apt: `apt-get install -y vim`

Create demo data:
- `docker-compose run aurora python manage.py populate_demo_data`

Rebuild the aurora container:
- `docker-compose stop`
- `docker-compose rm aurora` answer with `y`
- `docker-compose build`
- `docker-compose up -d`
All data is kept, so no need to run `migrate` or anything else again.

## Cleanup
You might notice that compose runs a new container for every 
`docker-compose run` if you list all containers using `docker ps -a`.
You clean up all the dead containers using: 
`docker ps -a | grep _run | awk '{print $1}' | xargs docker rm`