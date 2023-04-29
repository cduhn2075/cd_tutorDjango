FROM postgres

#ARG USER=craig
#RUN useradd -ms /bin/bash $USER
#USER $USER
#WORKDIR /home/$USER

#SHELL ["/bin/bash", "-o", "pipfail", "-c"]
#RUN echo $USER:$USER | chpasswd