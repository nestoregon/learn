# learning Mysql

The first thing you should do is downloading mysql for your machine. This is done easily by doing:

```bash
sudo apt-get install mysql
```

To login:
```bash
sudo mysql -u root -p
```

To show all databases:
```sql
show databases;
```

To create a new db
```sql
create database name_db;
```

To use that database
```sql
use name_db;
```

To grant all access to a user being root:
```sql
GRANT ALL PRIVILEGES ON database_name.* TO 'username'@'localhost';
```
