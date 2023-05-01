if [ ! -d file-handler ]
then
    git clone https://github.com/FelipeFuhr/file-handler
fi
cd file-handler && git pull && make pkg
