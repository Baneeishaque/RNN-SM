cd algorithms/
wget https://www.amherstqa.com/log-files/fm/g729a_Steg.rar
sudo apt update
sudo apt install unrar
unrar l g729a_Steg.rar 
unrar x  g729a_Steg.rar g729a_0.rar g729a_Steg/English*
la
la g729a_Steg/
unrar l g729a_0.rar 
ls g729a_0 | wc -l
ls g729a_Steg | wc -l
ls | grep "^English2519...g729a" | xargs rm
ls | grep "^English2518...g729a" | xargs rm
ls | grep "^English2517...g729a" | xargs rm
ls | grep "^English2516...g729a" | xargs rm
ls | grep "^English2515...g729a" | xargs rm
ls | grep "^English2514...g729a" | xargs rm
ls | grep "^English2513...g729a" | xargs rm
ls | grep "^English25129..g729a" | xargs rm
ls | grep "^English25128..g729a" | xargs rm
ls | grep "^English25127..g729a" | xargs rm
ls | grep "^English25126..g729a" | xargs rm
ls | grep "^English251259.g729a" | xargs rm
ls | grep "^English251258.g729a" | xargs rm
ls | grep "^English251257.g729a" | xargs rm
ls | grep "^English251256.g729a" | xargs rm
ls | grep "^English251255.g729a" | xargs rm
ls | grep "^English251254.g729a" | xargs rm
ls | grep "^English251253.g729a" | xargs rm
ls | grep "^English251252.g729a" | xargs rm
ls | grep "^English251251.g729a" | xargs rm
ls | wc -l
cd ../g729a_Steg/
ls | grep "^English2519...g729a" | xargs rm
ls | grep "^English2518...g729a" | xargs rm
ls | grep "^English2517...g729a" | xargs rm
ls | grep "^English2516...g729a" | xargs rm
ls | grep "^English2515...g729a" | xargs rm
ls | grep "^English2514...g729a" | xargs rm
ls | grep "^English2513...g729a" | xargs rm
ls | grep "^English25129..g729a" | xargs rm
ls | grep "^English25128..g729a" | xargs rm
ls | grep "^English25127..g729a" | xargs rm
ls | grep "^English25126..g729a" | xargs rm
ls | grep "^English251259.g729a" | xargs rm
ls | grep "^English251258.g729a" | xargs rm
ls | grep "^English251257.g729a" | xargs rm
ls | grep "^English251256.g729a" | xargs rm
ls | grep "^English251255.g729a" | xargs rm
ls | grep "^English251254.g729a" | xargs rm
ls | grep "^English251253.g729a" | xargs rm
ls | grep "^English251252.g729a" | xargs rm
ls | grep "^English251251.g729a" | xargs rm
ls | wc -l
cd ..
la
rm g729a_0.rar g729a_Steg.rar 
la
