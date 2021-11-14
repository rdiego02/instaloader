def cor(str, cor):
    cores = {
            'cinza':'\033[1;30m',
            'vermelho':'\033[1;31m',
            'verde':'\033[1;32m',
            'amarelo':'\033[1;33m',
            'roxo':'\033[1;34m',
            'ciano':'\033[1;36m'
            }
    return f'{cores[cor]}{str}\033[m'
