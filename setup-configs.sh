echo "Setting Up Server Configurations - server-config.json"
read -p "Enter PORT: " PORT
read -p "Enter MAIL SERVER: " SERVER
read -p "Enter SENDER: " SENDER
read -p "Enter PASSWORD: " PASSWORD

SERVER_CONFIG={\"port\":\"$PORT\",\"mail-server\":\"$SERVER\",\"password\":\"$PASSWORD\",\"sender\":\"$SENDER\"} 

echo $SERVER_CONFIG | jq '.' > configs/server-config.json

echo "Getting Logsmith Configurations Template - log.config.json"
curl -s -o ./configs/log.config.json https://raw.githubusercontent.com/TanmoySG/logsmith-monitor/main/libraries/js/examples/configs/jsonConfig.json

echo "To configure log.config.json visit - https://github.com/TanmoySG/logsmith#configurations-1"

# LOGCONFIGMOD="$(jq '.monitor.port="8096"' configs/log.config.json)" && echo $logconfigmod | jq . > configs/log.config.json 
