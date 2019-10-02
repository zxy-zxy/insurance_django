### Web application based on DRF
Available routes: 
* http://0.0.0.0:8000/api/v1/create_customer/
* http://0.0.0.0:8000/api/v1/1/create_policy/

#### Build & run
```bash
docker-compose -f docker-compose.yaml build
docker-compose -f docker-compose.yaml up
```

#### Tests
* Get your container id with
```bash
docker ps
```
* Run tests
```bash
docker exec -i -t <your_container_id_here> python manage.py test
```