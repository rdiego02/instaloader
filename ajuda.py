from cores import cor

def ajuda():
    print(cor("""
Com essa ferramenta é possível baixar fotos e vídeos do Instagram. 
Não é possível baixar stories no momento.

Sintaxe: 

        http://www.instagram.com/p/abcd <Índice(s) da(s) mídia(s)> - Baixa mídias específicas entre várias mídias.
        Isso é útil caso seja desejado apenas vídeos ou imagens específicos entre vários em um único post 
        
        Exemplo: http://www.instagram.com/p/abcd 2 5 7 
        O exemplo acima baixa especificamente a segunda, quinta e sétima mídia de um post

        Caso apenas a URL do post seja fornecida, todas as mídias serão baixadas.

""", 'amarelo'))
