playlist=$1

sudo killall mplayer
sudo mpc clear ; mpc load $playlist ;mpc shuffle ;mpc crossfade 3 ; mpc play
