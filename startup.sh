/etc/init.d/postgresql start > app.log 2>&1
su postgres -c "createuser root -s" >> app.log 2>&1
su postgres -c "createuser vulnwebsiteuser -s" >> app.log 2>&1
createdb vulnwebsite >> app.log 2>&1
psql -d vulnwebsite -c "ALTER USER vulnwebsiteuser WITH PASSWORD 'weakpasswordrule'" >> app.log 2>&1
psql -d vulnwebsite -c "DROP TABLE IF EXISTS users; CREATE TABLE users (id SERIAL PRIMARY KEY, role TEXT NOT NULL, firstname TEXT, lastname TEXT, username TEXT NOT NULL, password TEXT NOT NULL);" >> app.log 2>&1
psql -d vulnwebsite -c "DROP TABLE IF EXISTS customers; CREATE TABLE customers (id SERIAL PRIMARY KEY, firstname TEXT, lastname TEXT, username TEXT NOT NULL, password TEXT NOT NULL);" >> app.log 2>&1
psql -d vulnwebsite -c "DROP TABLE IF EXISTS messages; CREATE TABLE messages (id SERIAL PRIMARY KEY, to_id SERIAL, from_id SERIAL, body TEXT);" >> app.log 2>&1
cd /home/workspace/VulnWebApp && pip install wheel && pip install -r requirements.txt
