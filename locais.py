""""
Arquivo responsavel por armazenar as informações dos lugares de reciclagem.

"""
import materiais


def lugares():
    """"
    A função retorna um lista como todos os lugares.
    Os lugares que coletam todos os tipos de materiais recebem o 'coletam' proveniente de materiais.py
    """
    locais = [
        # Locais que coletam eletronicos.
        {
            'nome': 'Reversis',
            'coletam': materiais.eletronicos(),
            'latitude': -22.926877,
            'longitude': -47.042982,
            'atendimento': 'Seg a Sex das 7:00 às 15:50',
            'endereco': 'Rua da Abolição, 1900 - Pte. Preta, Campinas-SP'
        },
        # Locais que coletam entulho.
        {
            'nome': 'Usina de Reciclagem de Material de Construção',
            'coletam': materiais.entulhos(),
            'latitude': -22.924649,
            'longitude': -47.145181,
            'atendimento': 'Seg a Sex das 8:00 às 17:30',
            'endereco': 'Rua Doze, 2252 - Jardim São Caetano, Campinas-SP'
        },
        {
            'nome': 'Quinelatto Caçambas',
            'coletam': materiais.entulhos(),
            'latitude': -22.923193,
            'longitude': -47.105345,
            'atendimento': 'Seg a Sex das 8:00 às 18:00',
            'endereco': 'Rua Ernesto Alves Fuilho, 907 - Jardim Campos Eliseos, Campinas-SP'
        },
        {
            'nome': 'Barbosa Caçambas Entulhos',
            'coletam': materiais.entulhos(),
            'latitude': -22.857845,
            'longitude': -47.036500,
            'atendimento': 'Seg a Sex das 8:00 às 18:00',
            'endereco': 'Rua Londres, 28 - Parque São Quirino, Campinas-SP'
        },
        {
            'nome': 'Km Caçambas',
            'coletam': materiais.entulhos(),
            'latitude': -22.893936,
            'longitude': -47.096507,
            'atendimento': 'Seg a Sex das 8:00 às 17:00',
            'endereco': 'Rua Fernando da Cruz Passos, 251 - Jardim Chapadão, Campinas-SP'
        },
        #coletam os tipos mais comuns de reciclaveis.
        {
            'nome': 'Cooperativa de reciclagem',
            'coletam': materiais.todos_reciclaveis(),
            'latitude': -22.909522,
            'longitude': -47.037913,
            'atendimento': 'Seg a Sex das 8:00 às 17:00',
            'endereco': 'Jardim Proença, Campinas - SP'
        },
        {
            'nome': 'GMV Recycle',
            'coletam': materiais.todos_reciclaveis(),
            'latitude': -22.897886,
            'longitude': -47.093400,
            'atendimento': 'Seg a Sex das 7:00 às 19:00',
            'endereco': 'Rod. Lix da Cunha, 911 - Jardim Nova America, Campinas-SP '
        },
        {
            'nome': 'HT Papéis Barão - Coleta e reciclagem de residuos',
            'coletam': materiais.papeis() + materiais.plasticos(),
            'latitude': -22.933731,
            'longitude': -47.105661,
            'atendimento': 'Seg a Sex das 7:00 às 16:30',
            'endereco': 'Av. Ruy Rodrigues, 394 - Jardim Novo Campos Eliseos, Campinas-SP'
        },
        #coletam todos os tipos
        {
            'nome': 'Ecoponto Barão Geraldo',
            'coletam': materiais.todos_materiais_inorganicos(),
            'latitude': -22.817363,
            'longitude': -47.100563,
            'atendimento': 'Seg a Sex das 7:00 às 15:50',
            'endereco': 'Av. Santa Isabel, 2300 - Barão Geraldo, Campinas-SP'
        },
        {
            'nome': 'Ecoponto Vila União',
            'coletam': materiais.todos_materiais_inorganicos(),
            'latitude': -22.817363,
            'longitude': -47.100563,
            'atendimento': 'Seg a Sex das 7:00 às 18:00 e Sab e Dom das 7:00 as 15:20',
            'endereco': 'Rua Manoel Gomes Ferreira, 42 - Parque Tropical, Campinas-SP'
        }
    ]
    return locais
