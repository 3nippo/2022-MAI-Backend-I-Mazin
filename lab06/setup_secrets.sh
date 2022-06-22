set -e

docker swarm init || [ $? -eq 1 ]

echo "Enter secret db name (Ctrl+D to end secret)"
docker secret create db_name -

echo "Enter secret db superuser (Ctrl+D to end secret)"
docker secret create db_usr -

echo "Enter secret db password (Ctrl+D to end secret)"
docker secret create db_pwd -
