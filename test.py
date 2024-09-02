def get_subarreglo(a_original, objetivo):
    subarreglo = {}
    limite = 0
    indice = -1
    suma = 0

    if a_original.__len__() > 0:
        for i in range(len(a_original)):
            suma += a_original[i]

            if suma == objetivo:
                limite = i + 1
                indice = 0

            if suma - objetivo in subarreglo:
                if i - subarreglo[suma - objetivo] > limite:
                    limite = i - subarreglo[suma - objetivo]
                    indice = subarreglo[suma - objetivo] + 1

            if suma not in subarreglo:
                subarreglo[suma] = i
        return a_original[indice:indice + limite]
    else:
        return []