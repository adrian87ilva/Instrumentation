# (VAL_uc_user - VAL_uc_min) * ((VAL_ue_max - VAL_ue_min) + VAL_ue_min) / (VAL_uc_max - VAL_uc_min)

VAL_range_max = float(input("Digite o range do instrumento: "))
VAL_range_min = 0
VAL_uc_max = 20
VAL_uc_min = 4

VAL_uc_user = float(input("Digite o valor mA de saida atual do instrumento: "))

VAL_ue = (VAL_uc_user - VAL_uc_min) * ((VAL_range_max - VAL_range_min) + VAL_range_min) / (VAL_uc_max - VAL_uc_min)

print("O sinal de saída em mA do instrumento é:", VAL_ue)
