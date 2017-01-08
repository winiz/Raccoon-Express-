# Make sure the Apt package lists are up to date, so we're downloading versions that exist.
cookbook_file "apt-sources.list" do
  path "/etc/apt/sources.list"
end
execute 'apt_update' do
  command 'apt-get update'
end

# Base configuration recipe in Chef.
package "wget"
package "ntp"
cookbook_file "ntp.conf" do
  path "/etc/ntp.conf"
end
execute 'ntp_restart' do
  command 'service ntp restart'
end

package 'python' do
  action :install
end
execute 'python-setup' do
  command 'sudo apt-get install python3'
end
cookbook_file "get-pip.py" do
  path "/etc/get-pip.py"
end
execute 'pip-setup' do
  command 'python3 /etc/get-pip.py'
end

execute 'git-setup' do
  command 'sudo apt-get install git'
end

package "python3.5"
package "libpython3.5-dev"
package "python3.5-dev"
package "python3-pip"

package "postgresql"
package "postgresql-server-dev-all"

execute 'install_psycopg2' do     #Dependent on 'postgresql-server-dev-all'
  command 'pip3 install psycopg2'
  #ALTERNATIVELY: command apt-get install python3-psycopg2
end

execute 'create_postgresql_db' do
  command 'echo "CREATE DATABASE mydb; CREATE USER ubuntu; GRANT ALL PRIVILEGES ON DATABASE mydb TO ubuntu;" | sudo -u postgres psql'
end
execute 'django-setup' do
  command 'git clone https://github.com/django/django.git'
  command 'mkdir ~/.virtualenvs'
  command 'sudo apt-get install python3-pip'
  command 'sudo pip3 install virtualenv'
  command 'virtualenv ~/.virtualenvs/djangodev'
  command '. ~/.virtualenvs/djangodev/bin/activate'
  command 'pip install django'
  command 'sudo pip install django-stripe-payments'
end

execute 'server' do
  user 'ubuntu'
  cwd '/home/ubuntu/project/finalproject'
  command 'nohup python3 ./manage.py runserver 0.0.0.0:8080&'
end

execute 'update-migrate' do
  user 'ubuntu'
  cwd '/home/ubuntu/project/finalproject'
  command 'nohup python3 ./manage.py makemigrations'
end

execute 'create-database' do
  user 'ubuntu'
  cwd '/home/ubuntu/project/finalproject'
  command 'nohup python3 ./manage.py migrate'
end

package "libpcre3"
package "libpcre3-dev"

execute 'install_uwsgi' do
  command 'pip3 install uwsgi'
end

cookbook_file "rc.local-default" do
  path "/etc/rc.local"
end

execute 'start_uwsgi' do
  command '/etc/rc.local'
end

execute 'database-setup' do
  user 'ubuntu'
  cwd '/home/ubuntu/project/finalproject'
  command 'nohup python3 ./manage.py loaddata initial_data.json'
end

execute 'user-setup' do
  user 'ubuntu'
  cwd '/home/ubuntu/project/finalproject'
  command 'nohup python3 ./manage.py loaddata users.json'
end

execute 'usertype-setup' do
  user 'ubuntu'
  cwd '/home/ubuntu/project/finalproject'
  command 'nohup python3 ./manage.py loaddata usertype.json'
end

execute 'static-setup' do
  user 'ubuntu'
  cwd '/home/ubuntu/project/finalproject'
  command 'nohup python3 manage.py collectstatic --noinput'
end
