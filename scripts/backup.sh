/usr/bin/backup loop &
while [ `date +"%Y%m%d%H%M"` -lt `date +"%Y%m%d"`1155 ]
do
  sleep 60
done
/usr/bin/backup now