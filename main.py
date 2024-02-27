amarelinha = [[0], [1], [2], [3, 4], [5], [6], [7, 8], [9], [10]]
rodada = 1
indice = 0
pes_em = amarelinha[indice].copy()


def print_local(local):
  if pes_em == [0]:
    print("Você está no início da amarelinha")
  elif pes_em == [10]:
    print("Você está com dois pés no céu")
    print("Você se virou")
  elif len(local) == 2:
    print("Você pisou com dois pés em", local[0], "e", local[1])
  else:
    print("Você pisou com um pé em", local[0])


while rodada < 10:
  pedra_em = rodada
  print("A pedra foi jogada na casa ", pedra_em)

  while pes_em != [10]:
    print_local(pes_em)
    if pedra_em in amarelinha[indice + 1]:
      if len(amarelinha[indice + 1]) == 2:
        indice += 1
        pes_em = amarelinha[indice].copy()
        pes_em.pop(pes_em.index(pedra_em))
      else:
        indice += 2
        pes_em = amarelinha[indice].copy()
    else:
      indice += 1
      pes_em = amarelinha[indice].copy()

  while pes_em != [0]:
    print_local(pes_em)
    if pedra_em in amarelinha[indice - 1]:
      print("Você pegou a pedra")
      if len(amarelinha[indice - 1]) == 2:
        indice -= 1
        pes_em = amarelinha[indice].copy()
        pes_em.pop(pes_em.index(pedra_em))
      else:
        indice -= 2
        pes_em = amarelinha[indice].copy()
    else:
      indice -= 1
      pes_em = amarelinha[indice].copy()

  rodada += 1
  print()

print("Você venceu a amarelinha")