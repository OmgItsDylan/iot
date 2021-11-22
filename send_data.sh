#!/bin/bash

if [[ "$1" = "l1" ]]
then
  mosquitto_pub -d -q 1 -h "localhost" -p "1883" -t "v1/devices/me/telemetry" -u "9KoWvn7JUZ1xeoVUJPtr" -m {"status":$2}
  mosquitto_pub -d -q 1 -h "localhost" -p "1883" -t "v1/devices/me/telemetry" -u "9KoWvn7JUZ1xeoVUJPtr" -m {"location":bedroom}
  mosquitto_pub -d -q 1 -h "localhost" -p "1883" -t "v1/devices/me/telemetry" -u "9KoWvn7JUZ1xeoVUJPtr" -m {"intensity":$3}
elif [[ "$1" = "l2" ]]
then
  mosquitto_pub -d -q 1 -h "localhost" -p "1883" -t "v1/devices/me/telemetry" -u "8lDJcqe7waDWdpnp56Ye" -m {"status":$2}
  mosquitto_pub -d -q 1 -h "localhost" -p "1883" -t "v1/devices/me/telemetry" -u "8lDJcqe7waDWdpnp56Ye" -m {"location":kitchen}
  mosquitto_pub -d -q 1 -h "localhost" -p "1883" -t "v1/devices/me/telemetry" -u "8lDJcqe7waDWdpnp56Ye" -m {"intensity":$3}
elif [[ "$1" = "l3" ]]
then
  mosquitto_pub -d -q 1 -h "localhost" -p "1883" -t "v1/devices/me/telemetry" -u "VhB5McEIlaOY4YQorCnB" -m {"status":$2}
  mosquitto_pub -d -q 1 -h "localhost" -p "1883" -t "v1/devices/me/telemetry" -u "VhB5McEIlaOY4YQorCnB" -m {"location":livingRoom}
  mosquitto_pub -d -q 1 -h "localhost" -p "1883" -t "v1/devices/me/telemetry" -u "VhB5McEIlaOY4YQorCnB" -m {"intensity":$3}
elif [[ "$1" = "t1" ]]
then
  curl -v -X POST -d "{\"temperature\": $2}" http://localhost:9090/api/v1/EwgZPbrg0ZCMTQ7i9FRr/telemetry --header "Content-Type:application/json"
  curl -v -X POST -d "{\"humidity\": $3}" http://localhost:9090/api/v1/EwgZPbrg0ZCMTQ7i9FRr/telemetry --header "Content-Type:application/json"
  curl -v -X POST -d "{\"location\": Kitchen}" http://localhost:9090/api/v1/EwgZPbrg0ZCMTQ7i9FRr/telemetry --header "Content-Type:application/json"
elif [[ "$1" = "t2" ]]
then
  curl -v -X POST -d "{\"temperature\": $2}" http://localhost:9090/api/v1/t0ribl0rddawhoFYYccw/telemetry --header "Content-Type:application/json"
  curl -v -X POST -d "{\"humidity\": $3}" http://localhost:9090/api/v1/t0ribl0rddawhoFYYccw/telemetry --header "Content-Type:application/json"
  curl -v -X POST -d "{\"location\": Bedroom}" http://localhost:9090/api/v1/t0ribl0rddawhoFYYccw/telemetry --header "Content-Type:application/json"
elif [[ "$1" = "t3" ]]
then
  curl -v -X POST -d "{\"temperature\": $2}" http://localhost:9090/api/v1/PNLCvQREWEG5gIYZkXDD/telemetry --header "Content-Type:application/json"
  curl -v -X POST -d "{\"humidity\": $3}" http://localhost:9090/api/v1/PNLCvQREWEG5gIYZkXDD/telemetry --header "Content-Type:application/json"
  curl -v -X POST -d "{\"location\": Garden}" http://localhost:9090/api/v1/PNLCvQREWEG5gIYZkXDD/telemetry --header "Content-Type:application/json"
elif [[ "$1" = "f1" ]]
then
  echo -n '{"total": 10}' | coap post coap://localhost/api/v1/q08AYTqfJFfTMlxsaK9f/telemetry
  echo -n '{"consumption": 500}' | coap post coap://localhost/api/v1/q08AYTqfJFfTMlxsaK9f/telemetry
  echo -n '{"liquid": soho}' | coap post coap://localhost/api/v1/q08AYTqfJFfTMlxsaK9f/telemetry
elif [[ "$1" = "f2" ]]
then
  echo -n '{"total": 10}' | coap post coap://localhost/api/v1/YK14PpD43PisMRF6RP6l/telemetry
  echo -n '{"consumption": 500}' | coap post coap://localhost/api/v1/YK14PpD43PisMRF6RP6l/telemetry
  echo -n '{"liquid": soho}' | coap post coap://localhost/api/v1/YK14PpD43PisMRF6RP6l/telemetry
elif [[ "$1" = "f3" ]]
then
  echo -n '{"total": 10}' | coap post coap://localhost/api/v1/6gs9AOtSSP2QtUhLzmiw/telemetry
  echo -n '{"consumption": 500}' | coap post coap://localhost/api/v1/6gs9AOtSSP2QtUhLzmiw/telemetry
  echo -n '{"liquid": soho}' | coap post coap://localhost/api/v1/6gs9AOtSSP2QtUhLzmiw/telemetry
else
  echo "how to use script\n"
fi