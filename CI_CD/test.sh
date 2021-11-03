chmod +x ./linux/hello

./linux/hello &

sleep 3

for i in Anakin Luke Leia Kylo Rey;
do
    echo "$(date): $(curl -s http://localhost:11000/${i})"
done
