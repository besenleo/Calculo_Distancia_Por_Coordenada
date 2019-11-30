import materiais
import locais
from haversine import haversine
import erros

"""Aqui estao todas as funções principais do programa"""



def _checkar_se_e_float(n: float):
    """
    Função responsavel por checkar se o coordenada passado é float
    Retorna n caso esteja de acordo, senao torna None.
    """
    if isinstance(n, float):
        return n
    else:
        return None


def _checkar_se_e_graus(n: list):
    """
    Função responsavel por checkar se o coordenada passado esta em graus
    Retorna True caso esteja de acordo e uma string senao.
    """
    if isinstance(n, list):
        if 180 >= n[0] >= -180:
            if 60 >= n[1] >= 0:
                if 60 >= n[2] >= 0:
                    return _converter_graus_em_float(n)
                else:
                    raise erros.ValorDeSegundosErrado('Os valor referente ao segundos passado na lista nao segue o '
                                                     'padrão determinado!\n' + erros.explicacao())
            else:
                raise erros.ValorDeMinutosErrado('Os valor referente ao minutos passado na lista nao segue o padrão '
                                                 'determinado!\n' + erros.explicacao())
        else:
            raise erros.ValorDeGrausErrado('Os valor referente ao graus passado na lista nao segue o padrão '
                                           'determinado!\n' + erros.explicacao())
    else:
        return None


def _converter_graus_em_float(n: list) -> float:
    """
    Converte coordenadas geograficas em coordenadas decimais.
    É esperado que as coordenas geograficas sejam dadas pelo usuario em formato
    de lista. Ex: 22°10"11'W == [-22, 10, 11] / 47°21"01S == [-47, 21, 01]
    Retorna um as coordenas em float
    """
    graus = n[0]
    minutos = n[1] / 60
    segundos = n[2] / 3600
    if graus < 0:
        minutos = minutos * -1
        segundos = segundos * -1
    resultado = graus + minutos + segundos
    return resultado


def _definir_dois_pontos(x, y) -> tuple:
    """
    Função recebe dois pontos (x e y) e faz as devidas verifições e conversões.
    Retorna uma tuple com x e y em formato float.
    """
    lat = _checkar_se_e_graus(x)
    if not lat:  # Caso nao seja graus ira entrar nesse 'if'
        lat = _checkar_se_e_float(x)
        if not lat:  # Caso tb nao seja float ira entrar nesse 'if'
            raise erros.NaoFoiPossivelConverter(
                f"Nao foi possivel converter latitude (valor recebido: {x}). Por favor verifique os valor e tente novamente\n" + erros.explicacao())
    lon = _checkar_se_e_graus(y)
    if not lon: # Caso nao seja graus ira entrar nesse 'if'
        lon = _checkar_se_e_float(y)
        if not lon: # Caso tb nao seja float ira entrar nesse 'if'
            raise erros.NaoFoiPossivelConverter(
                f"Nao foi possivel converter longitude (valor recebido: {x}). Por favor verifique os valor e tente novamente\n" + erros.explicacao())

    coordenadas = (lat, lon)
    return coordenadas


def detectar_tipo(material: str, eWeb=None):
    """Essa função é responsavel por identificar o tipo de material digitado pelo usuario"""
    if not isinstance(material, str):
        raise TypeError("O valor inserido não é um caracter")
    else:
        if material in materiais.metais():
            return "Metal"
        elif material in materiais.papeis():
            return "Papel"
        elif material in materiais.plasticos():
            return "Plastico"
        elif material in materiais.vidros():
            return "Vidros"
        elif material in materiais.organicos():
            return "Organico"
        elif material in materiais.eletronicos():
            return "Eletronico"
        elif material in materiais.entulhos():
            return "Entulho"
        elif material in materiais.vegetais():
            return "Vegetação"
        elif material in materiais.nao_reciclaveis():
            return "Não é reciclaveis"
        else:
            if eWeb:
                return """
                        Ops! Não pude identificar que tipo de material esse item é categorizado.
                        Dica: tente digitar o material no singular e sem acentos. Ex: papéis, ficaria papel"""
            raise erros.MaterialNaoIdentificado(
                """
                Ops! Não pude identificar que tipo de material esse item é categorizado.
                Dica: tente digitar o material no singular e sem acentos. Ex: papéis, ficaria papel""")


def encontrar_lugar(material: str, x_user, y_user, eWeb=None):
    """
    Função responsável por pegar os inputs da localização e material a ser reclicado do usuario.
    Retorna a local mais proximo e a distancia (em linha reta e quilometros) para o usuario.
    """
    # Por boa pratica escolhemos declarar a variaveis antes.
    lugares_corretos = []
    lugar_perto = None
    distancia = None

    # itera por todos os lugares em locais.py e encontra os lugares que coletam o material descrito pelo usuario.
    for lugar in locais.lugares():  # itera pela lista de dicionarios (cada dict = lugar)
        for itens in lugar["coletam"]:  # itera pela lista de items que o lugar coleta
            if material in itens:
                lugares_corretos.append(lugar)
    # itera pelos lugares que coletam o material do usuario e encontra o mais perto.
    if lugares_corretos:
        for lugar in lugares_corretos:
            # na primeira execução do for dist_x e dist_y serão None.
            if lugar_perto is None or distancia is None:
                # Caso nenhum valor seja menor que o primeiro, logo o primeiro é o menor valor.
                lugar_perto = lugar
                origem = _definir_dois_pontos(x_user, y_user)
                destino = _definir_dois_pontos(lugar['latitude'], lugar['longitude'])
                distancia = haversine(origem, destino)
            else:
                origem = _definir_dois_pontos(x_user, y_user)
                destino = _definir_dois_pontos(lugar['latitude'], lugar['longitude'])
                distancia_lugar = haversine(origem, destino)
                if distancia_lugar < distancia:
                    lugar_perto = lugar
                    distancia = distancia_lugar
    else:
        if eWeb:  # Caso seja na web isso vai ser true e vai retorna uma string ao inves um raise
            distancia = None
            lugar_perto = """
                            Desculpe! Não encontramos nenhum lugar que coleta esse material. 
                            Tente informar o tipo dele, por exemplo: Carta = tipo: Papel. 
                            Dica: tente digitar o material no singular e sem acentos. Ex:papéis, ficaria papel"""
            return lugar_perto, distancia
        raise erros.MaterialNaoIdentificado("""
                                            Desculpe! Não encontramos nenhum lugar que coleta esse material. 
                                            Tente informar o tipo dele, por exemplo: Carta = tipo: Papel. 
                                            Dica: tente digitar o material no singular e sem acentos. Ex:papéis, ficaria papel""")

    return lugar_perto, distancia
