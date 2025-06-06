memoria = [0] * 64
R = {'R0': 0, 'R1': 0, 'R2': 0}
PC = 0

arquivo = input("Nome do arquivo do programa: ")
with open(arquivo, 'r') as f:
    linhas = f.readlines()

instrucoes = []
for linha in linhas:
    linha = linha.strip()
    if linha == '' or linha.startswith('#'):
        continue
    if '#' in linha:
        linha = linha.split('#')[0].strip()
    instrucoes.append(linha)

while PC < len(instrucoes):
    instrucao = instrucoes[PC]
    print(f"\nInstrução: {instrucao}")

    partes = instrucao.replace(',', '').split()
    comando = partes[0]

    if comando == 'LOAD':
        reg = partes[1]
        val = partes[2]
        if val.startswith('[') and val.endswith(']'):
            endereco = int(val[1:-1])
            R[reg] = memoria[endereco]
        else:
            R[reg] = int(val)

    elif comando == 'STORE':
        endereco = int(partes[1][1:-1])
        reg = partes[2]
        memoria[endereco] = R[reg]

    elif comando == 'ADD':
        reg_dest = partes[1]
        reg_src = partes[2]
        R[reg_dest] += R[reg_src]

    elif comando == 'HLT':
        print("Programa finalizado.")
        break

    PC += 1

    print(f"R0: {R['R0']}  R1: {R['R1']}  R2: {R['R2']}  PC: {PC}  Mem[30]: {memoria[30]}")