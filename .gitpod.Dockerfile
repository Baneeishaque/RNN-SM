FROM baneeishaque/gp-vnc-zsh-as-gh-chrome-idea-charm-conda3-mine-r-zilla-gram-matlab-mysql-phpwebstorm-1366x625-code

COPY environment.yml $HOME/

RUN conda env create -f $HOME/environment.yml \
 && rm $HOME/environment.yml

RUN pyenv global anaconda3-2020.11/envs/RNN-SM
RUN echo "conda activate RNN-SM" >> ~/.bashrc
RUN echo "conda activate RNN-SM" >> ~/.zshrc
