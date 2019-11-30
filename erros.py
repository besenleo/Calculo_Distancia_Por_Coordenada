def explicacao():
    exemplo = """
                Os valores das coordenadas devem estar em float ou graus.
                Caso você deseje colocar em float eles devem seguir esse formato:
                Ex1: 22.012311.
                Ex2: -22.012311.
                Ou caso desejar passa-los em graus, eles devem estar no formato abaixo, com cada numero separado por espaço e sem simbolos ou letras:
                Ex1: 22°01\"11\'W = -22 1 11.
                Ex2: 22°01\"11\'E = 22 1 11.
                
                Dica1: lembre-se quando sentido for W(Oeste) ou S(Sul) o primeiro valor é negativo (22°01\"11\'W = -22 1 11).
                Dica2: NÃO coloque o zero a esquerda. Ex: 22°01\"00\'W fica 22 01 00.
                Dica3: Graus pode variar de -180 ate 180, minutos e segundos podem variar de 0 a 60. Por exemplo a coordenada 22°100\"78\'E não existe!"""
    return exemplo


class MaterialNaoIdentificado(Exception):
    pass


class ValorDeSegundosErrado(Exception):
    pass


class ValorDeMinutosErrado(Exception):
    pass


class ValorDeGrausErrado(Exception):
    pass


class ValorInesperado(Exception):
    pass


class ParametroFaltando(Exception):
    pass


class NaoFoiPossivelConverter(Exception):
    pass