"""Lista com todos os materiais e seus respectivos tipos"""


def plasticos():
    plastico = ("copo descartável", "garrafa de plástico", "saco", "sacola",
                "frasco de produto", "embalagens pet", "cano", "tubo de pvc",
                "caneta", "tampa", "embalagem tipo tupperware",
                "embalagem de produto de limpeza", "tampinha de garrafa")
    return plastico


def papeis():
    papel = ("jornal", "revista", "lista telefônica", "papel sulfite", "papel de fax",
             "folha de caderno", "formulário de computador", "caixa de papelão",
             "apara de papel", "fotocópia", "envelope", "cartaz", "caixa de pizza",
             "cartolina", "papel cartão", "embalagem longa vida", "papel", "papeis")
    return papel


def vidros():
    vidro = ("pote de conserva", "embalagem de vidro", "frasco de remédio vazio",
             "copo", "caco de vidro", "tampa de forno", "tampa de micro-ondas",
             "garrafa de vidro", "vidro", "vidros")
    return vidro


def metais():
    metal = ("lata", "latas", "enlatado", "enlatados", "panela sem cabo", "ferragem", "arame", "chapa",
             "cano", "prego", "cobre", "embalagem de marmitex", "papel alumínio limpo", "lata de aerossol",
             "metal", "metais")
    return metal


def organicos():
    organico = ("gordura", "restos de alimentos", "carne", "vegetais", "frutas", "ossos", "café", "chá",
                "casca de ovo", "sementes", "folhas", "caule", "madeira", "dejetos humanos", "fezes",
                "organico", "organicos", "material organico", "materiais organicos", "materias organico")
    return organico


def eletronicos():
    eletronico = ("pilha", "pilhas", "bateria", "baterias", "bateria de carro", "computador", "smartphone",
                  "placa-mae", "processador", "fone de ouvido", "fonte", "memoria ram", "cooler",
                  "computador", "monitor", "televisor", "notebook", "celular", "tablet", "central telefonica",
                  "impressora", "video cassete", "aparelho de DVD", "aparelho de som", "microondas", "micro-ondas",
                  "nobreak", "modem", "cabo")
    return eletronico


def entulhos():
    entulho = ("entulho", "entulhos", "material de construção", "cimento", "tijolo", "tijolo quebrado", "piso",
               "piso quebrado", "terra", "ceramica", "concreto", "madeira", "areia")
    return entulho


def vegetais():
    vegetal = ("galho", "poda", "grama", "galho de arvore")
    return vegetal


def nao_reciclaveis():
    nao_reciclavel = ("embalagem metalizada", "isopor", "cabo de panela", "espuma",
                      "bandeja de plástico", "acrílico", "papel sanitário", "papel higiênico",
                      "papel plastificado", "papel engordurado", "etiqueta adesiva",
                      "papel parafinado", "papel carbono", "papel celofane", "guardanapo",
                      "bituca de cigarro", "fotografia", "espelho", "boxe temperado", "louça",
                      "óculos", "cerâmica", "porcelana", "pirex", "tubos de tv", "monitor",
                      "para-brisa de carro", "clipes", "grampo", "esponja de aço", "latas de inseticida",
                      "lata de verniz", "lata de solventes químicos")
    return nao_reciclavel


def todos_reciclaveis():
    """
    Função concatenara e retornará todos os reciclaveis 'mais comuns', em formato lista.
    """
    todos_reciclavel = plasticos() + papeis() + vidros() + metais()
    return todos_reciclavel


def todos_materiais_inorganicos():
    """
    Função concatenara e retornará todos os reciclaveis com excessão do organicos, em formato lista.
    """
    todos_material_ingornicos = plasticos() + papeis() + vidros() + metais() + entulhos() + eletronicos() + vegetais()
    return todos_material_ingornicos
