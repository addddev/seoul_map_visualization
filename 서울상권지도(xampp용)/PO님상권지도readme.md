# PO님 상권지도 readme


xampp면 거의 잘 될텐데 안 되시면
$uid = posix_getuid();
    $userInfo = posix_getpwuid($uid);
    echo "User: " . $userInfo['name'];
이거 입력하셔서 누가 파일 소유주인지 확인하시고, daemon:daemon자리를 소유주의 이름으로 바꿔주세요.
ex) www-data가 소유주이면 sudo chown www-data:www-data /opt/lampp/htdocs/시군구_dict.json

sudo /opt/lampp/lampp start


sudo mv /home/addd/Downloads/addd_commercial_district.php /home/addd/Downloads/addd_commercial_district.py /home/addd/Downloads/addd_commercial_district_json_making.ipynb /home/addd/Downloads/소분류_dict.json /home/addd/Downloads/시군구_dict.json /opt/lampp/htdocs



sudo chmod 666 /opt/lampp/htdocs/addd_commercial_district.php /opt/lampp/htdocs/addd_commercial_district.py /opt/lampp/htdocs/addd_commercial_district_json_making.ipynb /opt/lampp/htdocs/소분류_dict.json /opt/lampp/htdocs/시군구_dict.json


sudo chown daemon:daemon /opt/lampp/htdocs/addd_commercial_district.php /opt/lampp/htdocs/addd_commercial_district.py /opt/lampp/htdocs/addd_commercial_district_json_making.ipynb /opt/lampp/htdocs/소분류_dict.json /opt/lampp/htdocs/시군구_dict.json


sudo chmod -R 666 /opt/lampp/htdocs
sudo chown -R daemon:daemon /opt/lampp/htdocs

sudo chmod +x /opt/lampp/htdocs/addd_commercial_district.py

sudo chown -R daemon:daemon /opt/lampp/htdocs
sudo find /opt/lampp/htdocs -type d -exec chmod 777 {} \; -type f -exec chmod 666 {} \;


