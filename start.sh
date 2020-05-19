/usr/bin/tmux new-session -d -s Weather
/usr/bin/tmux set-option -t Weather set-remain-on-exit on
/usr/bin/tmux new-window -d -n 'Website' -t Weather:1 'sudo python /home/pi/Weather/weatherapp.py'


