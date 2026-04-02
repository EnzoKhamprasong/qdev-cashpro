def calculerReduction(total, fidelite):
  if fidelite is False or 0<=total<30:
    return 0
  if 30<=total<100:
    return 5
  if 100<=total<200:
    return 10