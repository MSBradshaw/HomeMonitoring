# one command line argument, name that the data should be labeled with: basement, upstairs or main
# run the script every 15 mintes (900 seconds)
watch -n 900 python3 bme280.py $1
