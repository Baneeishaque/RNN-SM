FROM baneeishaque/baneeishaque/gitpod-workspace-full-vnc-1366x768-tint2-pcmanfm-zsh-android-studio-gh-chrome-intellij-idea-pycharm

COPY environment.yml $HOME/

RUN conda env create -f $HOME/environment.yml \
 && rm $HOME/environment.yml

# RUN pyenv global anaconda3-2020.11/envs/RNN-SM
# RUN echo "conda activate RNN-SM" >> ~/.bashrc
# RUN echo "conda activate RNN-SM" >> ~/.zshrc
