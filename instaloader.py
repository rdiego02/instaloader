import requests
import re
from os import system, name
from cores import cor
from estilo import estilo
from ajuda import ajuda


def baixa(link, indice=None):
    try:
        if 'www.instagram.com/reel/' in link:
            change_link = link.split('reel')
            link = 'p'.join(change_link)
        elif 'www.instagram.com/tv/' in link:
            change_link = link.split('tv')
            link = 'p'.join(change_link)

        if 'www.instagram.com/p/' not in link:
            print(cor('Insira o link de um post do Instagram.', 'vermelho'))
            exit()

        else:
            while True:
                try:
                    htmlpage = requests.get(link).text.split('\\u0026')
                    htmlpage = '&'.join(htmlpage)
                    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', htmlpage)
                    break
                except requests.exceptions.ConnectionError:
                    print(cor('Erro de conexão.', 'vermelho'))
                    exit()
                except requests.exceptions.MissingSchema:
                    link = 'http://' + link
        pics = []
        match = '/v/t51.2885-15/e35/'
        for url in urls:
            if '.jpg' in url and url not in pics and match in url: 
                pics.append(url)
            elif '.mp4' in url and url not in pics:
                pics[-1] = url
        quantidade = len(pics)
        if quantidade == 0:
            print(cor('Nenhuma mídia encontrada.', 'vermelho'))
            exit()
        else:
            porcent = 0
            if not indice:
                while True:
                    confirm = input(cor(f'{quantidade} mídia(s) encontrada(s). Baixar?(S/N): ', 'amarelo'))[0]
                    if confirm in 'Nn':
                        exit()
                    elif confirm in 'Ss':
                        break
                for midia in pics:
                    nome = midia.split('_')[1]
                    porcent = porcent + 100/quantidade
                    print(f'Baixando...{porcent:.0f}%', end='\r')
                    mediabytes = requests.get(midia).content
                    if '.jpg' in midia:
                        open(f'Downloads/{nome}.jpg', 'wb').write(mediabytes)
                    elif '.mp4' in midia:
                        open(f'Downloads/{nome}.mp4', 'wb').write(mediabytes)
            else:
                while True:
                    confirm = input(cor(f'Baixar {len(indice)} das {quantidade} mídias encontradas?(S/N): ', 'amarelo'))[0]
                    if confirm in 'Ss':
                        break
                    elif confirm in 'Nn':
                        exit()
                for n in indice:
                    try:
                        n = int(n)
                        nome = pics[n-1].split('_')[1]
                        porcent = porcent + 100/len(indice)
                        print(f'Baixando...{porcent:.0f}%', end='\r')
                        mediabytes = requests.get(pics[n-1]).content
                        if '.jpg' in pics[n-1]:
                            open(f'Downloads/{nome}.jpg', 'wb').write(mediabytes)
                        elif '.mp4' in pics[n-1]:
                            open(f'Downloads/{nome}.mp4', 'wb').write(mediabytes)
                    except IndexError:
                        print(cor(f'Nenhuma mídia na posição {n}', 'vermelho'))
                        exit()
                    except ValueError:
                        print(cor(f'"{n}" não é uma posição válida. Informe um valor inteiro.', 'vermelho'))
                        exit()
            print('\n')     
            print(cor('Mídias salvas em Downloads.', 'verde'))
    except KeyboardInterrupt:
        print(cor('Saindo...', 'amarelo'))


if 'nt' not in name:
    system('clear')
else:
    system('cls')

estilo()
print(cor('Digite "ajuda" (sem as aspas) para obter informações sobre como usar o instaloader.', 'cinza'))
try:
    comando = input('>>> ').lstrip().rstrip()
    comando = comando.split(' ')
    indice = comando[1:]
    if 'ajuda' in comando:
        ajuda()
        exit()
except KeyboardInterrupt:
    print(cor('Saindo...', 'amarelo'))
    exit()

baixa(comando[0], indice)
