

sudo killall mplayer
sudo mpc -q update 
sudo mpc -q clear ; mpc -q ls Music/Artist/ | grep *flac |mpc -q add ; mpc -q shuffle ; mpc -q crossfade 3 ; mpc play

