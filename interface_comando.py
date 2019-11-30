#!/usr/bin/python
import sys
import argparse
import erros
import funcoes



def preparando_arparse():
    """
    Esta função é reponsavel por definir os argumentos esperados pela commandline.
    """
    parser = argparse.ArgumentParser(description='Determina o lugar mais perto para descartar seu material baseado em '
                                                 'suas coordenadas!\n' + erros.explicacao())
    parser.add_argument('--lat', type=float, metavar='', help='Latitude da sua localização atual em float.')
    parser.add_argument('--latg', nargs='+', type=int, metavar='', help='Latitude da sua localização atual em graus. (Leia a descrição acima para mais informaçoes e dicas!)')
    parser.add_argument('--lon', type=float, metavar='', help='Longitude da sua localização atual em float.')
    parser.add_argument('--long', nargs='+', type=int, metavar='', help='Longitude da sua localização atual em graus. (Leia a descrição acima para mais informaçoes e dicas!)')
    parser.add_argument('--mat', type=str, required=True, metavar='', help='Material que voce deseja descartar.')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = preparando_arparse()
    if args.lat is None and args.latg is None:
        raise erros.ParametroFaltando("Por favor fornecer sua latitude em float ou graus\n" + erros.explicacao())
    if args.lon is None and args.long is None:
        raise erros.ParametroFaltando("Por favor fornecer sua latitude em float ou graus\n" + erros.explicacao())
    lat = args.lat or args.latg  # Pego o valor que é diferente de None, caso ambos sejam entao pega o primeiro
    lon = args.lon or args.long
    mat = args.mat
    mat = mat.lower()  # converte para lowercase a string
    # Detecta o tipo do material e fala para o usuario
    tipo = funcoes.detectar_tipo(mat)
    print(f'Seu material poderá ser descartado como: {tipo}')
    print("")
    # Encontro o local mais proximo que recicla aquele tipo de material
    lugar, distancia = funcoes.encontrar_lugar(mat, lat, lon)
    print(f"O lugar mais proximo onde você pode descartar seu material é {lugar['nome']} , no endereço {lugar['endereco']}, o horario de atendimento é de {lugar['atendimento']}")
    print(f"Voce esta a {round(distancia, 2)} KM deste lugar")
