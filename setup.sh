PORT=$1
SERVER=$2
PASSWORD=$3
SENDER=$4

SERVER_CONFIG={\"port\":\"$PORT\",\"mail-server\":\"$SERVER\",\"password\":\"$PASSWORD\",\"sender\":\"$SENDER\"} 

echo $SERVER_CONFIG | jq '.' > configs/server-config.json