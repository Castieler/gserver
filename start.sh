#!/bin/bash
#!/bin/bash


CWD=`pwd`
echo $CWD

PYTHON_PATH=/usr/local/python3/bin
export PATH=$PATH:$PYTHON_PATH
basepath='/usr/local/python3/bin'


PIDFILE=$CWD/python_server.pid
git stash && git pull

case "$1" in

  start)
    nohup $basepath/uwsgi uwsgi.ini >nohup.log 2>&1 &
    sleep 4
#    nohup $basepath/python manage.py celery worker -c 2 --loglevel=info >celery.log 2>&1 &
#    echo $! >> $PIDFILE
#    nohup $basepath/python manage.py celery flower >flower.log 2>&1 &
#    echo $! >> $PIDFILE
    ;;

  stop)
    kill -9 `cat $PIDFILE`
    rm -rf $PIDFILE
    ps -ef |grep $basepath/python | grep -v grep | cut -c 9-15 | xargs kill -s 9

    ;;

  restart)
    sh $0 stop
    sleep 1
    sh $0 start
    ;;

  *)
    echo "Options: {start|stop|restart}"
    ;;

esac

exit 0
