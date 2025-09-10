printf "\033c\033[43;30m\n"
python3 count.py 5000 &
ngrok http http://0.0.0.0:5000 &