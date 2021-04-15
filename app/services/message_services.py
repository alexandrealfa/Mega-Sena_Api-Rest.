def message_result(value: str, msg = str):

    if value == 4:
        return f"você obteve 4 acertos e esta entre as {msg[2]}"

    elif value == 5:
        return f"você obteve 5 acertos e esta entre as {msg[1]}"

    elif value == 6:
        if msg[0] == "Não houve ganhadores":
            return "Parabéns você foi o primeiro Ganhador do Grande Prémio"
        return f"você obteve 6 acertos e esta entre as {msg[0]}"

    return "Não foi dessa vez, você não foi sorteado, por favor, tente novamente!."