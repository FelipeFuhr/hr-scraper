FROM ubuntu:22.04@sha256:9a0bdde4188b896a372804be2384015e90e3f84906b750c1a53539b585fbbe7f

ENV DEBIAN_FRONTEND=noninteractive 

COPY hr_scraper hr_scraper
COPY scripts scripts
COPY Makefile Makefile
COPY pyproject.toml pyproject.toml
COPY README.md README.md

RUN apt-get update                                  && \
    apt-get install -y                              \
            python3-pip=22.0.2+dfsg-1ubuntu0.2      \
            git-all=1:2.34.1-1ubuntu1.8             && \
    pip3 install pip==23.0.1                        \
                 poetry==1.4.2                      && \
    make pkg                                        && \
    apt remove -y git-all                           && \
    apt -y autoremove                               && \
    chmod a-w /etc                                  && \
    groupadd --gid 20001 pod                        && \
    useradd --uid 10001                             \
            --shell /bin/bash                       \
            --create-home pod                       \
            --gid pod                               && \
    groupadd --gid 20000 application                && \
    useradd --uid 10000                             \
            --gid application                       \
            --shell /bin/bash                       \
            --create-home application               

USER application

WORKDIR /home/application

ENTRYPOINT ["sleep", "7200"]
