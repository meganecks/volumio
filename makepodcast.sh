#!/bin/bash

channel=$1

## ch. list
# bayfm
# interfm
# jwave
# nippon
# tokyofm


# ruby makepodcast.rb TEST http://volumio.local/radio/jwave/ ~/radio/jwave > ~/radio/jwave.xml

# ruby /home/pi/bin/makepodcast.rb $channel  http://volumio.local/radio/$channel/ ~/radio/$channel  > ~/radio/$channel.xml
ruby /home/pi/bin/makepodcast.rb $channel  http://10.0.1.12/radio/$channel/ ~/radio/$channel  > ~/radio/$channel.xml


