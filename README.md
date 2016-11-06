![alt text](http://www.ungleich.ch/img/logo_200x200.svg "ungleich")

# ungleich-host-reservations

Container intended to get all host reservations from a running ungleich/ungleich-kea container.

# Creating the container

If you want to specify the database connection parameters manually, you can run/create the container like this:
```bash
docker run --name hosts --network=<user-defined-network> -e HOST=postgres -e DB=kea_db -e USER=kea -e PASSWORD=dummy_password ungleich/ungleich-host-inventory
```

Otherwise, if you prefer to take the parameters directly from a running Kea container, you can run/create the container with:
```bash
docker run --name hosts --network=<user-defined-network> --volumes-from=<running-kea-container> ungleich/ungleich-host-inventory
```

# Getting host reservations at any time.

Later, when you need to know the full list of host reservations, you can simply reuse the previously created container:

```bash
docker start -i hosts
```

# How to update database credentials?

When you need to update the database credentials (whether specified manually or automatically), you need to destroy the container and create a new one.
