from enum import Enum

class SituacaoJogadorEnum(Enum):
    ATIVO = 'Ativo'
    DEPARTAMENTO_MEDICO = 'Departamento Médico'
    SUSPENSO = 'Suspenso da Pelada'
    INATIVO = 'Inativo'

class PosicaoJogadorEnum(Enum):
    CORINGA = 'Coringa'
    DEFENSOR = 'Defensor'
    MEIO_CAMPISTA = 'Meio-campista'
    ATACANTE = 'Atacante'
