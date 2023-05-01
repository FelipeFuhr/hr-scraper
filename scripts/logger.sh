if [ ! -d logger ]
then
    git clone https://github.com/FelipeFuhr/pylogger logger
fi
cd logger && git pull && make pkg
