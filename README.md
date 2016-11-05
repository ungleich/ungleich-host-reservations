Create me like this:

```bash
docker run --name hosts --network=ethz-scientific -e HOST=postgres -e DB=kea_db -e USER=kea -e PASSWORD=dummy_password ungleich/ungleich-host-inventory
```

Later, when you need to know the full list of host reservations, you can call me again like this:

```bash
docker start -i hosts
```

When you get bored about me (or if your Postgres credentials change), just delete me:

```bash
docker rm hosts
```
